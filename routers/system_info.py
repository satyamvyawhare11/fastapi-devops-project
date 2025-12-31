from fastapi import APIRouter
from pydantic import BaseModel
from services.system_service import fetch_system_stats

router = APIRouter()

class SystemStats(BaseModel):
    cpu: float
    ram: float
    disk: float

    class Config:
        schema_extra = {
            "example": {
                "cpu": 18.2,
                "ram": 61.7,
                "disk": 44.9
            }
        }

@router.get(
    "/system",
    summary="System Information",
    description="Shows CPU, RAM and disk usage",
    response_model=SystemStats
)
def system_data():
    return fetch_system_stats()
