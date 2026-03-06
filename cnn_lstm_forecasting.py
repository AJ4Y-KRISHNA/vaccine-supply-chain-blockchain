import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# ===========================
# LOAD DATA
# ===========================

def load_data(csv_path):
    df = pd.read_csv(csv_path)

    # Use only demand column
    values = df["demand"].values.reshape(-1, 1)

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(values)

    return scaled, scaler


# ===========================
# CREATE SEQUENCES
# ===========================

def create_sequences(data, seq_length=14):
    xs = []
    ys = []

    for i in range(len(data) - seq_length):
        x = data[i:(i + seq_length)]
        y = data[i + seq_length]
        xs.append(x)
        ys.append(y)

    return np.array(xs), np.array(ys)


# ===========================
# CNN-LSTM MODEL
# ===========================

class CNNLSTM(nn.Module):
    def __init__(self):
        super(CNNLSTM, self).__init__()

        self.cnn = nn.Conv1d(
            in_channels=1,
            out_channels=16,
            kernel_size=3
        )

        self.lstm = nn.LSTM(
            input_size=16,
            hidden_size=32,
            num_layers=1,
            batch_first=True
        )

        self.fc = nn.Linear(32, 1)

    def forward(self, x):
        x = x.permute(0, 2, 1)        # (batch, channel, seq)
        x = torch.relu(self.cnn(x))
        x = x.permute(0, 2, 1)        # back to (batch, seq, features)

        lstm_out, _ = self.lstm(x)
        out = self.fc(lstm_out[:, -1, :])

        return out


# ===========================
# TRAIN MODEL
# ===========================

def train_model(csv_path, epochs=30):

    scaled_data, scaler = load_data(csv_path)
    X, y = create_sequences(scaled_data)

    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.float32)

    model = CNNLSTM()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(epochs):
        model.train()

        outputs = model(X_tensor)
        loss = criterion(outputs, y_tensor)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.6f}")

    return model, scaler


# ===========================
# PREDICT FUTURE DAYS
# ===========================

def predict_future(model, scaler, data, days=7):

    model.eval()

    predictions = []
    current_seq = data[-14:]

    for _ in range(days):
        seq_tensor = torch.tensor(
            current_seq.reshape(1, 14, 1),
            dtype=torch.float32
        )

        with torch.no_grad():
            pred = model(seq_tensor)

        predictions.append(pred.item())

        current_seq = np.append(current_seq[1:], pred.item())

    predictions = scaler.inverse_transform(
        np.array(predictions).reshape(-1, 1)
    )

    return predictions.flatten()