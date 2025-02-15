
from fastapi import APIRouter

router = APIRouter(prefix="/businesses")

@router.get("/")
def get_businesses():
    return [{"id": 1, "name": "AI Corp", "industry": "Artificial Intelligence"}]
