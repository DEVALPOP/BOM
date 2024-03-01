from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions

from DAXXMUSIC import app

@app.on_message(filters.command(["حظر"], prefixes=["/", "!", "%", ",", ".", "@", "#", "*]))
async def test_ban(c, msg):

    if msg.text == "حظر" and message.reply_to_message:
        user = await chat.get_member(message.from_user.id)
        if user.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 5719372657:
            member = await msg.chat.get_member(message.reply_to_message.from_user.id)
            if message.reply_to_message.from_user.id == 5719372657:
                return await msg.reply_text("دا مطور")
            if user.status == [ChatMemberStatus.OWNER]:
                return await msg.reply_text("دا مالك")
            if user.status == [ChatMemberStatus.ADMINISTRATOR]:
                return await msg.reply_text("دا مشرف")
            await c.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await msg.reply_text("tm")
        else:
            await msg.reply_text("لازم تكون مشرف")
