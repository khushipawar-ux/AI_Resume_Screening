"""
Skill Chart Component
"""
import streamlit as st

def render_skill_chart(skills: dict):
    """Render a skill chart component"""
    st.bar_chart(skills)
