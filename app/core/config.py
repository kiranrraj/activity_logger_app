from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Activity Logger"
    ENVIRONMENT: str = "development"
    MONGO_URI: str
    DATABASE_NAME: str
    COLLECTION_NAME: str
    LOG_LEVEL: str 
    
# @lru_cache() caches the Settings() object.
# Prevents reloading the .env file every time you call get_settings().
@lru_cache()
def get_settings():
    return Settings()