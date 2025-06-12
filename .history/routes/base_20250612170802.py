# main.py

from fastapi import FastAPI, APIRouter

base_router = APIRouter(

    
)

@base_router.get("/welcome")
def welcome():
    return{"Welcomeee to Smart Recruiter Assistant"}



