"""
Tests for Parsing Module
"""
import pytest
from core.parsing.text_cleaner import TextCleaner

def test_text_cleaner():
    """Test text cleaning functionality"""
    cleaner = TextCleaner()
    text = "  This   is   a   test  "
    cleaned = cleaner.clean(text)
    assert cleaned == "This is a test"

def test_pdf_parser():
    """Test PDF parsing"""
    # TODO: Implement PDF parser tests
    pass

def test_docx_parser():
    """Test DOCX parsing"""
    # TODO: Implement DOCX parser tests
    pass
