"""
Job Description API Routes
"""
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/job-descriptions", tags=["job-descriptions"])

class JDCreate(BaseModel):
    title: str
    description: str
    requirements: str = None

@router.post("/")
async def create_jd(jd: JDCreate):
    """Create a new job description"""
    return {"message": "Job description created", "data": jd}

@router.get("/{jd_id}")
async def get_jd(jd_id: int):
    """Get job description by ID"""
    return {"jd_id": jd_id}
