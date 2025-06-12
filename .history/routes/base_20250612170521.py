# main.py

from fastapi import FastAPI, API

app = FastAPI()

@app.get("/welcome")
def welcome():
    return{"Welcome to Smart Recruiter Assistant"}


