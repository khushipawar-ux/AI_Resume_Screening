"""
Job Description Pydantic Schemas
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JDBase(BaseModel):
    title: str
    description: str
    requirements: Optional[str] = None

class JDCreate(JDBase):
    pass

class JDResponse(JDBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
