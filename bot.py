from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram import Client, filters
from pyrogram.types import Message

#ADD YOURS
api_id = 4888076
api_hash = '8b9b8214d84305d5ba8042c93575ea84'
bot_token = '6986631333:AAHJ1THDOYeWasJfJ58ARCmlyGcyCB2GPO8'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


# delete button
@app.on_callback_query(filters.regex('cancel'))
async def cancel(bot,update):
	try:
		await update.message.delete()
	except:
		return

# Define start command handler
@app.on_message(filters.command("start"))
async def start_command(bot, message: Message):
    # Check if the user has a first name
    if message.from_user.first_name:
        user_name = message.from_user.first_name
    else:
        user_name = "User"
    
    # Send personalized welcome message
    await message.reply_text(
        text="👋 Hey {user_name}, \n**Send me a video, sticker, photo, Voice, Audio, or document to get its file ID.**",
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('📍 𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/NT_BOT_CHANNEL'),
      ],
      [
          InlineKeyboardButton('👩‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫', url='https://t.me/LISA_FAN_LK'),
          InlineKeyboardButton('🚨 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/NT_BOTS_SUPPORT'),
          ],
          [
          InlineKeyboardButton('⛔️ 𝐂𝐋𝐎𝐒𝐄', callback_data='cancel')
        ]  
      ]
     ),
   )
    




# Define help command handler
@app.on_message(filters.command("help"))
async def help_command(bot, message: Message):
    help_msg = """
**Here's how to use this bot:**

- Send any of the following types of messages to get its file ID:
  - Video
  - Sticker
  - Photo
  - Voice
  - Audio
  - Document
  
- To start, use the /start command.

- For help, use the /help command.

**Enjoy using the bot! If you encounter any issues, feel free to contact the owner.**

**OWNER :** @LISA_FAN_LK @YEAH_NEW
"""
    await message.reply_text(help_msg)


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
