#๐๐น๐ผ๐ฟ๐ฒ๐ป๐๐ฎ ๐ฝ๐ฟ๐ผ๐ท๐ฒ๐ฐ๐
#Ur Motherfucker If U Kang And Don't Give Creadits ๐ฅด

from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import BOT_IMG, BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"{BOT_IMG}",
        caption=f"""**โฎ๐ณ สษชษช ษช แด [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

โฎ **๐๐ฅ๐จ๐ซ๐๐ง๐ณ๐ ๐ฌ๐ฒ๐ฌ๐ญ๐๐ฆ ๐ฐ๐จ๐ซ๐ค๐ข๐ง๐  ๐๐ข๐ง๐**

โฎ **แดขแดษชแด แด แดส๊ฑษชแดษด : 5.0 Lาฝฦาฝสฦ**

โฎ **แดส แดแดกษดแดส : [{OWNER_NAME}](https://t.me/{OWNER_NAME})**

โฎ **๊ฑแดสแด ษชแดแด แดแดแดษชแดแด : `{uptime}`**

**๐ง๐ต๐ฎ๐ป๐ธ๐ ๐ณ๐ผ๐ฟ ๐๐๐ถ๐ป๐ด ๐ณ๐น๐ผ๐ฟ๐ฒ๐ป๐๐ฎโฅ๏ธ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ษขสแดแดแด", url=f"https://t.me/Florenza_support"
                    ),
                    InlineKeyboardButton(
                        "แดสแดษดษดแดส", url=f"https://t.me/Florenza_updates"
                    )
                ]
            ]
        )
    )
