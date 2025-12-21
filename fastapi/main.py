"""
Have to run this using uvicorn main:app --reload
here app is the object name for the fastapi app
"""
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def greet():
    return "Welcome to fastapi"

@app.get("/test")
def greet1():
    return "Welcome to fastapi-test"
