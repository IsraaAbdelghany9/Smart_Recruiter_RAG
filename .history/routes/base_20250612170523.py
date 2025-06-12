# main.py

from fastapi import FastAPI, APIRouter

app = FastAPI()

@app.get("/welcome")
def welcome():
    return{"Welcome to Smart Recruiter Assistant"}


