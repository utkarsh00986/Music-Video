import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Bot")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "marrk855")
ALIVE_NAME = getenv("ALIVE_NAME", "Marrk")
BOT_USERNAME = getenv("BOT_USERNAME", "irinMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "marrkbot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "marrkmusic")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "marrkchannel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/de3dce819a91c99243f9e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Rishabhbhan4/video-Bot")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/8628c642a266a22effd8c.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/8628c642a266a22effd8c.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/8628c642a266a22effd8c.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/8628c642a266a22effd8c.png")
