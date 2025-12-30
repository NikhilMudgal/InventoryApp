# def create_app():
#     app = FastAPI()
#     return app
from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome"



products = [
    Product(1, "Mobile", "Affordable Mobile", 100, 40),
    Product(2, "Laptop", "Gaming Laptop", 300, 15),
    Product(3, "Speakers", "Wireless Speakers", 200, 30)
]

@app.get("/products")
def get_products():
    return products