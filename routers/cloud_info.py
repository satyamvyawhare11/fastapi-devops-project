from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from services.cloud_service import read_s3_buckets

router = APIRouter()

class AwsBucketInfo(BaseModel):
    count: int
    names: List[str]

    class Config:
        schema_extra = {
            "example": {
                "count": 2,
                "names": [
                    "devops-logs",
                    "backup-storage"
                ]
            }
        }

@router.get(
    "/aws",
    summary="AWS S3 Info",
    description="Basic details about S3 buckets",
    response_model=AwsBucketInfo
)
def aws_details():
    return read_s3_buckets()
