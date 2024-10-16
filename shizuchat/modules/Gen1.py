from pyrogram import filters
from pyrogram.types import Message

from shizuchat import shizuchat
from shizuchat.modules.helpers.button import keyboard


@shizuchat.on_cmd(["gen"])
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"ʜᴇʏ {message.from_user.first_name},\n\n๏ ɪ ᴀᴍ ᴛʀᴜꜱᴛᴇᴅ ꜱᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ꜰᴜʟʟʏ ꜱᴀꜰᴇ & ꜱᴇᴄᴜʀᴇ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
  
