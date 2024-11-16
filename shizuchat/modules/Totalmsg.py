from pyrogram import Client, filters
from collections import defaultdict
from shizuchat import shizuchat
from shizuchat import shizuchat, mongo, LOGGER, db

# Dictionary to store message counts
user_message_count = defaultdict(int)

# Command to check total messages sent by the user
@shizuchat.on_message(filters.command("totalmsg"))
async def message_count(client, message):
    user_id = message.from_user.id
    count = user_message_count[user_id]
    await message.reply(f"ʜᴇʏ {message.from_user.mention}\nʏᴏᴜ ʜᴀᴠᴇ ꜱᴇɴᴛ ᴀ ᴛᴏᴛᴀʟ ᴏꜰ {count} ᴍᴇꜱꜱᴀɢᴇꜱ.")

# Increment message count on every message
@shizuchat.on_message(filters.text)
async def count_messages(client, message):
    user_id = message.from_user.id
    user_message_count[user_id] += 1
