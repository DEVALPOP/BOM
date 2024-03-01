from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions

from DAXXMUSIC import app


@app.on_message(filters.command(["حظر"], prefixes=["/", "!", "%", ",", ".", "@", "#", "*"]))
async def test_ban(c, msg):

    if msg.text == "حظر" and msg.reply_to_message:
        user = await chat.get_member(msg.from_user.id)
        if user.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or msg.from_user.id == 5719372657:
            member = await msg.chat.get_member(msg.reply_to_message.from_user.id)
            if msg.reply_to_message.from_user.id == 5719372657:
                return await msg.reply_text("دا مطور")
            if user.status == [ChatMemberStatus.OWNER]:
                return await msg.reply_text("دا مالك")
            if user.status == [ChatMemberStatus.ADMINISTRATOR]:
                return await msg.reply_text("دا مشرف")
            await c.ban_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
            await msg.reply_text("tm")
        else:
            await msg.reply_text("لازم تكون مشرف")
