"""
CRUD Operations Module
"""
from sqlalchemy.orm import Session
from typing import List, Optional
from .models import JobDescription, Candidate, MatchScore

class CRUDOperations:
    """Database CRUD operations"""
    
    @staticmethod
    def create_job_description(db: Session, title: str, description: str, requirements: str = None):
        """Create new job description"""
        jd = JobDescription(title=title, description=description, requirements=requirements)
        db.add(jd)
        db.commit()
        db.refresh(jd)
        return jd
    
    @staticmethod
    def create_candidate(db: Session, name: str, email: str, resume_path: str, jd_id: int):
        """Create new candidate"""
        candidate = Candidate(name=name, email=email, resume_path=resume_path, jd_id=jd_id)
        db.add(candidate)
        db.commit()
        db.refresh(candidate)
        return candidate
    
    @staticmethod
    def create_match_score(db: Session, candidate_id: int, overall_score: float, 
                          skill_score: float = None, experience_score: float = None,
                          education_score: float = None, explanation: str = None):
        """Create match score"""
        score = MatchScore(
            candidate_id=candidate_id,
            overall_score=overall_score,
            skill_score=skill_score,
            experience_score=experience_score,
            education_score=education_score,
            explanation=explanation
        )
        db.add(score)
        db.commit()
        db.refresh(score)
        return score
    
    @staticmethod
    def get_candidates_by_jd(db: Session, jd_id: int) -> List[Candidate]:
        """Get all candidates for a job description"""
        return db.query(Candidate).filter(Candidate.jd_id == jd_id).all()
    
    @staticmethod
    def get_candidate_with_score(db: Session, candidate_id: int) -> Optional[Candidate]:
        """Get candidate with match scores"""
        return db.query(Candidate).filter(Candidate.id == candidate_id).first()
