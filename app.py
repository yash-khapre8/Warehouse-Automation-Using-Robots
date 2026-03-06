import streamlit as st
import pandas as pd
import random

# Page Config
st.set_page_config(
    page_title="Warehouse Automation Dashboard",
    page_icon="📦",
    layout="wide"
)

# Title
st.title("📦 Warehouse Automation Analytics Dashboard")
st.markdown("Real-time simulation and financial analysis of robotic warehouse automation.")

st.divider()

# Sidebar
st.sidebar.header("⚙ Simulation Controls")

orders = st.sidebar.slider("Number of Orders", 50, 500, 150)
min_time = st.sidebar.slider("Minimum Robot Task Time", 3, 10, 5)
max_time = st.sidebar.slider("Maximum Robot Task Time", 10, 30, 20)

# Financial Inputs
current_cost = 6
labor_reduction = 0.35
error_reduction = 0.40
investment = 3.5

labor_savings = current_cost * labor_reduction
error_savings = current_cost * error_reduction
total_savings = labor_savings + error_savings
net_benefit = total_savings - investment

# KPI Section
st.subheader("📊 Financial Performance")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Labor Savings", f"₹{labor_savings} Cr", "35% reduction")
col2.metric("Error Savings", f"₹{error_savings} Cr", "40% reduction")
col3.metric("Total Savings", f"₹{total_savings} Cr")
col4.metric("Net Benefit", f"₹{net_benefit} Cr")

st.divider()

# Generate Synthetic Data
data = {
    "Order_ID": [i for i in range(1, orders+1)],
    "Robot_Task_Time_sec": [random.randint(min_time, max_time) for _ in range(orders)],
    "Picking_Accuracy_%": [round(random.uniform(95,100),2) for _ in range(orders)],
    "Daily_Order_Volume": [random.randint(12000,15000) for _ in range(orders)]
}

df = pd.DataFrame(data)

# Data Insights
avg_time = df["Robot_Task_Time_sec"].mean()
avg_accuracy = df["Picking_Accuracy_%"].mean()
max_orders = df["Daily_Order_Volume"].max()

# Charts Layout
st.subheader("📈 Warehouse Operational Analytics")

chart1, chart2 = st.columns(2)

with chart1:
    st.markdown("### Robot Task Time")
    st.bar_chart(df["Robot_Task_Time_sec"])

with chart2:
    st.markdown("### Picking Accuracy")
    st.line_chart(df["Picking_Accuracy_%"])

st.divider()

# Operational Insights
st.subheader("📉 Operational Insights")

c1, c2, c3 = st.columns(3)

c1.metric("Avg Robot Task Time", f"{avg_time:.2f} sec")
c2.metric("Avg Picking Accuracy", f"{avg_accuracy:.2f}%")
c3.metric("Peak Daily Orders", f"{max_orders}")

st.divider()

# Data Table
st.subheader("📋 Warehouse Data Preview")
st.dataframe(df, use_container_width=True)

# Download Button
st.download_button(
    label="⬇ Download Dataset",
    data=df.to_csv(index=False),
    file_name="warehouse_data.csv",
    mime="text/csv"
)

st.divider()

# Recommendation Section
st.subheader("📌 Business Recommendation")

if net_benefit > 0:
    st.success(
        f"""
        Automation investment is financially beneficial.

        **Expected Net Benefit:** ₹{net_benefit} Crores  
        The warehouse automation system improves efficiency,
        reduces human error, and enhances order fulfillment speed.
        """
    )
else:
    st.error(
        "Automation investment may not be profitable under current assumptions."
    )

st.caption("Developed using Streamlit | Warehouse Automation Simulation")