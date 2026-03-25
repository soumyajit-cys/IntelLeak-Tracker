from fastapi import APIRouter
from app.services.keyword_service import add_keyword, get_keywords, delete_keyword

router = APIRouter(prefix="/keywords")

@router.post("")
def create_keyword(data: dict):
    add_keyword(data["value"])
    return {"message": "Keyword added"}

@router.get("")
def list_keywords():
    return get_keywords()

@router.delete("/{value}")
def remove_keyword(value: str):
    delete_keyword(value)
    return {"message": "Keyword deleted"}