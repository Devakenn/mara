from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "5774874510:AAEnIkr8AXuQyagRv4oYHM-GnuWBQm6_uKk")
SESSION_NAME = getenv("SESSION_NAME", "AQC6-JnQ2OATjLxrC8n7E9uzVKY-58a2kXbXkjy91-U7yLyeNITHaIZNaHDFiqdqM-QrRAVc0CHO4ul08qe8pDU8CF6g6G_P2Saic9UzhIkpLpfyyszuueohDLi2V0f6yedW6DcuKztr_6XEtLlYIRgtHWzuRRIqMuHmLDp_hmYU4Vd0tV2rio9-PLeonZxsTlcJpUxYZ93sGUp0FKuUjTrBx9ZUJrZuVn4SYgLEcbkM1nA29p4jy5ryxzThSNKanG24LLkYpjSivO1WJi8hu6I_FpQENOyZOO3vKfRVWQfEvkRcE4phASahbKJkHhK5sBi04zY0LnpMiaYoqfQeFNFCAAAAAU31dE8A")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
ALIVE_NAME = getenv("ALIVE_NAME", "ali")
BOT_USERNAME = getenv("BOT_USERNAME", "LROBOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RR8R9-muntazer/mara")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
