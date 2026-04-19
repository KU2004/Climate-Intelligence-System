def create_features(df):
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day

    # Seasons
    df['season'] = df['month'] % 12 // 3 + 1

    print("✅ Features Created")
    return df