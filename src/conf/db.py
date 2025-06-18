import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_USER = os.environ.get("DB_APP_USER", "app_user")
DB_PASSWORD = os.environ.get(
    "DB_APP_PASSWORD", "your_app_accessing_db_limited_user_secret_password"
)
DB_HOST = os.environ.get("DB_HOST", "hw02db")
DB_NAME = os.environ.get("DB_NAME", "mydb")
DB_PORT = os.environ.get("DB_PORT", "5432")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, max_overflow=5)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
