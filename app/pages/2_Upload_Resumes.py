"""
Resume Upload Page
"""
import streamlit as st

st.set_page_config(page_title="Upload Resumes", page_icon="📄")

st.title("📄 Upload Resumes")

uploaded_files = st.file_uploader(
    "Upload Resume Files",
    type=['pdf', 'docx'],
    accept_multiple_files=True
)

if uploaded_files:
    st.write(f"Uploaded {len(uploaded_files)} resume(s)")
    
    if st.button("Process Resumes"):
        st.success(f"Processing {len(uploaded_files)} resumes...")
