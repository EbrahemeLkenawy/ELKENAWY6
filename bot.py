from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_ELkenawey
from pyromod import listen



bot = Client(
    "mo",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_ELkenawey=BOT_ELkenawey,
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    ELkenawy = @F_V_P
    await bot.send_message(ELkenawy, "**تم تشغيل ال صانع عزيزي المطور ،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور💎.")
    await idle()
