def calculate_risk(df):
    # Normalize values
    df['temp_norm'] = (df['temperature'] - df['temperature'].min()) / (df['temperature'].max() - df['temperature'].min())
    df['rain_norm'] = (df['rainfall'] - df['rainfall'].min()) / (df['rainfall'].max() - df['rainfall'].min())

    # Risk score
    df['risk_score'] = (
        df['temp_norm'] * 0.5 +
        (1 - df['rain_norm']) * 0.3 +
        (df['anomaly'] == -1).astype(int) * 0.2
    ) * 100

    # Risk category
    def categorize(score):
        if score > 70:
            return "HIGH"
        elif score > 40:
            return "MEDIUM"
        else:
            return "LOW"

    df['risk_level'] = df['risk_score'].apply(categorize)

    print("✅ Risk Analysis Done")
    return df