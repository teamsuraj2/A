import asyncio
import importlib

from pyrogram import idle

from Banword import Banword
from Banword.modules import ALL_MODULES
from config import LOGGER_ID

loop = asyncio.get_event_loop()


async def roy_bot():
    await Banword.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Banword.modules." + all_module)
    print(f"• @{(await Banword.get_me()).username} B𝗈𝗍 Started Successfully.")
    await idle()
    print("• Don't edit baby, otherwise you get an error: @TwsAssociation")
    await Banword.send_message(
        LOGGER_ID, "**✦ ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ.\n\n✦ ᴊᴏɪɴ - @TwsAssociation**"
    )


if __name__ == "__main__":
    loop.run_until_complete(roy_bot())
