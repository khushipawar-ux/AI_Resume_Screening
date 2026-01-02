"""
Resume Service Module
"""
from typing import Dict, Optional

class ResumeService:
    """Business logic for resume processing"""
    
    def __init__(self, parser, extractor, embedder):
        self.parser = parser
        self.extractor = extractor
        self.embedder = embedder
    
    def process_resume(self, file_path: str) -> Optional[Dict]:
        """
        Process resume file end-to-end
        
        Args:
            file_path: Path to resume file
            
        Returns:
            Processed resume data
        """
        # Parse resume
        parsed_text = self.parser.parse_resume(file_path)
        
        # Extract information
        skills = self.extractor.extract_skills(parsed_text)
        experience = self.extractor.extract_experience(parsed_text)
        education = self.extractor.extract_education(parsed_text)
        
        # Generate embeddings
        embedding = self.embedder.encode(parsed_text)
        
        return {
            'text': parsed_text,
            'skills': skills,
            'experience': experience,
            'education': education,
            'embedding': embedding
        }
