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
    Product(id=1, name="Mobile", description="Affordable Mobile", price=100, quantity=40),
    Product(id=2, name="Laptop", description="Gaming Laptop", price=300, quantity=15),
    Product(id=3, name="Speakers", description="Wireless Speakers", price=200, quantity=30),
    Product(id=4, name="Headphones", description="Wireless Headphones", price=150, quantity=20),
    Product(id=5, name="Tablet", description="Tablet", price=250, quantity=10),
    Product(id=6, name="Smartwatch", description="Smartwatch", price=300, quantity=15),
    Product(id=7, name="Keyboard", description="Wireless Keyboard", price=100, quantity=20),
    Product(id=8, name="Mouse", description="Wireless Mouse", price=50, quantity=30),
    Product(id=9, name="Monitor", description="Monitor", price=400, quantity=10),
    Product(id=10, name="Printer", description="Printer", price=350, quantity=15)
]

@app.get("/products")
def get_products():
    return products