# main.py

from fastapi import FastAPI
from routes import 
app = FastAPI()

@app.get("/welcome")
def welcome():
    return{"Welcome to Smart Recruiter Assistant"}


