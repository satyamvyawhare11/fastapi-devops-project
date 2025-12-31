import uvicorn
from app.api_app import app

if __name__ == "__main__":
    uvicorn.run(
        "app.api_app:app",
        port=8000,
        reload=True
    )
