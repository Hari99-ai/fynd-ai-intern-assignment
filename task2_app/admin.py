import streamlit as st
import pandas as pd

DATA_PATH = "data/feedback.csv"

st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("📊 Admin Feedback Dashboard")

df = pd.read_csv(DATA_PATH)

if df.empty:
    st.info("No feedback submitted yet.")
else:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Feedback", len(df))

    with col2:
        st.metric("Average Rating", round(df["rating"].mean(), 2))

    with col3:
        st.metric("5-Star Reviews", (df["rating"] == 5).sum())

    st.divider()

    st.subheader("All Submissions")
    st.dataframe(
        df[["timestamp", "rating", "user_review", "ai_summary", "ai_action"]],
        use_container_width=True
    )
