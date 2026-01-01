# def create_app():
#     app = FastAPI()
#     return app
from fastapi import Depends, FastAPI
from fastapi.routing import HTTPException
from sqlalchemy.orm import Session
from models import Product
from database import Session, engine
import database_models

database_models.Base.metadata.create_all(bind=engine) # This is the command to create the tables in the database.

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

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = Session()

    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
    db.commit()


init_db()

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.post("/product")
def create_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(product: Product):
    index: int = next((i for i, p in enumerate(products) if product.id == p.id), -1)
    if index == -1:
        raise HTTPException(status_code=404, detail="Product not found")
    products[index] = product
    return products

@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    index: int = next((i for i, p in enumerate(products) if product_id == p.id), -1)
    if index == -1:
        raise HTTPException(status_code=404, detail="Product not found")
    products.pop(index)
    return products