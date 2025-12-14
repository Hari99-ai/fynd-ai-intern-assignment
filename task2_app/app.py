import streamlit as st
import pandas as pd
from datetime import datetime
from utils.llm import user_response, summarize_review, recommend_action

DATA_PATH = "data/feedback.csv"

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

        df = pd.read_csv(DATA_PATH)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(DATA_PATH, index=False)

        st.success("Feedback submitted!")
        st.subheader("AI Response")
        st.write(ai_reply)
