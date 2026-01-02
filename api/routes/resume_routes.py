"""
Resume API Routes
"""
from fastapi import APIRouter, UploadFile, File
from typing import List

router = APIRouter(prefix="/resumes", tags=["resumes"])

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """Upload a resume file"""
    return {"filename": file.filename, "status": "uploaded"}

@router.get("/{resume_id}")
async def get_resume(resume_id: int):
    """Get resume by ID"""
    return {"resume_id": resume_id}

@router.get("/")
async def list_resumes():
    """List all resumes"""
    return {"resumes": []}
