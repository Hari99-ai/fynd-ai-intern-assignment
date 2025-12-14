import json

def call_llm(prompt: str) -> str:
    """
    Replace with Gemini / OpenRouter API call.
    Must return plain text.
    """
    # MOCK RESPONSE (for testing without API)
    return "Thanks for your feedback! We appreciate you taking the time to share this."

def summarize_review(review: str) -> str:
    prompt = f"""
Summarize the following customer review in one short sentence.

Review:
{review}
"""
    return call_llm(prompt)

def recommend_action(review: str, rating: int) -> str:
    prompt = f"""
Based on the review and rating, suggest one recommended business action.

Rating: {rating}
Review:
{review}
"""
    return call_llm(prompt)

def user_response(review: str, rating: int) -> str:
    prompt = f"""
Write a polite and friendly response to a customer review.

Rating: {rating}
Review:
{review}
"""
    return call_llm(prompt)
