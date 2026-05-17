from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(
    title="Inprep AI API",
    root_path="inprep_ai_api",
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "FastAPI Running perfectly!"}
