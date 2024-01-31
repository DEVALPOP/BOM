from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import Message
from strings import get_string, helpers
from DAXXMUSIC import app
from pyrogram.types import InputMediaVideo
from DAXXMUSIC.misc import SUDOERS
from DAXXMUSIC.utils.database import add_sudo, remove_sudo
from DAXXMUSIC.utils.decorators.language import language
from DAXXMUSIC.utils.extraction import extract_user
from DAXXMUSIC.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID


@app.on_message(filters.command(["addsudo", "زیادکردنی گەشەپێدەر"],prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["delsudo", "rmsudo", "لادانی گەشەپێدەر"],prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["sudolist", "listsudo", "sudoers", "گەشەپێدەران", "گەشەپێدەرەکان"],prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
async def sudoers_list(client, message: Message):
    keyboard = [[InlineKeyboardButton("๏ گەشەپێدەران ๏", callback_data="check_sudo_list")]]
    reply_markups = InlineKeyboardMarkup(keyboard)

    # await message.reply_photo(photo="https://graph.org/file/3202937ba2792dfa8722f.jpg", caption="**» ᴄʜᴇᴄᴋ sᴜᴅᴏ ʟɪsᴛ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.**\n\n**» ɴᴏᴛᴇ:**  ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ. ", reply_markup=reply_markups)
    await message.reply_photo(photo="https://graph.org/file/3202937ba2792dfa8722f.jpg",caption="**» لیستی گەشەپێدەران ببینە بە دوگمەی خوارەوە**\n\n**» تێبینی : تەنیا گەشەپێدەرەکان دەتوانن بیبینن**",reply_markup=reply_markups)


# noinspection PyUnreachableCode
@app.on_callback_query(filters.regex("^check_sudo_list$"))
async def check_sudo_list(client, callback_query: CallbackQuery):

    user_id = CallbackQuery.from_user.id
    if user_id != CallbackQuery.message.reply_to_message.from_user.id:
        return
        user_mention = (user.first_name if not user.mention else user.mention)
        keyboard = []
        caption = f"**لیستی بەڕێوبەرەکان**\n\n**🌹خاوەنی بۆت** ➥ {user_mention}\n\n"

        keyboard.append([InlineKeyboardButton("๏ خاوەنی بۆت ๏", url=f"tg://openmessage?user_id={OWNER_ID}")])

        count = 1
        for user_id in SUDOERS:
            if user_id != OWNER_ID:
                try:
                    user = await app.get_users(user_id)
                    user_mention = user.mention if user else f"**👾 گەشەپێدەر {count} ئایدی:** {user_id}"
                    caption += f"**👾 گەشەپێدەر** {count} **»** {user_mention}\n"
                    button_text = f"๏ گەشەپێدەران {count} ๏ "
                    keyboard.append([InlineKeyboardButton(button_text, url=f"tg://openmessage?user_id={user_id}")]
                                    )
                    count += 1
                except:
                    continue

        # Add a "Back" button at the end
        keyboard.append([InlineKeyboardButton("๏ گەڕانەوە ๏", callback_data="back_to_main_menu")])

        if keyboard:
            reply_markup = InlineKeyboardMarkup(keyboard)
            await callback_query.message.edit_caption(caption=caption, reply_markup=reply_markup)


@app.on_callback_query(filters.regex("^back_to_main_menu$"))
async def back_to_main_menu(client, callback_query: CallbackQuery):
    keyboard = [[InlineKeyboardButton("๏ گەشەپێدەرەکان ๏", callback_data="check_sudo_list")]]
    reply_markupes = InlineKeyboardMarkup(keyboard)
    await callback_query.message.edit_caption(
        caption="**» لیستی گەشەپێدەران ببینە بە دوگمەی خوارەوە**\n\n**» تێبینی : تەنیا گەشەپێدەرەکان دەتوانن بیبینن**",
        reply_markup=reply_markupes)
