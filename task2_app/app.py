import streamlit as st
import pandas as pd
import os
from datetime import datetime
from utils.llm import user_response, summarize_review, recommend_action

# ---------------- PATH SETUP ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_PATH = os.path.join(DATA_DIR, "feedback.csv")

os.makedirs(DATA_DIR, exist_ok=True)

COLUMNS = [
    "timestamp",
    "rating",
    "user_review",
    "ai_response",
    "ai_summary",
    "ai_action"
]

def load_data():
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame(columns=COLUMNS)
    try:
        return pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        return pd.DataFrame(columns=COLUMNS)

def save_data(df):
    df.to_csv(DATA_PATH, index=False)

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="User Feedback", layout="centered")
st.title("📝 Submit Your Feedback")

rating = st.radio("Select rating", [1, 2, 3, 4, 5], horizontal=True)
review = st.text_area("Write your review")

if st.button("Submit"):
    if review.strip() == "":
        st.warning("Please write a review.")
    else:
        ai_reply = user_response(review, rating)
        summary = summarize_review(review)
        action = recommend_action(review, rating)

        new_row = {
            "timestamp": datetime.now(),
            "rating": rating,
            "user_review": review,
            "ai_response": ai_reply,
            "ai_summary": summary,
            "ai_action": action
        }

        df = load_data()
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        save_data(df)

        st.success("Feedback submitted successfully!")
        st.subheader("AI Response")
        st.write(ai_reply)
