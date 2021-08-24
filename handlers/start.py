from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@DZVCrobot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Ciao 👋🏻 {}!**\n\nPosso riprodurre musica nelle chat vocali dei gruppi di Telegram.Ho un sacco di fantastiche funzioni che ti stupiranno!\n\n** Usa il comando /cmdlist per ulteriori informazioni sul mio utilizzo ❤**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Aggiungimi al tuo gruppo➕", url="https://t.me/DZVCrobot?startgroup=true")
            ],[
            InlineKeyboardButton("Commandi 🛠", url="https://telegra.ph/DZVCrobot-08-20")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@DZVCrobot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**Music Bot Online ✅**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="🎙️ Supporto 🎙️", url="https://t.me/Winged_z")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@DZVCrobot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**Menu di aiuto**

__× Aggiungimi al tuo gruppo..
× Rendimi admin con tutti i permessi..__

**🏷Comandi**
◎ /play <nome canzone> - play song you requested
◎ /playlist - Mostra la playlist
◎ /current - Mostra cos'è in riproduzione
◎ /player - apri le impostazioni
◎ /pause - metti in pausa la canzone
◎ /resume - riprendi la canzone
◎ /skip - passa alla prossima canzone in queue
◎ /end - stoppa la canzone
◎ /userbotjoin - fai entrare l'userbot
◎ /userbotleave - fai uscire l'userbot
◎ /reload - Aggiorna la lista degli admin
""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Supporto 🎙️", url="https://t.me/Winged_z")
              ]]
          )
      )
