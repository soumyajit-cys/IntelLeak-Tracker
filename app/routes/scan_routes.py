from fastapi import APIRouter
from app.services.scan_service import run_scan

router = APIRouter()

@router.post("/run-scan")
def manual_scan():
    return run_scan()