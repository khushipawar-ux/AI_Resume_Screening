"""
Tests for Extraction Module
"""
import pytest
from core.extraction.skill_extractor import SkillExtractor

def test_skill_extraction():
    """Test skill extraction"""
    extractor = SkillExtractor()
    text = "I have experience with Python, Java, and Machine Learning"
    skills = extractor.extract_skills(text)
    # TODO: Add assertions when implementation is complete
    assert isinstance(skills, list)
