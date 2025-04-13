from .db_connection import collection

async def save_file_to_db(message):
    file_info = {
        "file_name": message.document.file_name if message.document else None,
        "file_id": message.document.file_id if message.document else (
            message.video.file_id if message.video else (
                message.audio.file_id if message.audio else None)),
        "caption": message.caption,
        "from_channel": message.chat.id,
        "message_id": message.id
    }
    collection.insert_one(file_info)
