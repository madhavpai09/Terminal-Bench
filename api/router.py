from fastapi import APIRouter
import sys
sys.path.append("../")



router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}

