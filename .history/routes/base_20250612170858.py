# main.py

from fastapi import FastAPI, APIRouter

base_router = APIRouter(
    prefix="api/v1",
    tags=[]
)

@base_router.get("/")
def welcome():
    return{"Welcomeee to Smart Recruiter Assistant"}



