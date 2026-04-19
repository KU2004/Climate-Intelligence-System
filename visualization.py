import matplotlib.pyplot as plt
from src.utils import save_plot


def plot_all(df, forecast):
    """
    Generate and save all plots for climate analysis
    """

    # ==============================
    # 🌡️ Temperature Trend
    # ==============================
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['temperature'], label='Temperature')
    plt.plot(df['date'], df['temp_ma_30'], label='30-day MA')
    plt.legend()
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")

    save_plot(plt, "outputs/plots/temp_trend.png")
    plt.close()

    # ==============================
    # 🌧️ Rainfall Trend
    # ==============================
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['rainfall'])
    plt.title("Rainfall Trend")
    plt.xlabel("Date")
    plt.ylabel("Rainfall")

    save_plot(plt, "outputs/plots/rainfall.png")
    plt.close()

    # ==============================
    # 🚨 Anomaly Detection
    # ==============================
    plt.figure(figsize=(10, 5))
    anomalies = df[df['anomaly'] == -1]

    plt.plot(df['date'], df['temperature'], label="Temperature")
    plt.scatter(anomalies['date'], anomalies['temperature'], color='red', label="Anomalies")

    plt.legend()
    plt.title("Anomaly Detection")
    plt.xlabel("Date")
    plt.ylabel("Temperature")

    save_plot(plt, "outputs/plots/anomalies.png")
    plt.close()

    # ==============================
    # 🔮 Forecast Plot
    # ==============================
    plt.figure(figsize=(10, 5))
    plt.plot(forecast['ds'], forecast['yhat'])
    plt.title("Temperature Forecast")
    plt.xlabel("Date")
    plt.ylabel("Predicted Temperature")

    save_plot(plt, "outputs/plots/forecast.png")
    plt.close()

    print("✅ All plots generated and saved successfully!")