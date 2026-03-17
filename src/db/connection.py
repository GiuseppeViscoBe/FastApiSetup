from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.config import CONFIG
from sqlalchemy import text
from models.user import User


#Docker version
DB_URL = f"postgresql+psycopg://{CONFIG.POSTGRES_USER}:{CONFIG.POSTGRES_PASSWORD}@localhost/{CONFIG.POSTGRES_DB}"

engine = create_engine(
    url=DB_URL,
    echo=True
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


