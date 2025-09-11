from fastapi import FastAPI
from app.api.v1.endpoints import meal_scaner

app = FastAPI()

# Include API routes
app.include_router(meal_scaner.router, prefix="/api/v1", tags=["meal"])
