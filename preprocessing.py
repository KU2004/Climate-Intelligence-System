import pandas as pd
from src.utils import check_missing


def preprocess(df):
    """
    Clean and prepare climate dataset
    """

    # Convert date column
    df['date'] = pd.to_datetime(df['date'])

    # Sort by date
    df = df.sort_values('date')

    # Check missing values BEFORE handling
    print("🔍 Checking missing values BEFORE cleaning:")
    check_missing(df)

    # Handle missing values (forward fill)
    df = df.fillna(method='ffill')

    # Check missing values AFTER handling
    print("🔍 Checking missing values AFTER cleaning:")
    check_missing(df)

    print("✅ Preprocessing Done")

    return df