import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import math


# ==============================
# LOAD DATA WITH VACCINE FILTER
# ==============================

def load_data(csv_path, vaccine_name):
    df = pd.read_csv(csv_path)

    df = df[df["vaccine_name"] == vaccine_name]
    df = df.sort_values("date")

    features = df[["demand", "supply", "stock"]].values

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(features)

    return scaled, scaler, df


# ==============================
# CREATE SEQUENCES (30 DAYS)
# ==============================

def create_sequences(data, seq_length=30):
    X = []
    y = []

    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length][0])  # predict demand

    return np.array(X), np.array(y)


# ==============================
# CNN + LSTM MODEL
# ==============================

class CNNLSTM(nn.Module):
    def __init__(self, num_features=3):
        super(CNNLSTM, self).__init__()

        self.cnn = nn.Conv1d(
            in_channels=num_features,
            out_channels=32,
            kernel_size=3
        )

        self.lstm = nn.LSTM(
            input_size=32,
            hidden_size=64,
            num_layers=2,
            batch_first=True,
            dropout=0.2
        )

        self.fc = nn.Linear(64, 1)

    def forward(self, x):
        x = x.permute(0, 2, 1)
        x = torch.relu(self.cnn(x))
        x = x.permute(0, 2, 1)

        lstm_out, _ = self.lstm(x)
        output = self.fc(lstm_out[:, -1, :])

        return output


# ==============================
# TRAIN + EVALUATE
# ==============================

def train_and_evaluate(csv_path, vaccine_name, epochs=80):

    data, scaler, df = load_data(csv_path, vaccine_name)

    if len(data) < 60:
        raise ValueError("Not enough data for selected vaccine")

    X, y = create_sequences(data, seq_length=30)

    split = int(len(X) * 0.8)

    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    X_train = torch.tensor(X_train, dtype=torch.float32)
    y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)

    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)

    model = CNNLSTM(num_features=3)

    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(epochs):
        model.train()

        output = model(X_train)
        loss = criterion(output, y_train)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Evaluation
    model.eval()
    with torch.no_grad():
        predictions = model(X_test_tensor).numpy()

    y_test_real = []
    y_pred_real = []

    for i in range(len(predictions)):
        dummy_true = np.array([[y_test[i], 0, 0]])
        dummy_pred = np.array([[predictions[i][0], 0, 0]])

        inv_true = scaler.inverse_transform(dummy_true)
        inv_pred = scaler.inverse_transform(dummy_pred)

        y_test_real.append(inv_true[0][0])
        y_pred_real.append(inv_pred[0][0])

    rmse = math.sqrt(mean_squared_error(y_test_real, y_pred_real))
    mae = mean_absolute_error(y_test_real, y_pred_real)
    r2 = r2_score(y_test_real, y_pred_real)

    return model, scaler, data, df, rmse, mae, r2


# ==============================
# FUTURE PREDICTION (7 DAYS)
# ==============================

def predict_future(model, scaler, data, days=7):

    model.eval()

    predictions = []
    current_seq = data[-30:]

    for _ in range(days):
        seq_tensor = torch.tensor(
            current_seq.reshape(1, 30, 3),
            dtype=torch.float32
        )

        with torch.no_grad():
            pred = model(seq_tensor)

        pred_value = pred.item()
        predictions.append(pred_value)

        new_row = np.array([
            pred_value,
            current_seq[-1][1],
            current_seq[-1][2]
        ])

        current_seq = np.vstack((current_seq[1:], new_row))

    demand_predictions = []

    for p in predictions:
        dummy = np.array([[p, 0, 0]])
        inv = scaler.inverse_transform(dummy)
        demand_predictions.append(inv[0][0])

    return demand_predictions