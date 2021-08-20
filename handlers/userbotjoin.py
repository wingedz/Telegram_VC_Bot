from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import config
from config import BOT_USERNAME
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Aggiungimi come admin</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Music"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Sono entrato!")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Userbot già in chat</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑</b>",
        )
        return
    await message.reply_text(
            "<b>L'userbot è entrato</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Errore!</b>",
        )
        return
