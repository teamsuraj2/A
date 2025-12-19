from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from Banword import Banword as app
from Banword.helper.database import add_chat, add_user
from config import LOGGER_ID

START_IMG = "https://files.catbox.moe/iem38x.jpg"


def get_start_caption(user):
    return f"""
**𝖧𝖾𝗒** {user.mention} 

🤖 I am a **Abuse Remover Bot**.
I delete messages with Abuse word and restrict users who have Banword .

🚫 I also delete messages with **Banword**.
"""


def start_btn(u):

    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("𝗔𝗱𝗱 𝗠𝗲 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽", url=f"https://t.me/{u}?startgroup=true")],
            [InlineKeyboardButton("𝗛𝗲𝗹𝗽", callback_data="show_help")],
            [
                InlineKeyboardButton("💬 𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/dnsmusicupdate"),
                InlineKeyboardButton("🚀 𝗨𝗽𝗱𝗮𝘁𝗲", url="https://t.me/Team_Dns_Network"),
            ],
            [InlineKeyboardButton("𝗢𝘄𝗻𝗲𝗿", url="https://t.me/dnsmusicupdate")],
        ]
    )


@app.on_message(group=-11)
async def add_m(_, m):
    if m.chat.type == ChatType.PRIVATE:
        await add_user(m.from_user.id)
    if m.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        await add_chat(m.chat.id)


@app.on_message(filters.command("start") & (filters.private | filters.group))
async def start_command(_, message: Message):
    user = message.from_user
    chat = message.chat

    if chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        await add_chat(chat.id)

    if chat.type == ChatType.PRIVATE:
        await add_user(user.id)
        await message.reply_photo(
            photo=START_IMG,
            caption=get_start_caption(user),
            has_spoiler=True,
            reply_markup=start_btn((await app.get_me()).username),
        )
        await app.send_message(LOGGER_ID, f"{user.mention} has started the bot.")
    else:
        await message.reply_text(
            f"**𝖧𝖾𝗒 {user.mention}, 𝖳𝗁𝖺𝗇𝗄𝗌 𝖥𝗈𝗋 𝖠𝖽𝖽𝗂𝗇𝗀 𝖬𝖾!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "𝖯𝗋𝗂𝗏𝖺Ban𝗍𝖺𝗋𝗍",
                            url=f"https://t.me/{(await app.get_me()).username}?start=help",
                        )
                    ]
                ]
            ),
        )


@app.on_callback_query(filters.regex("^back_to_start$"))
async def back_to_start(_, query: CallbackQuery):
    user = query.from_user
    chat_id = query.message.chat.id

    await query.message.delete()

    await app.send_photo(
        chat_id=chat_id,
        photo=START_IMG,
        caption=get_start_caption(user),
        has_spoiler=True,
        reply_markup=start_btn((await app.get_me()).username),
    )
