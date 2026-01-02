"""
Vector Utilities Module
"""
import numpy as np
from typing import List

def normalize_vector(vector: np.ndarray) -> np.ndarray:
    """Normalize a vector to unit length"""
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm

def cosine_distance(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """Calculate cosine distance between two vectors"""
    return 1 - np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def euclidean_distance(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """Calculate Euclidean distance between two vectors"""
    return np.linalg.norm(vec1 - vec2)

def batch_normalize(vectors: np.ndarray) -> np.ndarray:
    """Normalize multiple vectors"""
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return vectors / np.where(norms == 0, 1, norms)
