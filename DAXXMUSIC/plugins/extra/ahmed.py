from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus

@Client.on_message(filters.group, group=2)
async def ban(c, msg):
  if msg.text == "حظر" and msg.reply_to_message:
    user = await message.chat.get_member(msg.reply_to_message.from_user.id)
    if user.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      await msg.reply_text("شغال")
    else:
      await msg.reply_text("لازم تكون مشرف")
