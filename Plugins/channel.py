import logging
logger = logging.getLogger(__name__)

from pyrogram import Client, filters, enums
from bot import Star_Moviess_Tamil
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BANNED_CHANNELS

@Star_Moviess_Tamil.on_message(
    filters.channel
    & (
        filters.document
        | filters.video
    ),
    group=4,
)
async def channel_receive_handler(bot, broadcast):
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔥 Uploaded By", url=f'https://telegram.me/Star_Moviess_Tamil')]])
    try:
        await bot.edit_message_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
