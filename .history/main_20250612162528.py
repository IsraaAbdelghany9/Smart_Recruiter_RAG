# main.py

from fastapi import FastAPI

app = FastAPI()

def welcome():
    return{"Welcome to Smart "}