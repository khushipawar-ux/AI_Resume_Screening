"""
Tests for Ranking Module
"""
import pytest
from core.matching.ranker import CandidateRanker

def test_candidate_ranking():
    """Test candidate ranking"""
    ranker = CandidateRanker()
    candidates = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 92},
        {'name': 'Charlie', 'score': 78}
    ]
    ranked = ranker.rank_candidates(candidates)
    assert ranked[0]['name'] == 'Bob'
    assert ranked[1]['name'] == 'Alice'
    assert ranked[2]['name'] == 'Charlie'

def test_candidate_filtering():
    """Test candidate filtering"""
    ranker = CandidateRanker()
    candidates = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 65},
        {'name': 'Charlie', 'score': 78}
    ]
    filtered = ranker.filter_candidates(candidates, min_score=0.7)
    assert len(filtered) == 2
