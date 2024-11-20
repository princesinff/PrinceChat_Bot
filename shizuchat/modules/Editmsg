from shizuchat import shizuchat
from shizuchat import shizuchat, mongo, LOGGER, db
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from pyrogram import *

@shizuchat.on_edited_message(filters.group & ~filters.me)
async def delete_edited_message(client, message):
    # Wait for a specified time (e.g., 2 seconds)
    await asyncio.sleep(2)
    await message.delete()
    await message.reply(f"**ʜᴇʏ, {message.from_user.mention}**\nʏᴏᴜ ᴇᴅɪᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪs ᴛᴏᴏ ʟᴏɴɢ ᴛʜᴀᴛ's ᴡʜʏ ɪ ʜᴀᴠᴇ ᴅᴇʟᴇᴛᴇᴅ ɪᴛ.")

    
