import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()  # load .env file

DATABASE_URL = "postgresql://postgres:HYkggJBTfARDlfcdPNZnNwSQLhYwnsMx@autorack.proxy.rlwy.net:33605/railway"
print(DATABASE_URL)
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set!")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()