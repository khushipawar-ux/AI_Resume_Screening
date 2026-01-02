# Environment Variables Template

## Database Configuration
```bash
# PostgreSQL Database URL
DATABASE_URL=postgresql://username:password@localhost:5432/resume_screening

# Example with specific credentials:
# DATABASE_URL=postgresql://postgres:mypassword@localhost:5432/resume_screening
```

## LLM Configuration
```bash
# Google Gemini API
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-pro

# Alternative: Ollama (local LLM)
# LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2
```

## Embedding Configuration
```bash
EMBEDDING_MODEL=all-MiniLM-L6-v2
```

## Scoring Weights
```bash
WEIGHT_SKILLS=0.4
WEIGHT_EXPERIENCE=0.3
WEIGHT_EDUCATION=0.2
WEIGHT_OVERALL=0.1
```

## Application Settings
```bash
DEBUG=False
LOG_LEVEL=INFO
```

## Getting Your API Keys

### Google Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and paste it in your `.env` file

### PostgreSQL Setup
1. Install PostgreSQL from [postgresql.org](https://www.postgresql.org/download/)
2. Create a database: `createdb resume_screening`
3. Update the `DATABASE_URL` with your credentials
