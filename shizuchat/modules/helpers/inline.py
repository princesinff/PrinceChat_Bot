from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from shizuchat import OWNER, shizuchat


START_BOT = [
    [
        InlineKeyboardButton(
            text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦",
            url=f"https://t.me/{shizuchat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="💫 ᴏᴡɴᴇʀ ❤️", user_id=OWNER),
        InlineKeyboardButton(text="⭐ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(text="« ғᴇᴀᴛᴜʀᴇs »", callback_data="HELP"),
    ],
]


DEV_OP = [
    [
        InlineKeyboardButton(text="💫 ᴏᴡɴᴇʀ ❤️", user_id=OWNER),
        InlineKeyboardButton(text="⭐ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦",
            url=f"https://t.me/{shizuchat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        # InlineKeyboardButton(text="🏔️ sᴏᴜʀᴄᴇ 🏔️", callback_data="SOURCE"),
        InlineKeyboardButton(text="💌 ᴀʙᴏᴜᴛ 💌", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦",
            url=f"https://t.me/{shizuchat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="⦿ ᴄʟᴏsᴇ ⦿",
            callback_data="CLOSE",
        ),
    ],
]


NEXT = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
        InlineKeyboardButton(text="⦿ ɴᴇxᴛ ⦿", callback_data="ADMIN_READ2"),
    ],
]

BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]


HELP_BTN = [
        [
        InlineKeyboardButton(text="🌸 ᴅᴇᴠ 🌸", callback_data="OWNER"),
    ],
    [
        InlineKeyboardButton(text="💫 ᴀᴅᴍɪɴs 💫", callback_data="ADMINS"),
        InlineKeyboardButton(text="🤖 ᴄʜᴀᴛʙᴏᴛ 🤖", callback_data="CHATBOT_CMD"),
    ],
    [ 
        InlineKeyboardButton(text="⚡ ᴀɪ ғᴇᴀᴛᴜʀᴇs ⚡", callback_data="AIBOT_CMD"),
        InlineKeyboardButton(text="🛒 ᴛᴏᴏʟs 🛒", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="disable_chatbot"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="SBACK"),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
        InlineKeyboardButton(text="🚫 ᴄʟᴏsᴇ 🚫", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="« ʜᴇʟᴘ »", url=f"https://t.me/{shizuchat.username}?start=help"
        ),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="📖 sᴜᴘᴘᴏʀᴛ 📖", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🌸 ᴏᴡɴᴇʀ ❤️", user_id=OWNER),
        #   InlineKeyboardButton(text="🏔️ sᴏᴜʀᴄᴇ 🏔️", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="📂 ᴜᴘᴅᴀᴛᴇs 📂", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]
