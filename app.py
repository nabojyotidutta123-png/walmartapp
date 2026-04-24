import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# ===================== CONFIG =====================
st.set_page_config(layout="wide", page_title="AI Retail Inventory Dashboard")

base_path = r"C:\Users\CHUMKI\Downloads\Amity\output"

# ===================== LOAD DATA =====================
df = pd.read_csv(os.path.join(base_path, "final_inventory_output.csv"))
df['Date'] = pd.to_datetime(df['Date'])

forecast_path = os.path.join(base_path, "forecast_output.csv")
perf_path = os.path.join(base_path, "model_performance.csv")

forecast_df = pd.read_csv(forecast_path) if os.path.exists(forecast_path) else None
perf_df = pd.read_csv(perf_path) if os.path.exists(perf_path) else None

# ===================== SIDEBAR =====================
st.sidebar.title("📊 Navigation")

module = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Overview",
        "📊 EDA",
        "📅 Seasonality",
        "🔁 Cycle & Trend",
        "📈 Forecasting",
        "🔮 Forecast View",
        "📦 Inventory Optimization",
        "⚠️ Alerts",
        "🤖 Model Performance",
        "💼 Business Insights"
    ]
)

# ===================== FILTERS =====================
store = st.sidebar.selectbox("Store", sorted(df['Store'].unique()))
dept = st.sidebar.selectbox("Department", sorted(df['Dept'].unique()))

filtered = df[(df['Store']==store) & (df['Dept']==dept)]

# ===================== OVERVIEW =====================
if module == "🏠 Overview":
    st.title("🏠 Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"{filtered['Weekly_Sales'].sum():,.0f}")
    col2.metric("Stockout Rate", f"{filtered['Stockout'].mean()*100:.2f}%")
    col3.metric("Total Cost", f"{filtered['Total_Cost'].sum():,.0f}")

    fig = px.line(filtered, x='Date', y='Weekly_Sales')
    st.plotly_chart(fig, use_container_width=True)

# ===================== EDA =====================
elif module == "📊 EDA":
    st.title("📊 EDA")

    fig1 = px.box(filtered, x='IsHoliday', y='Weekly_Sales')
    st.plotly_chart(fig1, use_container_width=True)

# ===================== SEASONALITY =====================
elif module == "📅 Seasonality":
    st.title("📅 Seasonality")

    monthly = filtered.groupby('Month')['Weekly_Sales'].mean().reset_index()
    st.plotly_chart(px.bar(monthly, x='Month', y='Weekly_Sales'), use_container_width=True)

    weekly = filtered.groupby('Week')['Weekly_Sales'].mean().reset_index()
    st.plotly_chart(px.line(weekly, x='Week', y='Weekly_Sales'), use_container_width=True)

# ===================== CYCLE =====================
elif module == "🔁 Cycle & Trend":
    st.title("🔁 Cycle & Trend")

    ts = filtered.groupby('Date')['Weekly_Sales'].sum().reset_index()
    ts['Smooth'] = ts['Weekly_Sales'].rolling(12).mean()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ts['Date'], y=ts['Weekly_Sales'], name="Actual"))
    fig.add_trace(go.Scatter(x=ts['Date'], y=ts['Smooth'], name="Trend"))

    st.plotly_chart(fig, use_container_width=True)

# ===================== FORECASTING =====================
elif module == "📈 Forecasting":
    st.title("📈 Forecasting")

    if forecast_df is not None:
        st.plotly_chart(
            px.line(forecast_df, x='ds', y='yhat', title="Forecast Trend"),
            use_container_width=True
        )

# ===================== 🔮 FORECAST VIEW =====================
elif module == "🔮 Forecast View":
    st.title("🔮 Forecast View (Actual vs Forecast)")

    if forecast_df is not None:

        # Aggregate actual
        actual = df.groupby('Date')['Weekly_Sales'].sum().reset_index()

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=actual['Date'],
            y=actual['Weekly_Sales'],
            name="Actual",
            line=dict(color='blue')
        ))

        fig.add_trace(go.Scatter(
            x=forecast_df['ds'],
            y=forecast_df['yhat'],
            name="Forecast",
            line=dict(color='red')
        ))

        fig.update_layout(title="Actual vs Forecast Comparison")

        st.plotly_chart(fig, use_container_width=True)

        # ===================== FUTURE FORECAST TABLE =====================
        future_forecast = forecast_df.tail(12)

        st.subheader("📊 Future Forecast (Next 12 Weeks)")
        st.dataframe(future_forecast[['ds','yhat']])

        # ===================== DOWNLOAD BUTTON =====================
        csv = future_forecast.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="📥 Download Forecast (CSV)",
            data=csv,
            file_name="forecast_output.csv",
            mime='text/csv'
        )

    else:
        st.warning("⚠️ Forecast data not available")

# ===================== INVENTORY =====================
elif module == "📦 Inventory Optimization":
    st.title("📦 Inventory")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered['Date'], y=filtered['Stock'], name="Stock"))
    fig.add_trace(go.Scatter(x=filtered['Date'], y=filtered['Demand'], name="Demand"))

    st.plotly_chart(fig, use_container_width=True)

# ===================== ALERTS =====================
elif module == "⚠️ Alerts":
    st.title("⚠️ Alerts")

    alerts = filtered[filtered['Stock'] < filtered['Reorder_Point']]
    st.dataframe(alerts[['Date','Stock','Reorder_Point']])

# ===================== MODEL PERFORMANCE =====================
elif module == "🤖 Model Performance":
    st.title("🤖 Model Performance")

    if perf_df is not None:
        st.dataframe(perf_df)

        st.plotly_chart(px.bar(perf_df, x='Model', y='MAE'), use_container_width=True)
        st.plotly_chart(px.bar(perf_df, x='Model', y='RMSE'), use_container_width=True)

        best = perf_df.loc[perf_df['RMSE'].idxmin(), 'Model']
        st.success(f"🏆 Best Model: {best}")

# ===================== BUSINESS =====================
elif module == "💼 Business Insights":
    st.title("💼 Business Insights")

    st.markdown("""
    - Seasonal demand patterns identified  
    - Stockouts driven by delayed replenishment  
    - Forecast improves planning accuracy  

    **Recommendations:**
    - Dynamic reorder policies  
    - Safety stock optimization  
    - ML-driven procurement  
    """)