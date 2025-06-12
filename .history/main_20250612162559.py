# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("Welcome")
def welcome():
    return{"Welcome to Smart Recruiter Assistant"}

