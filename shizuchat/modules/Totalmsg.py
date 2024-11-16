from shizuchat import shizuchat
from pyrogram import Client, filters
from collections import defaultdict
from datetime import datetime, timedelta

# Dictionary to store message counts
user_message_count = defaultdict(lambda: {
    "total": 0,
    "today": 0,
    "week": 0,
    "month": 0,
    "last_message_time": None
})

# Command to check message rank
@shizuchat.on_message(filters.command("msg"))
async def rank(client, message):
    user_id = message.from_user.id
    user_data = user_message_count[user_id]

    # Prepare the rank message
    rank_message = (
        f"Your message stats:\n"
        f"Total messages: {user_data['total']}\n"
        f"Messages today: {user_data['today']}\n"
        f"Messages this week: {user_data['week']}\n"
        f"Messages this month: {user_data['month']}\n"
    )
    
    await message.reply(rank_message)

# Increment message count on every message
@shizuchat.on_message(filters.text)
async def count_messages(client, message):
    user_id = message.from_user.id
    now = datetime.now()

    # Update total messages
    user_message_count[user_id]["total"] += 1

    # Check and update today's count
    if user_message_count[user_id]["last_message_time"] is None or user_message_count[user_id]["last_message_time"].date() != now.date():
        user_message_count[user_id]["today"] = 1
    else:
        user_message_count[user_id]["today"] += 1

    # Check and update this week's count
    if user_message_count[user_id]["last_message_time"] is None or user_message_count[user_id]["last_message_time"] < now - timedelta(weeks=1):
        user_message_count[user_id]["week"] = 1
    else:
        user_message_count[user_id]["week"] += 1

    # Check and update this month's count
    if user_message_count[user_id]["last_message_time"] is None or user_message_count[user_id]["last_message_time"].month != now.month or user_message_count[user_id]["last_message_time"].year != now.year:
        user_message_count[user_id]["month"] = 1
    else:
        user_message_count[user_id]["month"] += 1

    # Update the last message time
    user_message_count[user_id]["last_message_time"] = now


