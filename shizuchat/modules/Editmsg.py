from shizuchat import shizuchat
from pyrogram import Client, filters
import asyncio
from pyrogram import *

@shizuchat.on_edited_message(filters.group & ~filters.me)
async def delete_edited_message(client, message):
    # Wait for a specified time (e.g., 5 seconds)
    await asyncio.sleep(5)
    await message.delete()
