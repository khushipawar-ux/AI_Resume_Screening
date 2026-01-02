"""
Tests for Embeddings Module
"""
import pytest
import numpy as np
from core.embeddings.embedding_utils import cosine_similarity

def test_cosine_similarity():
    """Test cosine similarity calculation"""
    vec1 = np.array([1, 0, 0])
    vec2 = np.array([1, 0, 0])
    similarity = cosine_similarity(vec1, vec2)
    assert similarity == 1.0
    
    vec3 = np.array([0, 1, 0])
    similarity2 = cosine_similarity(vec1, vec3)
    assert similarity2 == 0.0
