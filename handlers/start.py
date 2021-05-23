from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello🥳 {message.from_user.first_name}!
I am Softfreakz Music Player Bot, created by my master Softfreakz

For Help, Support or Error Report contact my Master Softfreakz!

List of Supported Streaming Platforms Given Below:
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵Music Bot Commands🎵", url="https://telegra.ph/Softfreakz-Music-Bot-Commands-05-23",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "YouTube", url="Youtube.com"
                    ),
                    InlineKeyboardButton(
                        "Jio Saavn", url="https://www.jiosaavn.com/"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Deezer", url="https://www.deezer.com"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
