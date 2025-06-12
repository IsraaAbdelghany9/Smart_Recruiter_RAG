# main.py

from fastapi import FastAPI

app = FastAPI()

@app.we
def welcome():
    return{"Welcome to Smart Recruiter Assistant"}

