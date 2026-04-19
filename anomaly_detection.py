from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.01, random_state=42)

    df['anomaly'] = model.fit_predict(df[['temperature', 'rainfall', 'humidity']])

    print("✅ Anomaly Detection Done")
    return df