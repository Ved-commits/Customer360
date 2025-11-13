from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_events():
    return [{"id": 1, "customer_id": 1, "event_type": "view"}]
