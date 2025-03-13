import streamlit as st
import openai
import os

# Set your OpenAI API key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

# User progress tracking (can be replaced with a database)
user_progress = {}

st.set_page_config(page_title="AI Learning Tutor", page_icon="📚", layout="centered")
st.title("📚 AI-Based Personalized Learning Tutor")

# Chatbot Functionality
st.header("💬 Ask the AI Tutor")
question = st.text_input("Enter your question:")
if st.button("Get Answer", key="ask_btn"):
    if question:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an AI tutor helping students."},
                      {"role": "user", "content": question}]
        )
        answer = response["choices"][0]["message"]["content"]
        st.success("✅ AI Tutor: " + answer)
    else:
        st.warning("⚠️ Please enter a question.")

# Quiz Generation
st.header("📝 Generate a Quiz")
topic = st.text_input("Enter a topic for the quiz:")
if st.button("Generate Quiz", key="quiz_btn"):
    if topic:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Generate a short quiz on " + topic}]
        )
        quiz = response["choices"][0]["message"]["content"]
        st.info("📖 Quiz: " + quiz)
    else:
        st.warning("⚠️ Please enter a topic.")

# Progress Tracking
st.header("📊 Track Learning Progress")
user_id = st.text_input("Enter User ID:")
score = st.number_input("Enter your score:", min_value=0, max_value=100)
if st.button("Update Progress", key="progress_btn"):
    if user_id:
        if user_id not in user_progress:
            user_progress[user_id] = []
        user_progress[user_id].append(score)
        st.success(f"✅ Progress Updated! Your scores: {user_progress[user_id]}")
    else:
        st.warning("⚠️ Please enter a User ID.")

st.markdown("---")
st.caption("🚀 Built with Streamlit & OpenAI GPT-4")
