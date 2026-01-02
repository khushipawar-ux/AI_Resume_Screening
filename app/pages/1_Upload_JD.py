"""
Job Description Upload Page
"""
import streamlit as st

st.set_page_config(page_title="Upload Job Description", page_icon="📋")

st.title("📋 Upload Job Description")

jd_text = st.text_area("Paste Job Description", height=300)
uploaded_file = st.file_uploader("Or upload JD file", type=['txt', 'pdf', 'docx'])

if st.button("Process Job Description"):
    if jd_text or uploaded_file:
        st.success("Job Description processed successfully!")
    else:
        st.error("Please provide a job description")
