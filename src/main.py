from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.db.connection import engine
from src.db.base import Base
from src.routes import users
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown (optional)
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)

app.include_router(users.router)


@app.get("/")
def main():
    return {"message": "Hello World"}