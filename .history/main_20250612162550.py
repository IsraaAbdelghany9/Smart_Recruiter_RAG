# main.py

from fastapi import FastAPI

app = FastAPI()

@app.wel
def welcome():
    return{"Welcome to Smart Recruiter Assistant"}

