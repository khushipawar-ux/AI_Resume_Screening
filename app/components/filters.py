"""
Filters Component
"""
import streamlit as st

def render_filters():
    """Render filter controls"""
    st.sidebar.header("Filters")
    
    min_score = st.sidebar.slider("Minimum Match Score", 0, 100, 70)
    experience_range = st.sidebar.slider("Years of Experience", 0, 20, (0, 10))
    
    return {
        'min_score': min_score,
        'experience_range': experience_range
    }
