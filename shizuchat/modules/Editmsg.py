from shizuchat import shizuchat
from pyrogram import Client, filters
import asyncio
from pyrogram import *
@shizuchat.on_message(filters.text)
async def delete_edited_message(client, message):
    # Wait for a specified time (e.g., 10 seconds)
    await asyncio.sleep(10)
    await message.delete()
