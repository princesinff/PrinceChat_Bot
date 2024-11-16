from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from pyrogram import *
from shizuchat import shizuchat
from shizuchat.database.permissions import adminsOnly, member_permissions

# Initialize a set of bad words
bad_words = {"lund"}

# Command to add bad words
@shizuchat.on_message(
    filters.command(["abuse"]))
@adminsOnly("can_restrict_members")
async def add_bad_word(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply("Please provide a bad word to add. Usage: /add_bad_word <word>")
        return

    new_bad_word = message.command[1].lower()
    if new_bad_word in bad_words:
        await message.reply(f"{new_bad_word} is already in the list of bad words.")
    else:
        bad_words.add(new_bad_word)
        await message.reply(f"{new_bad_word} has been added to the list of bad words.")

# Message handler to filter bad words
@shizuchat.on_message(filters.text)
async def bad_word_filter(client: Client, message: Message):
    if any(bad_word in message.text.lower() for bad_word in bad_words):
        await message.delete()
        await message.reply("Your message contained inappropriate language and has been removed.")
