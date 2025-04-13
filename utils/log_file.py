from config import LOG_CHANNEL

async def log_event(client, file_name, message_id):
    try:
        await client.send_message(
            LOG_CHANNEL,
            f"✅ **File Saved to DB**\n\n**File Name:** `{file_name}`\n**Message ID:** `{message_id}`"
        )
    except Exception as e:
        print(f"Failed to log event: {e}")
