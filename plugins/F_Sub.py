# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton('📢 ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 📢', url='https://t.me/+wm7HnsM4mM8xNmFl'), InlineKeyboardButton("📢 ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 📢", url=client.invitelink) ]]
    text = "**Sᴏʀʀy Dᴜᴅᴇ Yᴏᴜ'ʀᴇ Nᴏᴛ Jᴏɪɴᴇᴅ My Cʜᴀɴɴᴇʟ 😐. Sᴏ Pʟᴇᴀꜱᴇ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟ Tᴏ Cᴄᴏɴᴛɪɴᴜᴇ **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))






