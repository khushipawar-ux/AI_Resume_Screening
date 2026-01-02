"""
Application Settings
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RESUMES_DIR = DATA_DIR / "resumes"
JD_DIR = DATA_DIR / "job_descriptions"
PARSED_RESUMES_DIR = DATA_DIR / "parsed_resumes"
EMBEDDINGS_DIR = DATA_DIR / "embeddings"

# Database (PostgreSQL)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/resume_screening")

# LLM Settings
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")  # gemini or ollama
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-pro")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2")

# Embedding Settings
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

# Scoring Weights
SCORING_WEIGHTS = {
    'skills': float(os.getenv("WEIGHT_SKILLS", "0.4")),
    'experience': float(os.getenv("WEIGHT_EXPERIENCE", "0.3")),
    'education': float(os.getenv("WEIGHT_EDUCATION", "0.2")),
    'overall': float(os.getenv("WEIGHT_OVERALL", "0.1"))
}

# Application Settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
