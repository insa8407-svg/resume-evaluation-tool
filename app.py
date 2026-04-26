import streamlit as st
import pandas as pd
import re

# -------------------------------
# Title
# -------------------------------
st.set_page_config(page_title="Resume Score Analyzer", layout="wide")

st.title("📄 Resume Score Analyzer")
st.write("Analyze your resume and get a score based on keyword matching.")

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader("Upload your Resume (TXT file only)", type=["txt"])

job_description = st.text_area("Paste Job Description (Optional)")

# -------------------------------
# Predefined Keywords (can improve later)
# -------------------------------
default_keywords = [
    "python", "machine learning", "data analysis", "sql",
    "communication", "teamwork", "project", "leadership",
    "deep learning", "nlp", "statistics"
]

# -------------------------------
# Function to clean text
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

# -------------------------------
# Analyze Resume
# -------------------------------
if uploaded_file is not None:
    resume_text = uploaded_file.read().decode("utf-8")
    resume_text = clean_text(resume_text)

    if job_description:
        job_description = clean_text(job_description)
        keywords = job_description.split()
    else:
        keywords = default_keywords

    # Remove duplicates
    keywords = list(set(keywords))

    matched_keywords = []
    missing_keywords = []

    for word in keywords:
        if word in resume_text:
            matched_keywords.append(word)
        else:
            missing_keywords.append(word)

    # Score Calculation
    score = int((len(matched_keywords) / len(keywords)) * 100)

    # -------------------------------
    # Output UI
    # -------------------------------
    st.subheader("📊 Resume Score")
    st.progress(score)
    st.success(f"Your Resume Score: {score}%")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matched Keywords")
        st.write(matched_keywords)

    with col2:
        st.subheader("❌ Missing Keywords")
        st.write(missing_keywords)

    # Suggestions
    st.subheader("💡 Suggestions")
    if score > 75:
        st.success("Great! Your resume matches well.")
    elif score > 50:
        st.warning("Good, but you can improve by adding missing keywords.")
    else:
        st.error("Your resume needs improvement. Add more relevant skills.")

else:
    st.info("Upload a resume file to get started.")
