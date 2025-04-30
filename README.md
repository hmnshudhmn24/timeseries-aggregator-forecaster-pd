# 📈 Time-Series Aggregator and Forecaster (with Prophet) 🧠

This **Streamlit-based tool** uses **Pandas** for resampling and interpolation, and **Prophet** for intelligent forecasting. Great for business insights, sales, sensor data, or energy use patterns.

## 🔧 Features

- Resample and clean time-series data
- Fill missing values via interpolation
- Forecast future values with Facebook Prophet
- Auto-detects frequency (daily, weekly, monthly)
- Interactive forecast and seasonality plots

## 🗃 Sample Data Format

```csv
date,value
2023-01-01,100
2023-01-02,105
...
```

## 🚀 How to Run

1. Install dependencies:

```bash
pip install pandas streamlit prophet matplotlib
```

2. Start the app:

```bash
streamlit run app/main.py
```

3. Upload your time-series file and interact with forecasts!

## 📁 Project Structure

- `app/main.py` – Main Streamlit app
- `data/data.csv` – Sample time-series data
- `README.md` – Project documentation
