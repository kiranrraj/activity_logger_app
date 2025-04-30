from motor.motor_asyncio import AsyncIOMotorClient
from core.config import get_settings
from core.logger import logger

settings = get_settings()
client: AsyncIOMotorClient = None
db = None

async def connect_to_mongoDB():
    global client, db

    try:
        logger.info("Connecting to MongoDB")
        client = AsyncIOMotorClient(settings.MONGO_URI)
        db = client[settings.DATABASE_NAME]
        logger.info(f"Connected to {settings.DATABASE_NAME} using {settings.MONGO_URI}")
    except Exception as e:
        logger.error(f"Failed to connect to mongo: {e}") 

async def close_mongoDB_connection():
    global client
    if client:
        logger.info("Closing MongoDB connection")
        client.close()
        logger.info("MongoDB connection closed")

def get_collection(collection_name: str):
    global db
    if db is None:
        raise Exception("MongoDB is not connected")
    col = db[collection_name]
    return col