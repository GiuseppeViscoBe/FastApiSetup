from fastapi import FastAPI
import httpx
from sqlalchemy import engine
from db.base import Base
from routes import users_router
import urllib3
from src.config import CONFIG

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(users_router)

@app.get("/")
def main():
    return {"message": "Hello World"}
    
