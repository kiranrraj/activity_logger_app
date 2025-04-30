import logging
from logging.handlers import RotatingFileHandler
from core.config import get_settings

settings = get_settings()

def setup_logger():

    # creates (or retrieves) a logger named "activity_logger".
    logger = logging.getLogger("activity_logger")

    # fetches the log level from settings, 
    # If the level name is invalid or missing, it defaults to logging.INFO
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    
    # Sets the overall level of this logger.
    logger.setLevel(log_level)

    # defines how log messages will be formatted
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Creates a handler that outputs log messages to the console (stdout).
    console_handler = logging.StreamHandler()

    # Applies the format to the console output.
    console_handler.setFormatter(log_format)

    # Attaches the console handler to the logger
    logger.addHandler(console_handler)

    # Creates a handler that writes logs to a file: activity.log.
    # Automatically rotates logs when the file size exceeds 10 MB (10**7 bytes).
    # Keeps the last 5 log files (like activity.log.1, activity.log.2, etc.).
    file_handler = RotatingFileHandler("activity.log", maxBytes=10**7, backupCount=5)
    
    # Applies the same format to file logs.
    file_handler.setFormatter(log_format)
    
    # Attaches the file handler to the logger
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()