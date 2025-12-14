import streamlit as st
import pandas as pd
import os

# ---------- PATH SETUP (CRITICAL) ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_PATH = os.path.join(DATA_DIR, "feedback.csv")

os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(DATA_PATH):
    pd.DataFrame(columns=[
        "timestamp",
        "rating",
        "user_review",
        "ai_response",
        "ai_summary",
        "ai_action"
    ]).to_csv(DATA_PATH, index=False)

df = pd.read_csv(DATA_PATH)

# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("📊 Admin Feedback Dashboard")

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
