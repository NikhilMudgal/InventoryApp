from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:1234@localhost:5432/products"
engine = create_engine(db_url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)