import streamlit as st
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8000"   # your FastAPI server

st.title("🌟 Simple To-Do Client (Streamlit + FastAPI)")

# ---- ADD TASK ----
st.header("➕ Add Task")

task_text = st.text_input("Task")
task_date_input = st.date_input("Select Date")  # calendar input

# Convert date to DD-MM-YYYY
task_date = task_date_input.strftime("%d-%m-%Y")

if st.button("Add Task"):
    if task_text:
        payload = {"task": task_text, "date": task_date}
        r = requests.post(f"{API_URL}/add", json=payload)
        st.success(r.json()["message"])
    else:
        st.error("Task cannot be empty.")

# ---- VIEW BY DATE ----
st.header("📅 View Tasks by Date")

view_date_input = st.date_input("Pick date to view", key="view_date")

view_date = view_date_input.strftime("%d-%m-%Y")

if st.button("View Tasks"):
    r = requests.get(f"{API_URL}/view/{view_date}")
    st.write(r.json())

# ---- VIEW ALL ----
st.header("📋 View All Tasks (Sorted)")

if st.button("Show All Tasks"):
    r = requests.get(f"{API_URL}/view_all")
    st.write(r.json())
