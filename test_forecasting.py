from forecasting import train_model, forecast_next_days
import matplotlib.pyplot as plt

model, df = train_model()
forecast = forecast_next_days(model, df)

print("Next 7 Day Forecast:")
print(forecast)

plt.plot(forecast)
plt.title("7-Day Vaccine Demand Forecast")
plt.show()