# main.py

from fastapi import FastAPI, APIRouter
from do
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
def welcome():
    return{"Welcomeee to Smart Recruiter Assistant"}



