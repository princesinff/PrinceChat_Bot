import sys
import asyncio
import importlib
from flask import Flask
import threading
from pyrogram import idle
from pyrogram.types import BotCommand
from config import OWNER_ID
from shizuchat import LOGGER, shizuchat
from shizuchat.modules import ALL_MODULES
from shizuchat.modules.Clone import restart_bots

async def anony_boot():
    try:
        await shizuchat.start()
        
        
        asyncio.create_task(restart_bots())
        
    except Exception as ex:
        LOGGER.error(ex)

    for all_module in ALL_MODULES:
        importlib.import_module("shizuchat.modules." + all_module)
        LOGGER.info(f"Successfully imported : {all_module}")

    
    try:
        await shizuchat.set_bot_commands(
            commands=[
                BotCommand("start", "✧ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ✧"),
                BotCommand("help", "✧ ɢᴇᴛ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ✧"),
                BotCommand("ping", "✧ ᴄʜᴇᴄᴋ ɪғ ᴛʜᴇ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇsᴅ ✧"),
                BotCommand("shipping", "✧ ᴄᴏᴜᴘʟᴇs ᴏғ ᴅᴀʏ ✧"),
                BotCommand("rankings", "✧ ᴜsᴇʀ ᴍsɢ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ ✧"),
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")
    
    LOGGER.info(f"@{shizuchat.username} Started.")
    try:
        await shizuchat.send_message(int(OWNER_ID), f"{shizuchat.mention} has started")
    except Exception as ex:
        LOGGER.info(f"@{shizuchat.username} Started, please start the bot from owner id.")
    
    await idle()

# Flask Server Code for Health Check
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    # Start Flask server in a new thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Start the bot asynchronously
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping shizuchat Bot...")
    
