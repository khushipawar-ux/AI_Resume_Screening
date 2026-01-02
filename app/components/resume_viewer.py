"""
Resume Viewer Component
"""
import streamlit as st

def render_resume_viewer(resume_path: str):
    """Render a resume viewer component"""
    st.info(f"Resume viewer for: {resume_path}")
    # TODO: Implement PDF/DOCX viewer
