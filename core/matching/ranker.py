"""
Ranker Module
"""
from typing import List, Dict

class CandidateRanker:
    """Rank candidates based on match scores"""
    
    def rank_candidates(self, candidates: List[Dict]) -> List[Dict]:
        """
        Rank candidates by match score
        
        Args:
            candidates: List of candidate dictionaries with scores
            
        Returns:
            Sorted list of candidates
        """
        return sorted(candidates, key=lambda x: x.get('score', 0), reverse=True)
    
    def filter_candidates(self, candidates: List[Dict], min_score: float = 0.7) -> List[Dict]:
        """
        Filter candidates by minimum score
        
        Args:
            candidates: List of candidates
            min_score: Minimum score threshold
            
        Returns:
            Filtered list of candidates
        """
        return [c for c in candidates if c.get('score', 0) >= min_score]
