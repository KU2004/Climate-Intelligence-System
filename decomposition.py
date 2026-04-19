from statsmodels.tsa.seasonal import seasonal_decompose

def decompose(df):
    result = seasonal_decompose(df['temperature'], model='additive', period=365)
    return result