def moving_average(df):
    df['temp_ma_30'] = df['temperature'].rolling(window=30).mean()
    df['rain_ma_30'] = df['rainfall'].rolling(window=30).mean()

    print("✅ Trend Analysis Done")
    return df