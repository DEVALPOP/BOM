import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from DAXXMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InputMediaPhoto, InputMediaVideo
from DAXXMUSIC import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from DAXXMUSIC import Telegram, YouTube, app
from DAXXMUSIC.misc import SUDOERS
from DAXXMUSIC.plugins.sudo.sudoers import sudoers_list
from DAXXMUSIC import check_client
from DAXXMUSIC.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from DAXXMUSIC.utils.decorators.language import LanguageStart
from DAXXMUSIC.utils.inline import (help_pannel, private_panel,
                                     start_pannel)





#async def hilo(client, message: Message, _):
    #out = start_pannel(_)
    #await message.reply_video(
        #video=f"https://telegra.ph/file/46725d06d4a277c32fe64.mp4",
        #caption=f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 .](https://t.me/so_alfaa)\n\n[❍ | 𝐋𝐮𝐫𝐚 𝐓𝐡𝐞 𝐁𝐞𝐬𝐭 𝐒𝐨𝐮𝐫𝐜𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞 .](https://t.me/so_alfaa)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/so_alfaa)""",
        #reply_markup=InlineKeyboardMarkup(
            #[
                #[
                    #InlineKeyboardButton(
                        #"الاعدادات", callback_data="settings_helper"),
                    #InlineKeyboardButton(
                        #"الاوامر", url=f"https://t.me/{app.username}?start=help")
                #],[
                    #InlineKeyboardButton(
                        #"مطورين السورس", callback_data=f"eslam"),
            #],
            #]
        #),
    #)
    
    
@app.on_callback_query(filters.regex("fft"))
async def fft(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)

    await query.edit_message_media(
       InputMediaPhoto(
           "https://graph.org/file/3cd7d168316e95c6dbfbd.jpg",
           ""
       ),
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", url=f"t.me/MGIMT"),
                    InlineKeyboardButton(
                        "◌ᴅᴇᴠᴇʟᴏᴘᴇʀ◌", url=f"t.me/IQ7amo")
                ],[
                    InlineKeyboardButton(
                        "", callback_data="close"),
                    InlineKeyboardButton(
                        "گەڕانەوە", callback_data="am"),
               ],
          ]
        ),
    )    
    
    

@app.on_callback_query(filters.regex("tele"))
async def eslam(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/3f991cf109e90c025f35a.mp4",None,
           "**✧ فێرکاری پەخشکردنی ڤۆیس و گۆرانی و ڤیدیۆی تێلێگرام\n- ڕپلەی ڤۆیس یان گۆرانی یان ڤیدیۆ بکە نموونە :\n• پ ئەلینا یان پلەی\n• بە ئینگلیزی /play\n• وەڵامی ڤۆیس یان ڤیدیۆ پەخشی دەکات**"
       ),
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("", url=f"t.me/EHS4SS"),
                    InlineKeyboardButton("گەڕانەوە", callback_data="ko")
                ],[
                    InlineKeyboardButton("", url=f"t.me/IQMUC"),
                ],[
                    InlineKeyboardButton("◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data="fft"),
                    InlineKeyboardButton("", callback_data="ko"),
               ],
          ]
        ),
    )  


@app.on_callback_query(filters.regex("ko"))
async def back1(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/06f578ffcacbfea71ad30.mp4",None,
           "**✧ بەخێربێن بۆ بەشی پەخشکردنی پلاتفۆڕمەکان\n- پشتگیری لە پلاتفۆڕمەکان ↓**\n\n**• Telegram\n• Youtube\n• SoundCloud\n• AppleMusic\n• Spotify\n\n- فێرکای لە دوگمەکانی خوارەوەیە**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "• 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆", callback_data=f"tele"),
                     InlineKeyboardButton(
                        "• 𝖸𝗈𝗎𝖳𝗎𝖻𝖾", callback_data=f"yout"),
                     InlineKeyboardButton(
                        "• 𝖲𝗉𝗈𝗍𝗂𝖿𝗒", callback_data=f"spo"),
                ],[
                     InlineKeyboardButton(
                        "• 𝖠𝗉𝗉𝗅𝖾𝖬𝗎𝗌𝗂𝖼", callback_data=f"apple"),
                     InlineKeyboardButton(
                        "• 𝖲𝗈𝗎𝗇𝖽𝖢𝗅𝗈𝗎𝖽", callback_data=f"sound"),
                ],[
                     InlineKeyboardButton(
                        "", callback_data=f"fft"),
                ],[

                     InlineKeyboardButton(
                        "گەڕانەوە", callback_data=f"am"),
                ],[

                     InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data=f"fft"),


                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("don"))
