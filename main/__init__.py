#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 14476409
API_HASH = "8e36763bdeedf326512b5453368474cc"
BOT_TOKEN ="5642701991:AAGfKwNnjQmvrJOjbKudRUhK-DNgOE3A79s"
SESSION = "BAB7_iGwOYYCpHoVuLSWyw70Q8_I6y2sK-Tejv0Trm2nY_JCLaA93pzAz1KjdhvHwtrhFXOQ_fhy8XEW8mI5sxl5dwHill529Skwbnrxp-tr1GlNUpfOy574Av667UPQNJiqjTaYyjEMW8KsstqGN8P-il-MOCGWsbNd4J4UScao-_bRXi79QUmMDcd1ACoE_xnTSR1CvRuG04IHv1-DNEBTi8wXxmkUuO4yH7ybQlXSz1E5TLQdpZTXe6U45gq8R_z3b-euvJsJkFeL_BxQkpKwHzOZZiTGbtI12xgNSt8H6orbagdRcBJK-WrzCnLeeRcojT-HR-zgsk3yDCcShz2yAAAAAUJfRBMA"
FORCESUB = "shopeehaul20221"
AUTH = "5471325958"

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
