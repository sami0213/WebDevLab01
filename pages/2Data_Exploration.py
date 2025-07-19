
import streamlit as st
import pandas as pd
import plotly.express as px
import json


# Load data from data.json
with open("data.json", "r") as f:
    data = json.load(f)
df = pd.DataFrame(data)

# Initialize session state for selected subject
if "selected_subject" not in st.session_state:
    st.session_state.selected_subject = df["subject"].unique()[0]

# App title and description
st.title("My Study Habits Dashboard")
st.markdown("""
This page explores my study habits using interactive visualizations.
You can filter study hours, select subjects, and view trends over time.
""")

# User inputs
subject = st.selectbox("Choose a subject to explore:", df["subject"].unique())
st.session_state.selected_subject = subject

hour_range = st.slider("Filter by study hours:", 0, 10, (1, 8))  # User input 2

# NEW: Streamlit divider
st.divider()  # NEW

# NEW: Streamlit toast
st.toast("Study data loaded successfully!")  # NEW

# NEW: Streamlit caption
st.caption("Data source: Personal study log (data.json)")  # NEW

# Tabs for each graph
tab1, tab2, tab3 = st.tabs(["Total Study Time", "Filtered Study Hours", "Study Trend"])

# Static Graph: Pie chart of total study time
with tab1:
    st.subheader("Total Study Time by Subject")
    total_time = df.groupby("subject")["hours"].sum().reset_index()
    fig_static = px.pie(total_time, names="subject", values="hours", title="Study Time Distribution")
    st.plotly_chart(fig_static)

# Dynamic Graph 1: Bar chart of study hours per subject
with tab2:
    st.subheader("Study Hours per Subject (Filtered)")
    filtered_df = df[(df["hours"] >= hour_range[0]) & (df["hours"] <= hour_range[1])]
    fig_dynamic1 = px.bar(filtered_df, x="subject", y="hours", color="subject", title="Filtered Study Hours")
    st.plotly_chart(fig_dynamic1)

# Dynamic Graph 2: Line chart of study hours over time for selected subject
with tab3:
    st.subheader(f"Study Trend for {st.session_state.selected_subject}")
    subject_df = df[df["subject"] == st.session_state.selected_subject]
    fig_dynamic2 = px.line(subject_df, x="date", y="hours", title=f"Study Hours Over Time: {st.session_state.selected_subject}")
    st.plotly_chart(fig_dynamic2)
