from fastapi import FastAPI
import uvicorn
from app.api.v1.endpoints import lab_report
from app.api.v1.endpoints import meal_scaner

app = FastAPI()

# Router Include
app.include_router(lab_report.router)
app.include_router(meal_scaner.router, prefix="/api/v1", tags=["meal"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
