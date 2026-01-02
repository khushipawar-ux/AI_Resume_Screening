"""
Resume Parser Module
"""
from typing import Dict, Optional
from .pdf_parser import PDFParser
from .docx_parser import DOCXParser
from .text_cleaner import TextCleaner

class ResumeParser:
    """Main resume parser orchestrator"""
    
    def __init__(self):
        self.pdf_parser = PDFParser()
        self.docx_parser = DOCXParser()
        self.text_cleaner = TextCleaner()
    
    def parse_resume(self, file_path: str) -> Optional[Dict]:
        """
        Parse resume file and extract structured data
        
        Args:
            file_path: Path to resume file
            
        Returns:
            Parsed resume data
        """
        # TODO: Implement resume parsing logic
        pass
