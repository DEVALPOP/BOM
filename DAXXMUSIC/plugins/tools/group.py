from pyrogram import Client, filters
from pyrogram.types import Message
from DAXXMUSIC import app
from config import OWNER_ID

from pyrogram import filters, Client
from DAXXMUSIC import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from DAXXMUSIC.core.call import DAXX 
from DAXXMUSIC.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)


@app.on_message(filters.regex("مين في الكول"))
async def strcall(client, message):
    assistant = await group_assistant(DAXX,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./strings/call.mp3"), stream_type=StreamType().pulse_stream)
        text="↯︙الاعضاء المتواجدين في المكالمة المرئية :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="⦗ يتكلم ⦘"
            else:
                mut="⦗ لا يتكلم ⦘"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}:{user.mention}↬{mut}\n"
        text += f"\n↯︙عدد الاشخاص في المكالمة المرئية ↬ ⦗ {len(participants)} ⦘"    
        await message.reply(f"{text}")
        await asyncio.sleep(5)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"لم يتم العثور على دردشة فيديو نشطة.\nيرجى بدء دردشة فيديو في مجموعتك/قناتك والمحاولة مرة أخرى.")
    except TelegramServerError:
        await message.reply(f"ارسل مرة اخرى يوجد خطأ في احد سيرفرات التليكرام")
@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("𖠇 تم بدء المحادثه الصوتيه..✅\n│\n└𖠇 بواسطة الادمنيه 👨‍✈️ ")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : {da} ثواني ")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : دقيقة ")
        elif 2 <= ma[0] < 3:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : دقيقتين ")
        elif 3 <= ma[0] < 11:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : {ma[0]} دقايق ")  
        else:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : {ma[0]} دقيقه ")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : ساعه ")
        elif 2 <= ho[0] < 3:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : ساعتين ")
        elif 3 <= ho[0] < 11:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : {ho[0]} ساعات ")  
        else:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\│\n└𖠇 وقت المحادثة : {ho[0]} ساعة ")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : يوم ")
        elif 2 <= day[0] < 3:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : يومين ")
        elif 3 <= day[0] < 11:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : {day[0]} ايام ")  
        else:
            await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : {day[0]} يوم")
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"• قــــام ← {message.from_user.mention}"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n• بــدعـــوة ←{user.first_name}"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass
          

####

@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)

###
@app.on_message(filters.command("leavegroup")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = f"sᴜᴄᴄᴇssғᴜʟʟʏ   ʟᴇғᴛ  !!."
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


####


@app.on_message(filters.command(["spg"], ["/", "!", "."]))
async def search(event):
    msg = await event.respond("Searching...")
    async with aiohttp.ClientSession() as session:
        start = 1
        async with session.get(f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={event.text.split()[1]}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}", headers={"x-referer": "https://explorer.apis.google.com"}) as r:
            response = await r.json()
            result = ""
            
            if not response.get("items"):
                return await msg.edit("No results found!")
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r'\/\d', item["link"]):
                    link = re.sub(r'\/\d', "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            prev_and_next_btns = [Button.inline("▶️Next▶️", data=f"next {start+10} {event.text.split()[1]}")]
            await msg.edit(result, link_preview=False, buttons=prev_and_next_btns)
            await session.close()
