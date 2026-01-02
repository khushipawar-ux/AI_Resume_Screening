"""
Ranking Dashboard Page
"""
import streamlit as st

st.set_page_config(page_title="Ranking Dashboard", page_icon="📊", layout="wide")

st.title("📊 Candidate Ranking Dashboard")

# Placeholder for ranking table
st.dataframe({
    'Rank': [1, 2, 3],
    'Candidate': ['John Doe', 'Jane Smith', 'Bob Johnson'],
    'Match Score': [95, 88, 82],
    'Skills Match': ['90%', '85%', '80%']
})
