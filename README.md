# AI Resume Screening System

An intelligent resume screening system powered by AI that matches candidates with job descriptions using NLP, embeddings, and LLM-based explanations.

## Features

- 📄 **Resume Parsing**: Extract information from PDF and DOCX resumes
- 🎯 **Smart Matching**: AI-powered matching between resumes and job descriptions
- 📊 **Ranking Dashboard**: Visual ranking of candidates with detailed scores
- 🤖 **Gemini AI Explanations**: Get Google Gemini-powered explanations for match scores
- 📈 **Skill Gap Analysis**: Identify missing skills and upskilling opportunities
- 🔍 **Multi-aspect Scoring**: Evaluate candidates on skills, experience, and education
- 🗄️ **PostgreSQL Database**: Robust and scalable data storage

## Project Structure

```
ai-resume-screening/
├── app/                    # Streamlit UI
├── core/                   # Core AI logic
├── db/                     # Database layer
├── services/               # Business logic
├── api/                    # FastAPI backend
├── utils/                  # Utilities
├── tests/                  # Tests
├── config/                 # Configuration
├── scripts/                # Helper scripts
└── data/                   # Data storage
```

## Installation

1. **Prerequisites**:
   - Python 3.8+
   - PostgreSQL 12+ installed and running
   - Google Gemini API key

2. **Clone the repository**

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up PostgreSQL database**:
```bash
# Create database
createdb resume_screening

# Or using psql
psql -U postgres
CREATE DATABASE resume_screening;
```

5. **Set up environment variables in `.env`**:
```
DATABASE_URL=postgresql://username:password@localhost:5432/resume_screening
GEMINI_API_KEY=your_gemini_api_key_here
```

6. **Initialize the database**:
```bash
python scripts/migrate_db.py
```

## Usage

### Run Streamlit App
```bash
streamlit run app/streamlit_app.py
```

### Run FastAPI Backend
```bash
uvicorn api.main:app --reload
```

## Development

### Run Tests
```bash
pytest tests/
```

### Code Formatting
```bash
black .
```

## License

MIT License
