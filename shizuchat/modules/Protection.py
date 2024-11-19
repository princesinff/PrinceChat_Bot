from shizuchat import shizuchat
from shizuchat import shizuchat, mongo, LOGGER, db
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from pyrogram import *

@shizuchat.on_message(filters.text)
async def delete_links(client, message):
    # Check if the message contains a link
    if "http://" in message.text or "https://" in message.text:
        # Delete the message
        await client.delete_messages(message.chat.id, message.message_id)
