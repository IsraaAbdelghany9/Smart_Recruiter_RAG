# main.py

from fastapi import FastAPI

app = FastAPI()

@app
def welcome():
    return{"Welcome to Smart Recruiter Assistant"}

