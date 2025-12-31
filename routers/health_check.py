from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class HealthStatus(BaseModel):
    state: str
    time_checked: str

    class Config:
        schema_extra = {
            "example": {
                "state": "healthy",
                "time_checked": "2025-01-01 11:00:00"
            }
        }

@router.get(
    "/health",
    summary="Health Status",
    description="Returns current health of the service",
    response_model=HealthStatus
)
def check_health():
    return {
        "state": "healthy",
        "time_checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
