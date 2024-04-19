from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize your Pyrogram client
api_id = 4888076
api_hash = '8b9b8214d84305d5ba8042c93575ea84'
bot_token = '6986631333:AAHJ1THDOYeWasJfJ58ARCmlyGcyCB2GPO8'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define start command handler
@app.on_message(filters.command("start"))
async def start_command(bot, message: Message):
    # Check if the user has a first name
    if message.from_user.first_name:
        user_name = message.from_user.first_name
    else:
        user_name = "User"
    
    # Send personalized welcome message
    await message.reply_text(f"Hey 👋 {user_name}, \nSend me a video, sticker, photo, Voice, Audio, or document to get its file ID.")



@app.on_message(filters.private & filters.text & ~filters.forwarded)
async def handle_new_user_text(bot, message: Message):
    new_user_info = {
        "id": message.from_user.id,      
        "is_bot": message.from_user.is_bot,
        "first_name": message.from_user.first_name,
        "username": message.from_user.username,
        "language_code": message.from_user.language_code
    }
    chat_info = {
        "id": message.chat.id,
        "type": message.chat.type,
        "username": message.chat.username,
        "first_name": message.chat.first_name
    }
    info_text = f"User Info:\n\n{new_user_info}\n\nChat Info:\n\n{chat_info}"
    await message.reply_text(info_text)



# Define handlers for different types of messages
@app.on_message(filters.video)
async def handle_video(bot, message: Message):
    # Handle video message
    await message.reply_text(f"Video file ID: {message.video.file_id}")

@app.on_message(filters.sticker)
async def handle_sticker(bot, message: Message):
    # Handle sticker message
    await message.reply_text(f"Sticker file ID: {message.sticker.file_id}")

@app.on_message(filters.photo)
async def handle_photo(bot, message: Message):
    # Handle photo message
    await message.reply_text(f"Photo file ID: {message.photo.file_id}")

@app.on_message(filters.document)
async def handle_document(bot, message: Message):
    # Handle document message
    await message.reply_text(f"Document file ID: {message.document.file_id}")

# Define handlers for voice and audio messages
@app.on_message(filters.voice)
async def handle_voice(bot, message: Message):
    # Handle voice message
    await message.reply_text(f"Voice file ID: {message.voice.file_id}")

@app.on_message(filters.audio)
async def handle_audio(bot, message: Message):
    # Handle audio message
    await message.reply_text(f"Audio file ID: {message.audio.file_id}")


# Run the client
if __name__ == "__main__":
    print("alive")
    app.run()
