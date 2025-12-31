from fastapi import FastAPI
from pydantic import BaseModel
from routers import health_check, system_info, cloud_info

class HomeResponse(BaseModel):
    message: str

    class Config:
        schema_extra = {
            "example": {
                "message": "API is up and running"
            }
        }

app = FastAPI(
    title="DevOps Practice API",
    description="Simple API built to understand how DevOps tools expose Python logic",
    version="1.0"
)

@app.get(
    "/",
    summary="Home Endpoint",
    description="Used to verify that the API is working",
    response_model=HomeResponse
)
def home_page():
    return {"message": "API is up and running"}

# connect routes
app.include_router(health_check.router)
app.include_router(system_info.router)
app.include_router(cloud_info.router, prefix="/cloud")
