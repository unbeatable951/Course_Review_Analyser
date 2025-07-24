# app.py

import streamlit as st
import pandas as pd
import joblib
import difflib

# Load data
df_courses = pd.read_csv(r"C:\Users\SACHIN\OneDrive\Desktop\Projects(ZENITH)\Coursera_courses.csv")
df_stats = pd.read_csv(r"C:\Users\SACHIN\OneDrive\Desktop\Projects(ZENITH)\coursea_data.csv")

# Load trained sentiment model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Extract slug from URL or text
def extract_slug(text):
    if "coursera.org" in text:
        parts = text.strip('/').split('/')
        if "learn" in parts:
            idx = parts.index("learn")
            if idx + 1 < len(parts):
                return parts[idx + 1].replace("-", " ")
    return text.lower()

# Predict sentiment
def predict_sentiment(text_series):
    X = vectorizer.transform(text_series)
    return model.predict(X)

# Analyze course
def analyze_course(user_input):
    slug = extract_slug(user_input)

    all_names = df_courses['name'].dropna().str.lower().tolist()
    all_ids = df_courses['course_id'].dropna().str.lower().tolist()
    candidates = all_names + all_ids

    best_match = difflib.get_close_matches(slug, candidates, n=1, cutoff=0.4)
    if not best_match:
        st.error("❌ No matching course found.")
        return

    match = best_match[0]
    matched = df_courses[df_courses['name'].str.lower() == match]
    if matched.empty:
        matched = df_courses[df_courses['course_id'].str.lower() == match]
    if matched.empty:
        st.error("❌ Still no exact match found.")
        return

    course = matched.iloc[0]
    course_name = course['name']
    course_provider = course['institution']

    st.subheader(f"✅ Course: {course_name}")
    st.markdown(f"**🏫 Offered by:** {course_provider}")

    # Match with stats
    stats_match = df_stats[df_stats['course_title'].str.lower().str.contains(course_name.lower(), na=False)]
    if not stats_match.empty:
        stats = stats_match.iloc[0]
        st.markdown(f"**⭐ Rating:** {stats['course_rating']} / 5")
        st.markdown(f"**📊 Difficulty:** {stats['course_difficulty']}")
        st.markdown(f"**🎓 Enrolled:** {stats['course_students_enrolled']} students")
    else:
        st.info("ℹ️ No rating/difficulty info found.")

    # Simulated reviews
    reviews = pd.Series([
        "Great and informative course!",
        "Too basic, not what I expected.",
        "Very detailed and engaging.",
        "The content felt outdated.",
        "Awesome projects and explanations!"
    ])

    sentiments = predict_sentiment(reviews)
    pos = sum(sentiments)
    neg = len(sentiments) - pos

    st.subheader("📝 Simulated Sentiment Review Summary:")
    st.markdown(f"👍 Positive Reviews: **{pos}**")
    st.markdown(f"👎 Negative Reviews: **{neg}**")

    st.markdown(f"📘 *'{course_name}' is a course offered by {course_provider} on Coursera.*")


# ---- Streamlit App Layout ---- #
st.set_page_config(page_title=" Course Review Analyzer", layout="centered")

st.title("🎓 Course Review Analyzer")
st.markdown("Get course details and simulated sentiment insights.")

user_input = st.text_input("Enter course name or Coursera URL:")

if st.button("Analyze"):
    if user_input.strip():
        analyze_course(user_input)
    else:
        st.warning("Please enter a course name or Coursera URL.")
