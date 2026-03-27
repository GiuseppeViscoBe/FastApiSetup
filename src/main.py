from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.core.exception_handler import base_app_exception_handler, generic_exception_handler
from src.core.exceptions import BaseAppException
from src.core.connection import engine
from src.core.base import Base
from src.routes import user_router
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

app.add_exception_handler(BaseAppException, base_app_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(user_router.router)


@app.get("/")
def main():
    return {"message": "Hello World"}