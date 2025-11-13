from fastapi import APIRouter

router = APIRouter()

@router.get("/{customer_id}")
def recommend(customer_id: int):
    return {"customer_id": customer_id, "recommendations": [101, 102, 103]}
