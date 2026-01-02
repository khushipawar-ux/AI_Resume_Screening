"""
Text Utilities Module
"""
import re
from typing import List

def normalize_whitespace(text: str) -> str:
    """Normalize whitespace in text"""
    return re.sub(r'\s+', ' ', text).strip()

def remove_special_characters(text: str) -> str:
    """Remove special characters from text"""
    return re.sub(r'[^\w\s.,;:!?-]', '', text)

def extract_emails(text: str) -> List[str]:
    """Extract email addresses from text"""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

def extract_phone_numbers(text: str) -> List[str]:
    """Extract phone numbers from text"""
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(phone_pattern, text)

def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to maximum length"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."
