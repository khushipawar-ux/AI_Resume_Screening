"""
Embedding Utilities Module
"""
import numpy as np
from typing import List

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors
    
    Args:
        vec1: First vector
        vec2: Second vector
        
    Returns:
        Cosine similarity score
    """
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def batch_cosine_similarity(vec: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """
    Calculate cosine similarity between a vector and multiple vectors
    
    Args:
        vec: Query vector
        matrix: Matrix of vectors
        
    Returns:
        Array of similarity scores
    """
    # TODO: Implement batch cosine similarity
    return np.array([])
