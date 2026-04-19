import streamlit as st
import pandas as pd
import os
from PIL import Image

# ==============================
# ⚙️ Page Config
# ==============================
st.set_page_config(
    page_title="Climate Trend Analyzer",
    layout="wide",
    page_icon="🌍"
)

st.title("🌍 Climate Trend Analyzer Dashboard")
st.markdown("Advanced Climate Analysis with Trend, Anomaly Detection, Risk Scoring & Forecasting")

# ==============================
# 📂 Load Processed Data
# ==============================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/processed/climate_processed.csv")
        df['date'] = pd.to_datetime(df['date'])
        return df
    except:
        return None

df = load_data()

# ==============================
# 🚨 Data Check
# ==============================
if df is None:
    st.error("❌ Processed data not found. Please run `python main.py` first.")
    st.stop()

# ==============================
# 🎛 Sidebar Filters
# ==============================
st.sidebar.header("📊 Filters")

# 🔥 NEW: City Filter
city = st.sidebar.selectbox("Select City", df['city'].unique())

year = st.sidebar.selectbox("Select Year", sorted(df['date'].dt.year.unique()))
month = st.sidebar.selectbox("Select Month", list(range(1, 13)))

filtered_df = df[
    (df['city'] == city) &
    (df['date'].dt.year == year) &
    (df['date'].dt.month == month)
]

# 🔥 NEW: Show Selected Region
st.markdown(f"### 📍 Selected Region: **{city}**")

# ==============================
# 📊 KPI Metrics
# ==============================
col1, col2, col3 = st.columns(3)

col1.metric("🌡 Avg Temperature", f"{filtered_df['temperature'].mean():.2f}")
col2.metric("🌧 Total Rainfall", f"{filtered_df['rainfall'].sum():.2f}")
col3.metric("💧 Avg Humidity", f"{filtered_df['humidity'].mean():.2f}")

# ==============================
# 🔥 Risk Score KPI
# ==============================
st.subheader("⚠️ Climate Risk Analysis")

col1, col2 = st.columns(2)

col1.metric("Avg Risk Score", f"{filtered_df['risk_score'].mean():.2f}")
col2.metric("Most Common Risk Level", filtered_df['risk_level'].mode()[0])

# ==============================
# 📈 Live Charts
# ==============================
st.subheader("📈 Climate Trends")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌡 Temperature")
    st.line_chart(filtered_df.set_index('date')['temperature'])

with col2:
    st.markdown("### 🌧 Rainfall")
    st.line_chart(filtered_df.set_index('date')['rainfall'])

# ==============================
# 🔥 NEW: Multi-City Comparison
# ==============================
st.subheader("🌍 Multi-City Temperature Comparison")

comparison = df[df['date'].dt.year == year]

pivot = comparison.pivot_table(
    index='date',
    columns='city',
    values='temperature'
)

st.line_chart(pivot)

# ==============================
# 🔥 Risk Distribution
# ==============================
st.subheader("📊 Risk Level Distribution")
st.bar_chart(filtered_df['risk_level'].value_counts())

# ==============================
# 🚨 Anomaly Detection
# ==============================
st.subheader("🚨 Anomaly Detection")

if 'anomaly' in df.columns:
    anomalies = df[df['anomaly'] == -1]

    st.success(f"Total Anomalies Detected: {len(anomalies)}")

    st.dataframe(anomalies[['date', 'temperature', 'rainfall', 'humidity']].head(10))
else:
    st.warning("⚠️ No anomaly data found. Run pipeline again.")

# ==============================
# 🔥 Extreme Events
# ==============================
st.subheader("🚨 Extreme Climate Events")

if 'event' in df.columns:
    events = filtered_df['event'].value_counts().reset_index()
    events.columns = ['Event Type', 'Count']
    st.dataframe(events)
else:
    st.warning("Run main.py to generate events")

# ==============================
# 🖼 Generated Plots
# ==============================
st.subheader("📊 Generated Analysis Plots")

plot_paths = {
    "Temperature Trend": "outputs/plots/temp_trend.png",
    "Rainfall Trend": "outputs/plots/rainfall.png",
    "Anomaly Detection": "outputs/plots/anomalies.png",
    "Forecast": "outputs/plots/forecast.png"
}

cols = st.columns(2)

i = 0
for title, path in plot_paths.items():
    if os.path.exists(path):
        img = Image.open(path)
        with cols[i % 2]:
            st.markdown(f"### {title}")
            st.image(img, use_container_width=True)
    else:
        st.warning(f"{title} not found. Run main.py first.")
    i += 1

# ==============================
# 📋 Dataset Preview
# ==============================
st.subheader("📋 Dataset Preview")
st.dataframe(filtered_df.head(20))

# ==============================
# 📌 Insights Section
# ==============================
st.subheader("📌 Insights")

total_anomalies = len(df[df['anomaly'] == -1]) if 'anomaly' in df.columns else 0

st.markdown(f"""
- 📈 Temperature shows seasonal variation with increasing trend  
- 🌧 Rainfall fluctuates based on seasonal cycles  
- 🚨 {total_anomalies} anomalies detected  
- ⚠️ Risk level is mostly **{filtered_df['risk_level'].mode()[0]}**  
- 🔥 Extreme events like heatwaves, floods, or droughts detected  
""")

# ==============================
# 👨‍💻 Footer
# ==============================
st.markdown("---")
st.markdown("🚀 Built using Python, Machine Learning, Time-Series Analysis & Streamlit")