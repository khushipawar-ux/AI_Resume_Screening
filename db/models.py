"""
Database Models
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class JobDescription(Base):
    __tablename__ = 'job_descriptions'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    requirements = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    candidates = relationship("Candidate", back_populates="job_description")

class Candidate(Base):
    __tablename__ = 'candidates'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))
    resume_path = Column(String(500))
    parsed_data = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign keys
    jd_id = Column(Integer, ForeignKey('job_descriptions.id'))
    
    # Relationships
    job_description = relationship("JobDescription", back_populates="candidates")
    scores = relationship("MatchScore", back_populates="candidate")

class MatchScore(Base):
    __tablename__ = 'match_scores'
    
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidates.id'))
    overall_score = Column(Float)
    skill_score = Column(Float)
    experience_score = Column(Float)
    education_score = Column(Float)
    explanation = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    candidate = relationship("Candidate", back_populates="scores")
