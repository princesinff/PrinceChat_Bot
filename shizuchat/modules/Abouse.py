from pyrogram import Client, filters
from pyrogram import Client, filters
import asyncio
from pyrogram import *

@shizuchat.on_cmd(["bad_word"])
async def bad_word_filter(client, message):
    # Check if the message contains any bad words
    if any(bad_word in message.text.lower() for bad_word in bad_words):
        # Delete the message
        await message.delete()
        # Optionally, send a warning to the user
        await message.reply("Your message contained inappropriate language and has been removed.")
