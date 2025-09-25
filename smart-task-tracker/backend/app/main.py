from fastapi import FastAPI
from app.routers import tasks

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Smart Task Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Task API is running"}

app.include_router(tasks.router)