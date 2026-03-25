from fastapi import APIRouter
from app.services.alert_service import get_alerts

router = APIRouter(prefix="/alerts")

@router.get("")
def alerts():
    return get_alerts()