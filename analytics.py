from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def analytics():
    return {"total_customers": 120, "total_events": 540}
