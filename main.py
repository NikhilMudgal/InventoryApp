# def create_app():
#     app = FastAPI()
#     return app
from fastapi import FastAPI

app = FastAPI()

def greet():
    return "Welcome"