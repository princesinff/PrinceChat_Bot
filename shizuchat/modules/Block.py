import asyncio
from sys import version as pyver

import pyrogram
from shizuchat import shizuchat
from pyrogram import __version__ as pyrover
from pyrogram import filters, idle
from config import OWNER_ID
from pyrogram.errors import FloodWait
from pyrogram.types import Message

import config
from shizuchat.modules.helpers import mongo
from shizuchat.modules.helpers.mongo import db

@shizuchat.on_cmd(["block"])
async def block_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var not defined. Please define it first"
            )
        if message.reply_to_message:
            if not message.reply_to_message.forward_sender_name:
                return await message.reply_text(
                    "Please reply to forwarded messages only."
                )
            replied_id = message.reply_to_message_id
            try:
                replied_user_id = save[replied_id]
            except Exception as e:
                print(e)
                return await message.reply_text(
                    "Failed to fetch user. You might've restarted bot or some error happened. Please check logs"
                )
            if await mongo.is_banned_user(replied_user_id):
                return await message.reply_text("Already Blocked")
            else:
                await mongo.add_banned_user(replied_user_id)
                await message.reply_text("Banned User from The Bot")
                try:
                    await app.send_message(
                        replied_user_id,
                        "You're now banned from using the Bot by admins.",
                    )
                except:
                    pass
        else:
            return await message.reply_text(
                "Reply to a user's forwarded message to block him from using the bot"
            )

@shizuchat.on_cmd(["unblock"])
async def unblock_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var not defined. Please define it first"
            )
        if message.reply_to_message:
            if not message.reply_to_message.forward_sender_name:
                return await message.reply_text(
                    "Please reply to forwarded messages only."
                )
            replied_id = message.reply_to_message_id
            try:
                replied_user_id = save[replied_id]
            except Exception as e:
                print(e)
                return await message.reply_text(
                    "Failed to fetch user. You might've restarted bot or some error happened. Please check logs"
                )
            if not await mongo.is_banned_user(replied_user_id):
                return await message.reply_text("Already UnBlocked")
            else:
                await mongo.remove_banned_user(replied_user_id)
                await message.reply_text(
                    "Unblocked User from The Bot"
                )
                try:
                    await app.send_message(
                        replied_user_id,
                        "You're now unbanned from the Bot by admins.",
                    )
                except:
                    pass
        else:
            return await message.reply_text(
                "Reply to a user's forwarded message to unblock him from the bot"
            )
