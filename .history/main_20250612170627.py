# main.py

from fastapi import FastAPI
from routes import base
app = FastAPI()

@app.get("/welcome")
def welcome():
    return{"Welcome to Smart Recruiter Assistant"}


