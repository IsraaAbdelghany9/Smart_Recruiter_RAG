# routes/base.py

from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
def welcome():
    app_name= 
    return{"Welcomeee to Smart Recruiter Assistant"}



