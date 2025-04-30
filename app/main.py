from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.config import get_settings
from core.logger import logger
from db.mongo import connect_to_mongoDB, close_mongoDB_connection, get_collection
import uvicorn

settings = get_settings()
print(settings.MONGO_URI)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    await connect_to_mongoDB()
    yield 
    # SHUTDOWN
    await close_mongoDB_connection

app = FastAPI(
    title=settings.APP_NAME, 
    lifespan=lifespan
    )

@app.get('/')
async def root_handler():
    return {"message": "Welcome"}


if __name__ == "__main__":
    uvicorn.run(app)
