import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

st.title("📈 Time-Series Aggregator and Forecaster")

uploaded_file = st.file_uploader("Upload a time-series CSV (columns: date, value)", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['date'])
    df = df.sort_values('date')
    df.set_index('date', inplace=True)

    st.subheader("🔍 Raw Data Preview")
    st.dataframe(df.head())

    st.subheader("🛠 Aggregation & Cleaning")
    freq = st.selectbox("Choose Resampling Frequency", ['D', 'W', 'M'])
    df_resampled = df.resample(freq).mean()
    df_resampled = df_resampled.interpolate(method='linear')

    st.line_chart(df_resampled)

    st.subheader("🧠 Forecast with Prophet")
    forecast_horizon = st.slider("Forecast Horizon (periods)", min_value=10, max_value=365, value=60)
    
    df_prophet = df_resampled.reset_index().rename(columns={'date': 'ds', 'value': 'y'})
    model = Prophet()
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=forecast_horizon, freq=freq)
    forecast = model.predict(future)

    st.write("📊 Forecast Plot")
    fig1 = model.plot(forecast)
    st.pyplot(fig1)

    st.write("📈 Forecast Components")
    fig2 = model.plot_components(forecast)
    st.pyplot(fig2)

    st.success("✅ Forecasting completed successfully!")
else:
    st.info("👆 Upload a CSV file to get started.")
