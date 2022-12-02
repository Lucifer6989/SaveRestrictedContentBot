#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 4783634
API_HASH = "f6c33f46599246676f75e153b615dbbc"
BOT_TOKEN = "5282656364:AAGlZaYBX8yvzBmngA8L9CLWQej1HxfsMsc"
SESSION = "BQAJr1LUg7YhUQe4n5oTkgttJjxMCCwODN8e_xTxpV7K9cGQtbxZa4jriVO0Zwve5ushrwa7CaFbSPYPP7Vvm9u-J1GxFwSv4Tj647DlqOygHLZJApJ-St3lvVu392o8sPyJ3TYVpPJQKZyo7dvdmU5JLrAwEkwdsy__3EkrVHvl5-fU6H0gWapnUpZ4PxmAM5dhQFOrGIcfwaGpTPvfBAVTSuZgacEauxI9sUNimS3aTg-WaJpq4agcVwPteU3hjO2Fugfk8SSuFxYQlcOYXAkeYVOYIKh1_yxyrLDWxYvngilhKYKxjatMLvoipMU36pUcXSX3_CW_mqoVONZu0VtCa3-QZQA"
FORCESUB = config("FORCESUB", default=None)
AUTH = 1476517140

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
