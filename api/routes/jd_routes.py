"""
Job Description API Routes
"""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from db.database import get_db
from db.crud import CRUDOperations

router = APIRouter(prefix="/job-descriptions", tags=["job-descriptions"])

class JDCreate(BaseModel):
    title: str
    description: str
    requirements: str = None

@router.post("/", response_model=dict)
async def create_jd(jd: JDCreate, db=Depends(get_db)):
    """Create a new job description"""
    try:
        new_jd = CRUDOperations.create_job_description(
            db, jd.title, jd.description, jd.requirements
        )
        return {"message": "Job description created", "data": new_jd}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{jd_id}")
async def get_jd(jd_id: int, db=Depends(get_db)):
    """Get job description by ID"""
    try:
        jd = CRUDOperations.get_job_description(db, jd_id)
        if not jd:
            raise HTTPException(status_code=404, detail="Job description not found")
        return jd
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
async def get_all_jds(db=Depends(get_db)):
    """Get all job descriptions"""
    try:
        return CRUDOperations.get_all_job_descriptions(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


