#!/usr/bin/env python3
from pyrogram import Client
from pyrogram import filters

# ~~~~~~ CONFIG ~~~~~~~~ #
ACCOUNT = "@ssfazeli"
PHONE_NR = '+989365881944'

# https://my.telegram.org/auth?to=apps
API_ID = 589029 
API_HASH = "d56f334a5f5531e5f54158a186951700"

# CHAT ID
SOURCE_CHAT = -671280694 
TARGET_CHAT = -671280694
# ~~~~~~~~~~~~~~~~~~~~~~ #

app = Client(
    ACCOUNT,
    phone_number=PHONE_NR,
    api_id=API_ID,
    api_hash=API_HASH
)

# filters.chat(SOURCE_CHAT)
@app.on_message(filters.chat(SOURCE_CHAT))
def my_handler(client, message):
    message.copy(  # copy() so there's no "forwarded from" header
        chat_id=TARGET_CHAT,  # the channel you want to post to
        caption="Copied from XYZ"  # Caption
    )

app.run()