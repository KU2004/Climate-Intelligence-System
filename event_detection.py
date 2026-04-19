def detect_events(df):
    def classify(row):
        if row['temperature'] > 40:
            return "Heatwave"
        elif row['rainfall'] > 180:
            return "Flood Risk"
        elif row['rainfall'] < 20:
            return "Drought"
        else:
            return "Normal"

    df['event'] = df.apply(classify, axis=1)

    print("✅ Event Detection Done")
    return df