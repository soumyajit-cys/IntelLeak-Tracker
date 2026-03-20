from fastapi import APIRouter
from database import alert_collection

router = APIRouter()

@router.get("/alerts")
def get_alerts():
    return list(alert_collection.find({}, {"_id": 0}))