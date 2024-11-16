from pyrogram import Client, filters
import random
from shizuchat import shizuchat

# Command to start a chatfight
@shizuchat.on_message(filters.command("chatfight"))
async def chatfight(client, message):
    if len(message.command) < 3:
        await message.reply("Usage: /chatfight @user1 @user2")
        return

    user1 = message.command[1]
    user2 = message.command[2]

    # Simulate a fight outcome
    outcome = random.choice([f"{user1} wins!", f"{user2} wins!", "It's a draw!"])
    
    await message.reply(outcome)
