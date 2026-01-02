"""
Ranking API Routes
"""
from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from db.crud import CRUDOperations

router = APIRouter(prefix="/ranking", tags=["ranking"])

@router.get("/{jd_id}")
async def get_rankings(jd_id: int, db=Depends(get_db)):
    """Get candidate rankings for a job description"""
    try:
        candidates_with_scores = CRUDOperations.get_candidates_by_jd(db, jd_id)
        # In a real app, we might want to sort these by score
        return {"jd_id": jd_id, "rankings": candidates_with_scores}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/calculate/{jd_id}")
async def calculate_rankings(jd_id: int, db=Depends(get_db)):
    """Calculate rankings for candidates"""
    # This would involve calling the ranking service
    return {"message": "Rankings calculation triggered", "jd_id": jd_id}

