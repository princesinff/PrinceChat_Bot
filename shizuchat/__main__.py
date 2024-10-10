import asyncio
import importlib

from pyrogram import idle
from config import OWNER_ID
from shizuchat import LOGGER, shizuchat
from shizuchat.modules import ALL_MODULES


async def anony_boot():
    try:
        await shizuchat.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("shizuchat.modules." + all_module)
        LOGGER.info(f"Successfully imported : {all_module}")

    LOGGER.info(f"@{shizuchat.username} Started.")
    try:
        await shizuchat.send_message(int(OWNER_ID), f"{shizuchat.mention} has started")
    except Exception as ex:
        LOGGER.info(f"@{shizuchat.first_name} Started, please start the bot from owner id.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping shizuchat Bot...")
