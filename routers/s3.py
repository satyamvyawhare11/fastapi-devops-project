from fastapi import APIRouter, UploadFile, File
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=os.getenv("AWS_REGION")
)

bucket_name = os.getenv("AWS_BUCKET")

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    s3.upload_fileobj(file.file, bucket_name, file.filename)
    return {"message": "File uploaded"}

@router.get("/files")
def list_files():
    files = []
    response = s3.list_objects_v2(Bucket=bucket_name)

    if "Contents" in response:
        for item in response["Contents"]:
            files.append(item["Key"])

    return {"files": files}
