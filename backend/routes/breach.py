from fastapi import APIRouter
from database import breach_collection

router = APIRouter()

@router.get("/breach-data")
def get_data():
    return list(breach_collection.find({}, {"_id": 0}))