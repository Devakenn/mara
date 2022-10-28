from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "12103782"))
API_HASH = getenv("API_HASH", "c7407238fc27d47705106d6b76253bdc")
BOT_TOKEN = getenv("BOT_TOKEN", "5516806812:AAGtGK35h8gVVn3Jbi7QqvUTCn0xPbGAtwc")
SESSION_NAME = getenv("SESSION_NAME", "AQCZx1o--_WEP-KktOxzqzuQGmjb08MUUXTP1vwoT_ergfNbp0Z_oyoCkc_yvG5NdtDpZBwlQyBKcN8QwAe83GT4aip5eqvY162AZn_vRS11uM9b3xC8Mfxty_mJYgoV0cPoKFXnjVIvCVq2VL1Hvo2mfEAEZGUEKGaY1s6z2a6GxUGIqGOkJXuUT-pzB_DGuoaoqCxhiqSkDxkozi9V-y1ZJqVLw2mnVWSANPEo-5KxK2-_nFjqULBxjbnHOAtspNBLd1ZemctWS1_-IyBp_I-wGHwANJEYdwh_SlIZ7rDKOgGvaVEQOBkKR6cUzA-sjizMkADxexXbGP9rdEAaw4KvAAAAAVT_ZpUA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "iPiiii")
ALIVE_NAME = getenv("ALIVE_NAME", "aken")
BOT_USERNAME = getenv("BOT_USERNAME", "AzvzbbzBot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RR8R9-muntazer/mara")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "mus_3b2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ipiiii")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5186954055").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5186954055").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