async def don(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/417746bcdb462a48ea974.mp4",None,
           "**بەخێربێن بۆ بەشی داگرتن ♪\nبۆ گەڕانی گۆرانی یان ڤیدیۆ و داگرتنی ↓\n\n[ گەڕان + ناوی گۆرانی ..]\n\nنموونە -› گەڕان قادر کابان فریشتە**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "", callback_data=f"tele"),
                    InlineKeyboardButton(
                        "", callback_data=f"ddd"),
                ],[
                    InlineKeyboardButton(
                        "", callback_data=f"fft"),
                    InlineKeyboardButton(
                        "", callback_data=f"ddd"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data=f"fft"),

                     InlineKeyboardButton(
                        "", callback_data=f"fft"),
                ],[

                     InlineKeyboardButton(
                        "", callback_data=f"close"),

                     InlineKeyboardButton(
                        "گەڕانەوە", callback_data=f"am")
                ],[

                     InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data=f"fft")

                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("yout"))
async def donnr(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/7300df6491dfcbe571680.mp4",None,
           "**◌ بەخێربێن بۆ بەشی پەخشکردنی 𝖸𝗈𝗎𝖳𝗎𝖻𝖾\n\n• دوو ڕێگا هەیە بۆ پەخشکردن :\n\n1 - دانانی لینك لەگەڵ فەرمانی پەخشکردن\n2 - [پ ئەلینا یان پلەی] ڕێپلەی لینك بکە\n\n◌ نموونە : پ ئەلینا https://youtu.be/UuEPuVjsoG4**\n- **سەیری ڤیدیۆ بکە بۆ تێگەیشتن**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "", callback_data=f"tele"),
                    InlineKeyboardButton(
                        "", callback_data=f"ddd"),
                ],[
                    InlineKeyboardButton(
                        "", callback_data=f"fft"),
                    InlineKeyboardButton(
                        "", callback_data=f"ddd"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data=f"fft"),

                     InlineKeyboardButton(
                        "", callback_data=f"fft"),
                ],[

                     InlineKeyboardButton(
                        "", callback_data=f"close"),

                     InlineKeyboardButton(
                        "گەڕانەوە", callback_data=f"ko")
                ],[

                     InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data=f"fft")

                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("apple"))
async def apple(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/76b82a7b8df689a169182.mp4",
           "**◌ بەخێربێن بۆ بەشی پەخشی 𝖠𝗉𝗉𝗅𝖾 𝖬𝗎𝗌𝗂𝖼 ♪\n\n• فەرمانی پەخشکردن بنووسە لەگەڵ لینکی 𝖠𝗉𝗉𝗅𝖾𝖬𝗎𝗌𝗂𝖼\n\n• نموونە :** [ `پلەی https://music.apple.com/sa/album/ipad/1616715862?i=1616715870&l=ar` ]\n\n**سەیری ڤیدیۆ بکە بۆ تێگەیشتن**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "", callback_data=f"tele"),
                    InlineKeyboardButton(
                        "", callback_data=f"ddd"),
                ],[
                    InlineKeyboardButton(
                        "", callback_data=f"fft"),
                    InlineKeyboardButton(
                        "", callback_data=f"ddd"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data=f"fft"),

                     InlineKeyboardButton(
                        "", callback_data=f"fft"),
                ],[

                     InlineKeyboardButton(
                        "", callback_data=f"close"),

                     InlineKeyboardButton(
                        "گەڕانەوە", callback_data=f"ko")
                ],[

                     InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data=f"fft")

                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("spo"))
async def spo(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/bc01ebc69dc2ff1f380d9.mp4",None,
           "**✶ بەخێربێن بۆ بەشی پەخشی 𝖲𝗉𝗈𝗍𝗂𝖿𝗒 ♪**\n\n**• فەرمانی پەخشکردن بنووسە لەگەڵ لینکی سپۆتیفای**\n\n**• نموونە :** [ `پلەی https://open.spotify.com/track/2GQB3Xe1J9D2sK90AtHfhI?si=aIuly9l-T-Gy5GvfZxpUiw&context=spotify%3Aplaylist%3A37i9dQZF1DXcJUwMZo8Ss1i=1616715870&l=ar` ]\n\n**سەیری ڤیدیۆ بکە بۆ تێگەیشتن**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "", callback_data=f"tele"),
                    InlineKeyboardButton(
                        "", callback_data=f"ddd"),
                ],[
                    InlineKeyboardButton(
                        "", callback_data=f"fft"),
                    InlineKeyboardButton(
                        "", callback_data=f"ddd"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data=f"fft"),

                     InlineKeyboardButton(
                        "", callback_data=f"fft"),
                ],[

                     InlineKeyboardButton(
                        "", callback_data=f"close"),

                     InlineKeyboardButton(
                        "گەڕانەوە", callback_data=f"ko")
                ],[

                     InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data=f"fft")

                ],
            ]
        ),
    )
