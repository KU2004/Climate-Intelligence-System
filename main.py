# ==============================
# 📦 Imports
# ==============================
from src.synthetic_data import generate_climate_data
from src.data_loader import load_data
from src.preprocessing import preprocess
from src.feature_engineering import create_features
from src.trend_analysis import moving_average
from src.anomaly_detection import detect_anomalies
from src.forecasting import prophet_forecast
from src.visualization import plot_all
from src.utils import log

# 🔥 NEW IMPORTS
from src.risk_analysis import calculate_risk
from src.event_detection import detect_events

import os


def main():
    log("🚀 Pipeline started")

    # Ensure folders exist
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("outputs/forecast", exist_ok=True)   # 🔥 NEW

    # ==============================
    # 1. Generate Data
    # ==============================
    log("Generating synthetic climate data...")
    generate_climate_data()

    # ==============================
    # 2. Load Data
    # ==============================
    log("Loading dataset...")
    df = load_data("data/raw/climate.csv")

    # 🔥 NEW: Validate data
    if df is None or df.empty:
        log("❌ Data loading failed!")
        return

    # ==============================
    # 3. Preprocessing
    # ==============================
    log("Preprocessing data...")
    df = preprocess(df)

    # ==============================
    # 4. Feature Engineering
    # ==============================
    log("Creating features...")
    df = create_features(df)

    # ==============================
    # 5. Trend Analysis
    # ==============================
    log("Performing trend analysis...")
    df = moving_average(df)

    # ==============================
    # 6. Anomaly Detection
    # ==============================
    log("Detecting anomalies...")
    df = detect_anomalies(df)

    # ==============================
    # 🔥 Climate Risk Score
    # ==============================
    log("Calculating climate risk score...")
    df = calculate_risk(df)

    # ==============================
    # 🔥 Extreme Event Detection
    # ==============================
    log("Detecting extreme climate events...")
    df = detect_events(df)

    # ==============================
    # 💾 Save Processed Data
    # ==============================
    df.to_csv("data/processed/climate_processed.csv", index=False)
    log("✅ Processed data saved to data/processed/climate_processed.csv")

    # ==============================
    # 🔥 Forecasting (Per City)
    # ==============================
    log("Generating forecast for each city...")

    forecasts = []

    if 'city' in df.columns:
        for city in df['city'].unique():
            log(f"Forecasting for {city}...")

            city_df = df[df['city'] == city].copy()

            forecast = prophet_forecast(city_df)

            forecast['city'] = city  # 🔥 Tag city
            forecasts.append(forecast)

        final_forecast = pd.concat(forecasts)

    else:
        final_forecast = prophet_forecast(df)

    # 🔥 Save forecast
    final_forecast.to_csv("outputs/forecast/forecast.csv", index=False)
    log("✅ Forecast saved to outputs/forecast/forecast.csv")

    # ==============================
    # 8. Visualization
    # ==============================
    log("Generating visualizations...")
    plot_all(df, final_forecast)

    log("✅ Pipeline executed successfully!")


# ==============================
# ▶️ Entry Point
# ==============================
if __name__ == "__main__":
    import pandas as pd  # 🔥 FIX: ensure pandas available here
    main()