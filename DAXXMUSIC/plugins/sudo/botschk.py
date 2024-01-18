from DAXXMUSIC.misc import db
from DAXXMUSIC.utils.database import get_assistant, get_authuser_names, get_cmode

import asyncio
import config
import random
import asyncio
from datetime import datetime
from pyrogram.enums import ChatType
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.logging import LOGGER
from config import *
from pyrogram import filters
from DAXXMUSIC import app 
from DAXXMUSIC import app, userbot
from DAXXMUSIC.core.userbot import Client
from DAXXMUSIC.misc import SUDOERS





BOT_LIST = ["IQJOBOT", "IQMCBOT"]






@app.on_message(filters.command(["botschk","چالاکی بۆت","بۆتەکانم","botchk"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def bots_chk(app, message):
    msg = await message.reply_video(video="https://graph.org/file/201c35646084d635882be.mp4", caption="**پشکنین بۆ بۆتەکانم چالاکن یان ناچالاك👾🚀!**")
    response = "**پشکنین بۆ بۆتەکانم چالاکن یان ناچالاك👾🚀!**\n\n"
    for bot_username in BOT_LIST:
        try:
            bot = await userbot.get_users(bot_username)
            bot_id = bot.id
            await asyncio.sleep(0.5)
            bot_info = await userbot.send_message(bot_id, "/start")
            await asyncio.sleep(3)
            async for bot_message in userbot.get_chat_history(bot_id, limit=1):
                if bot_message.from_user.id == bot_id:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n**╰⊚ دۆخ: چالاك ✅**\n\n"
                else:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n**╰⊚ دۆخ: ناچالاك ❌**\n\n"
        except Exception:
            response += f"╭⎋ {bot_username}\n╰⊚ **sᴛᴀᴛᴜs: ᴇʀʀᴏʀ ❌**\n"
    
    await msg.edit_text(response)
