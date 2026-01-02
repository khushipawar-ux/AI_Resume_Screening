"""
Score Card Component
"""
import streamlit as st

def render_score_card(title: str, score: float, max_score: float = 100):
    """Render a score card component"""
    percentage = (score / max_score) * 100
    
    st.metric(
        label=title,
        value=f"{score:.1f}",
        delta=f"{percentage:.1f}%"
    )
