import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from cnn_lstm_multifeature import train_and_evaluate, predict_future

st.title("📊 AI Demand Forecasting (CNN-LSTM)")

df = pd.read_csv("data/vaccine_demand.csv")

vaccine_list = df["vaccine_name"].unique()

selected_vaccine = st.selectbox("Select Vaccine", vaccine_list)

if st.button("Train Model & Predict"):

    with st.spinner("Training CNN-LSTM Model..."):

        model, scaler, data, filtered_df, rmse, mae, r2 = train_and_evaluate(
            "data/vaccine_demand.csv",
            selected_vaccine,
            epochs=80
        )

        future = predict_future(model, scaler, data, days=7)

    st.success("Model Training Completed")

    col1, col2, col3 = st.columns(3)

    col1.metric("RMSE", f"{rmse:.2f}")
    col2.metric("MAE", f"{mae:.2f}")
    col3.metric("R² Score", f"{r2:.3f}")

    st.subheader("Next 7 Days Forecast")
    st.write(future)

    plt.figure(figsize=(10, 5))

    plt.plot(
        filtered_df["demand"].values[-30:],
        label="Last 30 Days"
    )

    future_index = range(
        len(filtered_df)-1,
        len(filtered_df)-1 + 7
    )

    plt.plot(
        future_index,
        future,
        marker='o',
        label="Forecast"
    )

    plt.legend()
    plt.title(f"{selected_vaccine} Demand Forecast")
    plt.xlabel("Time")
    plt.ylabel("Demand")

    st.pyplot(plt)