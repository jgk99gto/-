import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/387a2616036fbc923706a.mp4"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@H_M_Dr"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/بنك"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/ZZZ7iZ")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
