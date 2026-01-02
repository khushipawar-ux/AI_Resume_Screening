"""
Job Description Service Module
"""
from typing import Dict

class JDService:
    """Business logic for job description processing"""
    
    def __init__(self, extractor, embedder):
        self.extractor = extractor
        self.embedder = embedder
    
    def process_jd(self, jd_text: str) -> Dict:
        """
        Process job description
        
        Args:
            jd_text: Job description text
            
        Returns:
            Processed JD data
        """
        # Extract requirements
        skills = self.extractor.extract_skills(jd_text)
        
        # Generate embeddings
        embedding = self.embedder.encode(jd_text)
        
        return {
            'text': jd_text,
            'required_skills': skills,
            'embedding': embedding
        }
