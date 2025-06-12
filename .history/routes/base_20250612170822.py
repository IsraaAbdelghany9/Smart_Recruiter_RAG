# main.py

from fastapi import FastAPI, APIRouter

base_router = APIRouter(
    prefix=
)

@base_router.get("/welcome")
def welcome():
    return{"Welcomeee to Smart Recruiter Assistant"}



