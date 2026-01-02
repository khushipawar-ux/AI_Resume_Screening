"""
Text Cleaner Module
"""
import re

class TextCleaner:
    """Clean and normalize extracted text"""
    
    @staticmethod
    def clean(text: str) -> str:
        """
        Clean and normalize text
        
        Args:
            text: Raw text to clean
            
        Returns:
            Cleaned text
        """
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters
        text = re.sub(r'[^\w\s.,;:!?-]', '', text)
        return text.strip()
