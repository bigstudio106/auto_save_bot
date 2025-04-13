from pyrogram import Client, filters
from config import BOT_TOKEN, SOURCE_CHANNEL
from database.save_file import save_file_to_db
from utils.log_file import log_event

app = Client("AutoSaveBot", bot_token=BOT_TOKEN)

@app.on_message(filters.channel & filters.chat(int(SOURCE_CHANNEL)) & (filters.document | filters.video | filters.audio))
async def save_file(client, message):
    await save_file_to_db(message)

    file_name = message.document.file_name if message.document else (
        message.video.file_name if message.video else (
            message.audio.file_name if message.audio else "Unknown"))

    await log_event(client, file_name, message.id)

app.run()
