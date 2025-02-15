
from fastapi import APIRouter

router = APIRouter(prefix="/grants")

@router.get("/")
def get_grants():
    return [{"id": 1, "title": "AI Research Grant", "technology": "Artificial Intelligence"}]
