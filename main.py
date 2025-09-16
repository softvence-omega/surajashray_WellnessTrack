from fastapi import FastAPI
import uvicorn

from app.api.v1.endpoints import lab_report

app = FastAPI()


app.include_router(lab_report.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)


### Add model locally