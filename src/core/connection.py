from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config import CONFIG

DB_URL = (
    f"postgresql+psycopg://{CONFIG.POSTGRES_USER}:"
    f"{CONFIG.POSTGRES_PASSWORD}@localhost/{CONFIG.POSTGRES_DB}"
)

engine = create_engine(
    DB_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()