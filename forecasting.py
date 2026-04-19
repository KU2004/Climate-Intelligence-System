from prophet import Prophet

def prophet_forecast(df):
    prophet_df = df[['date', 'temperature']].rename(columns={'date': 'ds', 'temperature': 'y'})

    model = Prophet()
    model.fit(prophet_df)

    future = model.make_future_dataframe(periods=365)
    forecast = model.predict(future)

    print("✅ Forecast Generated")
    return forecast