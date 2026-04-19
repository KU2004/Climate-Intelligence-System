import os
import pandas as pd
from datetime import datetime


# ==============================
# 📁 Create Directory if not exists
# ==============================
def create_dir(path):
    """
    Create directory if it does not exist
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📁 Created directory: {path}")


# ==============================
# 💾 Save DataFrame to CSV
# ==============================
def save_csv(df, path):
    """
    Save DataFrame to CSV file
    """
    create_dir(os.path.dirname(path))
    df.to_csv(path, index=False)
    print(f"💾 Data saved at: {path}")


# ==============================
# 📊 Load CSV safely
# ==============================
def load_csv(path):
    """
    Load CSV file with error handling
    """
    try:
        df = pd.read_csv(path)
        print(f"✅ Loaded data from {path}")
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        return None


# ==============================
# 🕒 Get current timestamp
# ==============================
def get_timestamp():
    """
    Returns current timestamp string
    """
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# ==============================
# 🧾 Simple Logger
# ==============================
def log(message):
    """
    Print log message with timestamp
    """
    print(f"[{get_timestamp()}] {message}")


# ==============================
# 📉 Normalize column (optional)
# ==============================
def normalize_column(df, column):
    """
    Normalize a column (min-max scaling)
    """
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df


# ==============================
# 🔍 Check missing values
# ==============================
def check_missing(df):
    """
    Print missing value summary
    """
    missing = df.isnull().sum()
    print("🔍 Missing Values:\n", missing)
    return missing


# ==============================
# 📌 Save Plot Safely
# ==============================
def save_plot(plt, path):
    """
    Save matplotlib plot safely
    """
    create_dir(os.path.dirname(path))
    plt.savefig(path)
    print(f"📊 Plot saved at: {path}")