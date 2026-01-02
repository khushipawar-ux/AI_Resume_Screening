"""
Resume Pydantic Schemas
"""
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class ResumeBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class ResumeCreate(ResumeBase):
    resume_path: str
    jd_id: int

class ResumeResponse(ResumeBase):
    id: int
    resume_path: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class SkillSchema(BaseModel):
    name: str
    proficiency: Optional[str] = None

class ExperienceSchema(BaseModel):
    company: str
    position: str
    duration: str
    description: Optional[str] = None
