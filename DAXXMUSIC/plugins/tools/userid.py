
from DAXXMUSIC import app
from pyrogram import Client, filters

from pyrogram.enums import ParseMode

####

@app.on_message(filters.command('id',"ايدي","الايدي"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[: الايدي :]({message.link})** `{message_id}`\n"
    text += f"**[هويتك:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ : الايدي :](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("** منور يقمر**", quote=True)

    text += f"**[ : ايدي الجروب :](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)


        




        









