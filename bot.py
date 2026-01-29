from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery
)

api_id = YOUR_API_ID
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"

app = Client(
    "file_id_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)


@app.on_callback_query(filters.regex("^cancel$"))
async def cancel(_, query: CallbackQuery):
    try:
        await query.message.delete()
    except:
        pass


@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text(
        "👋 **Hello!**\n\n"
        "Send me a **Video, Sticker, Photo, Voice, Audio, or Document** "
        "and I’ll give you its **File ID**.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📍 Update Channel",
                        url="https://t.me/NT_BOT_CHANNEL"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👩‍💻 Developer",
                        url="https://t.me/LISA_FAN_LK"
                    ),
                    InlineKeyboardButton(
                        "🚨 Support Group",
                        url="https://t.me/NT_BOTS_SUPPORT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⛔️ CLOSE",
                        callback_data="cancel"
                    )
                ]
            ]
        )
    )


@app.on_message(filters.command("help"))
async def help(_, message: Message):
    await message.reply_text(
        "**How to use this bot:**\n\n"
        "• Send any media file\n"
        "• Bot will reply with its File ID\n\n"
        "**Supported types:**\n"
        "Video, Sticker, Photo, Voice, Audio, Document\n\n"
        "**Owner:** @LISA_FAN_LK & @YEAH_NEW"
    )


@app.on_message(filters.private & filters.text & ~filters.command(["start", "help"]))
async def user_info(_, message: Message):
    user = message.from_user
    chat = message.chat

    text = (
        "**User Info**\n"
        f"ID: `{user.id}`\n"
        f"Name: {user.first_name}\n"
        f"Username: @{user.username}\n"
        f"Language: {user.language_code}\n\n"
        "**Chat Info**\n"
        f"Chat ID: `{chat.id}`\n"
        f"Type: {chat.type}"
    )

    await message.reply_text(text)


@app.on_message(
    filters.video
    | filters.sticker
    | filters.photo
    | filters.document
    | filters.voice
    | filters.audio
)
async def file_id_handler(_, message: Message):
    media = (
        message.video
        or message.sticker
        or message.photo
        or message.document
        or message.voice
        or message.audio
    )

    await message.reply_text(
        f"📁 **File ID:**\n`{media.file_id}`"
    )


if __name__ == "__main__":
    print("Bot is alive 🚀")
    app.run()
