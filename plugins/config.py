import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7377106068:AAHrsLBCzA3wzLadWF1M-iIUbJFhQt3jQOk")
    
    API_ID = int(os.environ.get("API_ID", "24828869"))
    
    API_HASH = os.environ.get("API_HASH", "3b0dce801ac887dca64ca774a0f2e421")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "LegendSources"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://arupmondal9832819925:F29l4feKy31E4Fut@cluster0.8vyek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")   
    SESSION_NAME = os.environ.get("SESSION_NAME", "LegendSources")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002192714055"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "akmbotQ")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1801203400"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "aappg_bot")
                                  
