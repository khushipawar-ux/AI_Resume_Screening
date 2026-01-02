"""
Tests for Ranking Module
"""
import pytest
from core.matching.ranker import CandidateRanker

def test_candidate_ranking():
    """Test candidate ranking"""
    ranker = CandidateRanker()
    candidates = [
        {'name': 'Khushi', 'score': 85},
        {'name': 'Arihant', 'score': 92},
        {'name': 'Arshi', 'score': 78}
    ]
    ranked = ranker.rank_candidates(candidates)
    assert ranked[0]['name'] == 'Arihant'
    assert ranked[1]['name'] == 'Khushi'
    assert ranked[2]['name'] == 'Arshi'

def test_candidate_filtering():
    """Test candidate filtering"""
    ranker = CandidateRanker()
    candidates = [
        {'name': 'Khushi', 'score': 85},
        {'name': 'Arihant', 'score': 65},
        {'name': 'Arshi', 'score': 78}
    ]
    filtered = ranker.filter_candidates(candidates, min_score=0.7)
    assert len(filtered) == 3
