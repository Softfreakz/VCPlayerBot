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
I am Softfreakz Music Player Bot, Created by my master Softfreakz

For any issue support or error report contact my Master Softfreakz!
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="www.softfreakz.com",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="www.softfreakz.com"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="www.softfreakz.com"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Join ChatGroup", url="www.softfreakz.com"
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
