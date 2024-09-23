import os
from os import getenv
from dotenv import load_dotenv
from OWNER import BOT_ELkenawey, OWNER, OWNER_ELKENAWY, DATABASE, CHANNEL, GROUP, LOGS, VIDEO

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
user = {}
call = {}
dev = {}
logger = {}
logger_mode = {}
botname = {}
appp = {}
helper = {}



API_ID = int(getenv("API_ID", "6562407329"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
BOT_ELkenawey = BOT_TOKEN
MONGO_DB_URL = DATABASE
OWNER = OWNER
OWNER_ELKENAWY= OWNER_ELkenawy
CHANNEL = CHANNEL
GROUP = GROUP
LOGS = LOGS
VIDEO = VIDEO
