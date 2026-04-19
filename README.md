# 🌍 Climate Intelligence System

An advanced data-driven system designed to analyze climate trends, detect anomalies, assess risk levels, identify extreme environmental events, and forecast future climate patterns using Machine Learning and Time-Series techniques.

---

## 🚀 Project Overview

Climate change is one of the most critical global challenges. This project simulates a real-world **Climate Intelligence Platform** that helps:

- Analyze long-term climate trends  
- Detect abnormal environmental behavior  
- Identify extreme events like heatwaves, floods, and droughts  
- Calculate climate risk levels  
- Forecast future climate conditions  

---

## 🎯 Problem Statement

Traditional climate analysis systems lack integrated tools for:

- Real-time insights  
- Risk-based decision-making  
- Multi-region comparison  
- Predictive modeling  

This project solves these gaps by building an **end-to-end climate analytics system**.

---

## 💡 Key Features

### 📊 Data Analysis
- Time-series climate data processing  
- Trend analysis using moving averages  
- Seasonal pattern simulation  

### 🤖 Machine Learning
- Anomaly Detection using Isolation Forest  
- Forecasting using Prophet  

### ⚠️ Risk Intelligence
- Climate Risk Score (0–100)  
- Risk categorization (Low, Medium, High)  

### 🚨 Event Detection
- Heatwaves  
- Flood risk  
- Drought conditions  

### 🌍 Multi-Region Analysis
- Mumbai, Delhi, Bangalore comparison  
- City-wise filtering  
- Cross-region trend visualization  

### 📈 Dashboard (Streamlit)
- Interactive filters (City, Year, Month)  
- KPI metrics  
- Trend charts  
- Risk distribution  
- Anomaly detection  
- Event analysis  
- Multi-city comparison  

---

## 🏗️ Project Architecture
Data Generation → Preprocessing → Feature Engineering
↓
Trend Analysis → Anomaly Detection → Risk Scoring
↓
Event Detection → Forecasting → Visualization Dashboard

---

## 📁 Folder Structure
Climate-Intelligence-System/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── src/
│ ├── synthetic_data.py
│ ├── preprocessing.py
│ ├── feature_engineering.py
│ ├── trend_analysis.py
│ ├── anomaly_detection.py
│ ├── forecasting.py
│ ├── risk_analysis.py
│ ├── event_detection.py
│ ├── visualization.py
│ ├── utils.py
│
├── app/
│ └── streamlit_app.py
│
├── outputs/
│ ├── plots/
│ ├── forecast/
│
├── main.py
├── requirements.txt
└── README.md

---

## ⚙️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Prophet  
- Matplotlib  
- Streamlit  

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
python main.py
streamlit run app/streamlit_app.py
