import asyncio
import requests
from datetime import datetime
from config import BANNED_USERS, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram import Client as app, filters, enums

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)

muted_users = []
@app.on_message(filters.command(["كتم"], ""), group=39)
async def mute_user(client, message):
    global muted_users    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:    
        if message.reply_to_message.from_user.id == 6909581339:
            await app.send_message(message.chat.id, "عذرا لا يمكنك كتم المطور فيجا")
        else: 
         if message.reply_to_message:
           user_id = message.reply_to_message.from_user.mention
         if user_id not in muted_users:
            muted_users.append(user_id)
            await message.reply_text(f" {user_id}\nكتمته\n༄")
         else:
           await message.reply_text(f"{user_id}\nمكتوم  من قبل\n༄")
    else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")


@app.on_message(filters.command(["الغاء الكتم"], ""), group=62)
async def unmute_user(client, message):
   global muted_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339: 
    user_id = message.reply_to_message.from_user.mention
    if user_id in muted_users:
        muted_users.remove(user_id)
        await message.reply_text(f" {user_id}\nابشر الغيت كتمه\n༄")
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")    
       
        
        
       
@app.on_message(filters.text, group=9)
async def handlge_message(client, message):
    if message.from_user and message.from_user.id in muted_users:
        await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)

@app.on_message(filters.command(["المكتومين"], ""), group=137)
async def get_rmuted_users(client, message):
    global muted_users
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
         count = len(muted_users)
         user_ids = [str(user) for user in muted_users]
         response = f" <u>قائمة المكتومين وعددهم :</u> {count}\n"
         response += "⭓━⭓⭓⭓⭓━⭓\n"
         response += "\n".join(user_ids)
         await message.reply_text(response)
    else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")



@app.on_message(filters.command(["مسح المكتومين"], ""), group=136)
async def unmute_all(client, message):
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
    global muted_users
    count = len(muted_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in muted_users.copy():
        user_id = member
        try:
            muted_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"مسحت {successful_count} من المكتومين\n༄")
    else:
        await message.reply_text("↢ لا يوجد مستخدمين مكتومين ليتم مسحهم\n༄")

    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count}\nمن المكتومين\n༄")
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")


