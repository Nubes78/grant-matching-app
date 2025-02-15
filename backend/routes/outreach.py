
from fastapi import APIRouter

router = APIRouter(prefix="/outreach")

@router.get("/")
def get_outreach():
    return {"message": "Outreach tracking API"}
