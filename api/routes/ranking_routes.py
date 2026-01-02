"""
Ranking API Routes
"""
from fastapi import APIRouter

router = APIRouter(prefix="/ranking", tags=["ranking"])

@router.get("/{jd_id}")
async def get_rankings(jd_id: int):
    """Get candidate rankings for a job description"""
    return {"jd_id": jd_id, "rankings": []}

@router.post("/calculate/{jd_id}")
async def calculate_rankings(jd_id: int):
    """Calculate rankings for candidates"""
    return {"message": "Rankings calculated", "jd_id": jd_id}
