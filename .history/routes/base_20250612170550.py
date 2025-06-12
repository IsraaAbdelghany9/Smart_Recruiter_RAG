# main.py

from fastapi import FastAPI, APIRouter

app = FastAPI()


base_router = APIRouter()

@base_router.get("/welcome")
def welcome():
    return{"Welcome to Smart Recruiter Assistant"}

