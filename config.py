import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
SOURCE_CHANNEL = int(os.getenv("SOURCE_CHANNEL"))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
