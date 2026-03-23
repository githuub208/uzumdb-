from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv("app/.env")
DB_NAME=os.getenv("DB_NAME")
DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")

engine = create_engine(
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}"
)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
