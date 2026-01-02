"""
Main Streamlit Dashboard for AI Resume Screening
"""
import streamlit as st

def main():
    st.set_page_config(
        page_title="AI Resume Screening",
        page_icon="📄",
        layout="wide"
    )
    
    st.title("🎯 AI Resume Screening System")
    st.markdown("### Welcome to the AI-powered Resume Screening Platform")
    
    st.info("Use the sidebar to navigate between different pages.")
    
    # Overview metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Resumes", "0")
    with col2:
        st.metric("Job Descriptions", "0")
    with col3:
        st.metric("Matches Found", "0")

if __name__ == "__main__":
    main()
