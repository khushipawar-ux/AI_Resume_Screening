"""
Application Constants
"""

# Supported file formats
SUPPORTED_RESUME_FORMATS = ['.pdf', '.docx', '.doc']
SUPPORTED_JD_FORMATS = ['.txt', '.pdf', '.docx']

# Scoring thresholds
MIN_MATCH_SCORE = 0.7
EXCELLENT_MATCH_SCORE = 0.9
GOOD_MATCH_SCORE = 0.8

# Extraction patterns
EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
PHONE_PATTERN = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
URL_PATTERN = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'

# Education levels
EDUCATION_LEVELS = [
    'High School',
    'Associate Degree',
    'Bachelor\'s Degree',
    'Master\'s Degree',
    'PhD',
    'Professional Degree'
]

# Experience levels
EXPERIENCE_LEVELS = {
    'entry': (0, 2),
    'junior': (2, 5),
    'mid': (5, 8),
    'senior': (8, 12),
    'expert': (12, float('inf'))
}
