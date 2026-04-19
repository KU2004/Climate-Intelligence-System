import pandas as pd
import numpy as np
import os

def generate_climate_data(output_path="data/raw/climate.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    np.random.seed(42)

    cities = ["Mumbai", "Delhi", "Bangalore"]
    all_data = []

    for city in cities:
        dates = pd.date_range(start="2010-01-01", periods=1000)
        day_of_year = dates.dayofyear.to_numpy()

        trend = 0.02 * np.arange(1000)

        seasonal = 10 * np.sin(2 * np.pi * day_of_year / 365)
        noise = np.random.normal(0, 2, 1000)

        base_temp = {
            "Mumbai": 28,
            "Delhi": 25,
            "Bangalore": 22
        }[city]

        temperature = base_temp + trend + seasonal + noise

        rainfall = 100 + 30 * np.sin(2 * np.pi * day_of_year / 365) + np.random.normal(0, 10, 1000)
        humidity = 60 + 20 * np.sin(2 * np.pi * day_of_year / 365) + np.random.normal(0, 5, 1000)

        # anomalies
        anomaly_idx = np.random.choice(range(1000), size=20)
        temperature[anomaly_idx] += np.random.uniform(10, 15, 20)

        df = pd.DataFrame({
            "date": dates,
            "city": city,
            "temperature": temperature,
            "rainfall": rainfall,
            "humidity": humidity
        })

        all_data.append(df)

    final_df = pd.concat(all_data)
    final_df.to_csv(output_path, index=False)

    print("✅ Multi-city dataset generated!")