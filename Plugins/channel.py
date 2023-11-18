import logging
logger = logging.getLogger(__name__)

from pyrogram import Client, filters, enums
from bot import Star_Moviess_Tamil

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
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        file_name = get_media_file_name(broadcast)
        file_hash = get_hash(log_msg, Var.HASH_LENGTH)
        stream_link = "https://{}/{}/{}?hash={}".format(Var.FQDN, log_msg.id, file_name, file_hash) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}/{}?hash={}".format(Var.FQDN,
                                    Var.PORT,
                                    log_msg.id,
                                    file_name,
                                    file_hash)
        shortened_link = await get_shortlink(stream_link)

        await log_msg.reply_text(
            text=f"<b>Channel Name :- {broadcast.chat.title}\nChannel ID :- <code>{broadcast.chat.id}</code>\nRequest URL :- https://t.me/{(await bot.get_me()).username}?start=Star_Bots_Tamil_{str(log_msg.id)}</b>",
            quote=True,
            parse_mode=ParseMode.HTML
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📥 Fast Download Link", url=f"https://t.me/{(await bot.get_me()).username}?start=Star_Bots_Tamil_{str(log_msg.id)}")]])
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"<b>Got FloodWait of {str(w.x)}s From {broadcast.chat.title}\n\nChannel ID :-</b> <code>{str(broadcast.chat.id)}</code>",
                             disable_web_page_preview=True, parse_mode=ParseMode.HTML)
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"<b>#Error_Trackback :-</b> <code>{e}</code>", disable_web_page_preview=True, parse_mode=ParseMode.HTML)
        print(f"Can't Edit Broadcast Message!\nError :- {e}")
