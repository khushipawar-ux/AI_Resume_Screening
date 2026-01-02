"""
Ranking Service Module
"""
from typing import List, Dict

class RankingService:
    """Business logic for candidate ranking"""
    
    def __init__(self, similarity_calculator, scoring_engine, ranker):
        self.similarity_calculator = similarity_calculator
        self.scoring_engine = scoring_engine
        self.ranker = ranker
    
    def rank_candidates(self, candidates: List[Dict], jd_data: Dict) -> List[Dict]:
        """
        Rank candidates against job description
        
        Args:
            candidates: List of candidate data
            jd_data: Job description data
            
        Returns:
            Ranked list of candidates with scores
        """
        scored_candidates = []
        
        for candidate in candidates:
            # Calculate similarity
            similarity_scores = self.similarity_calculator.calculate_multi_aspect_similarity(
                candidate, jd_data
            )
            
            # Calculate final score
            final_score = self.scoring_engine.calculate_score(similarity_scores)
            
            scored_candidates.append({
                **candidate,
                'score': final_score,
                'similarity_scores': similarity_scores
            })
        
        # Rank candidates
        return self.ranker.rank_candidates(scored_candidates)
