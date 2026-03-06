import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def load_data():
    df = pd.read_csv("data/vaccine_demand.csv")
    return df

def train_model():
    df = load_data()
    
    df["day"] = np.arange(len(df))
    
    X = df[["day"]]
    y = df["demand"]

    model = RandomForestRegressor(n_estimators=200)
    model.fit(X, y)

    predictions = model.predict(X)
    mae = mean_absolute_error(y, predictions)

    return model, df, mae

def forecast_next_days(model, df, days=7):
    last_day = df["day"].iloc[-1]
    future_days = np.arange(last_day + 1, last_day + 1 + days)
    
    future_df = pd.DataFrame({"day": future_days})
    predictions = model.predict(future_df)

    return predictions