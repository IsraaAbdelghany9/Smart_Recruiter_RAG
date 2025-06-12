# main.py

from fastapi import FastAPI, APIRouter

base_router = APIRouter(
    prefix="p"
)

@base_router.get("/welcome")
def welcome():
    return{"Welcomeee to Smart Recruiter Assistant"}



