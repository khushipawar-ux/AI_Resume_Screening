"""
Scoring Module
"""
from typing import Dict

class ScoringEngine:
    """Calculate final match scores"""
    
    def __init__(self, weights: Dict[str, float] = None):
        self.weights = weights or {
            'skills': 0.4,
            'experience': 0.3,
            'education': 0.2,
            'overall': 0.1
        }
    
    def calculate_score(self, similarity_scores: Dict[str, float]) -> float:
        """
        Calculate weighted final score
        
        Args:
            similarity_scores: Dictionary of aspect-wise scores
            
        Returns:
            Final weighted score
        """
        total_score = 0.0
        for aspect, score in similarity_scores.items():
            weight = self.weights.get(aspect, 0.0)
            total_score += score * weight
        return total_score
