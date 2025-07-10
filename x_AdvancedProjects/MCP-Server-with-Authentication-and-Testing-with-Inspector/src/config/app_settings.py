# src\config\app_settings.py

import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class AppSettings:
    API_KEY = os.getenv("API_KEY", "") 
    LOG_DIR = os.getenv("LOG_DIR", "logs")
     

logger.info("Settings loaded: LOG_DIR=%s", AppSettings.LOG_DIR)