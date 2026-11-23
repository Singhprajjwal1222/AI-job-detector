
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import find_jobs

# Create FastAPI application
app = FastAPI(
    title="AI Job Matcher API",
    description="AI-powered job recommendation system",
    version="1.0"
)

# Allow React frontend to connect with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Request model
class JobRequest(BaseModel):
    request: str

# Home route
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Job Matcher API",
        "status": "running"
    }

# Job search API
@app.post("/find-jobs")
def find_jobs_api(data: JobRequest):
    result = find_jobs(data.request)
    return result
