from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:1234@localhost:5432/products"  # This is the database url for the project. The database name is "products".
engine = create_engine(db_url) # This is the engine for the database.
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine) # This is the session for the database.

# def get_db():
#     db = Session()
#     try:
#         yield db
#     finally:
#         db.close()

# def close_db(db):
#     db.close()
