import asyncio
import math
import os
import shutil
import socket
from datetime import datetime

import dotenv
import heroku3
import requests
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from config import OWNER_ID
from shizuchat import shizuchat
from shizuchat.database.misc import XCB, HAPP
from shizuchat.database.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from shizuchat.database.pastebin import BADbin




@shizuchat.on_message(
    filters.command(["gitpull", "update"]) & filters.user(int(OWNER_ID))
)
async def update(_, message: Message):
        if HAPP is None:
            return await message.reply_text(_["heroku_1"])
            response = await message.reply_text(_["heroku_13"])
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit(_["heroku_14"])
    except InvalidGitRepositoryError:
        return await response.edit(_["heroku_15"])
    to_exc = f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]
    for checks in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("» ʙᴏᴛ ɪs ᴜᴘ-ᴛᴏ-ᴅᴀᴛᴇ.")
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    updates = "".join(
        f"<b>➣ #{info.count()}: <a href={REPO_}/commit/{info}>{info.summary}</a> ʙʏ -> {info.author}</b>\n\t\t\t\t<b>➥ ᴄᴏᴍᴍɪᴛᴇᴅ ᴏɴ :</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
        for info in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}")
    )
    _update_response_ = "**ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !**\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ\n\n__**ᴜᴩᴅᴀᴛᴇs:**__\n"
    _final_updates_ = f"{_update_response_} {updates}"

    if len(_final_updates_) > 4096:
        url = await BADbin(updates)
        nrs = await response.edit(
            f"**ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !**\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ\n\n__**ᴜᴩᴅᴀᴛᴇs :**__\n\n[ᴄʜᴇᴄᴋ ᴜᴩᴅᴀᴛᴇs]({url})",
            disable_web_page_preview=True,
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)
    os.system("git stash &> /dev/null && git pull")

    try:
        served_chats = await get_active_chats()
        for x in served_chats:
            try:
                await app.send_message(
                    chat_id=int(x),
                    text="{0} ɪs ᴜᴘᴅᴀᴛᴇᴅ ʜᴇʀsᴇʟғ\n\nʏᴏᴜ ᴄᴀɴ sᴛᴀʀᴛ ᴩʟᴀʏɪɴɢ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 15-20 sᴇᴄᴏɴᴅs.".format(
                        app.mention
                    ),
                )
                await remove_active_chat(x)
                await remove_active_video_chat(x)
            except:
                pass
        await response.edit(
            _final_updates_
            + f"» ʙᴏᴛ ᴜᴩᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! ɴᴏᴡ ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs",
            disable_web_page_preview=True,
        )
    except:
        pass

            return
        except Exception as err:
            await response.edit(
                f"{nrs.text}\n\nsᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ, ᴩʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʟᴏɢs."
            )
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text="ᴀɴ ᴇxᴄᴇᴩᴛɪᴏɴ ᴏᴄᴄᴜʀᴇᴅ ᴀᴛ #ᴜᴩᴅᴀᴛᴇʀ ᴅᴜᴇ ᴛᴏ : <code>{0}</code>".format(
                    err
                ),
            )
    else:
        os.system("pip3 install --no-cache-dir -U -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && python3 -m shizuchat")
        exit()

                  
