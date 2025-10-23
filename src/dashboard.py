import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="DataInsight Dashboard",
    page_icon="📊",
    layout="wide"
    )

st.title("📊 DataInsight Dashboard")
st.markdown("### Automated CSV Analysis and Visualization")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.info("No file uploaded — using sample dataset.")
    df = pd.read_csv("data/sample_data.csv")

st.subheader("Data Overview")
st.dataframe(df.head())

st.subheader("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Rows", len(df))
with col2:
    st.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
with col3:
    st.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
with col4:
    st.metric(
        "Avg Quantity",
        f"{df['Quantity'].mean():.2f}"
    )

st.subheader("Visualizations")

fig1 = px.bar(
    df, x="Region",
    y="Sales", color="Region",
    title="Sales by Region",
    text_auto=True
    )
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(
    df,
    x="Date",
    y="Profit",
    title="Profit Trend Over Time",
    markers=True)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Profit vs Sales Correlation")
fig3 = px.scatter(
    df, x="Sales",
    y="Profit",
    size="Quantity",
    color="Region",
    hover_name="Region",
    title="Profit vs Sales")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.caption("Created by Noufil Tamboli | Automated CI/CD Data Pipeline Demo 🚀")
