import pandas as pd 
import plotly.express as px 
import streamlit as st 

st.set_page_config(page_title="DataPulse", layout="wide", page_icon="🏥")

df = pd.read_csv("health_data.csv")

st.title("🏥 DataPulse - Health Tracker Dashboard")

st.subheader("Raw Data")
with st.expander("🔍 Show Raw Data"):
    st.dataframe(df)

st.divider()

total_steps = df["Steps"].sum()

fig_calories = px.bar(df, x="Date", y="Calories Burned", title="Calories burned per day")
st.plotly_chart(fig_calories)
st.divider()

fig_steps = px.line(df, x="Date", y="Steps", title="Steps Tracked Over Time")
st.plotly_chart(fig_steps)
st.divider()

avg_sleep = df["Sleep Hours"].mean()

col1,col2 = st.columns(2)

with col1:
    st.metric(label="Total Steps", value=(total_steps))
    
with col2:
    st.metric(label="Average Sleep (hrs)", value=f"{avg_sleep:.2f}")

st.divider()

fig_sleep = px.pie(df, values='Sleep Hours', names='Date', title="Sleep hours per day")
st.plotly_chart(fig_sleep)
st.divider()

max_cal = df.loc[df["Calories Burned"].idxmax()]
st.subheader("🔥 Highest Burn Day")
st.write(f"**Date:** {max_cal['Date']}")
st.write(f"**Calories Burned:** {max_cal['Calories Burned']}")