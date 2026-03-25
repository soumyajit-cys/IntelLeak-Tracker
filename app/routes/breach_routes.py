from fastapi import APIRouter
from app.services.breach_service import get_breach_data

router = APIRouter(prefix="/breach-data")

@router.get("")
def get_data():
    return get_breach_data()