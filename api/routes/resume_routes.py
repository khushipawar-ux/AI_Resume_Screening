"""
Resume API Routes
"""
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from typing import List
from db.database import get_db
from db.crud import CRUDOperations
import os
from config.settings import RESUMES_DIR

router = APIRouter(prefix="/resumes", tags=["resumes"])

@router.post("/upload")
async def upload_resume(jd_id: int, file: UploadFile = File(...), db=Depends(get_db)):
    """Upload a resume file and create candidate entry"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(RESUMES_DIR, exist_ok=True)
        
        # Save file
        file_path = os.path.join(RESUMES_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Create candidate entry in DB
        candidate = CRUDOperations.create_candidate(
            db, 
            name=file.filename, # Placeholder for name
            email="placeholder@example.com", 
            resume_path=file_path, 
            jd_id=jd_id
        )
        
        return {"message": "Resume uploaded and candidate created", "candidate": candidate}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{resume_id}")
async def get_resume(resume_id: int, db=Depends(get_db)):
    """Get resume by ID"""
    try:
        candidate = CRUDOperations.get_candidate_with_score(db, resume_id)
        if not candidate:
            raise HTTPException(status_code=404, detail="Candidate not found")
        return candidate
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
async def list_resumes(jd_id: int, db=Depends(get_db)):
    """List all resumes for a job description"""
    try:
        return CRUDOperations.get_candidates_by_jd(db, jd_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

