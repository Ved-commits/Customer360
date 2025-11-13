from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_customers():
    return [{"id": 1, "name": "Aisha", "email": "aisha@example.com"}]
