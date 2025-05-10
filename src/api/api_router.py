from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/", tags=["Api"])
async def read_root():
    version = os.getenv("API_VERSION", "unknown")
    return {
        "status": "API is running",
        "version": version
    }
