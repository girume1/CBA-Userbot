"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/cbc375cdf9ab13c790cf8.jpg"
pm_caption = "Ethio <Userbot> 🇪🇹 IS: ONLINE\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "TELETHON VERSION: 6.0.9\nPython: 3.7.4\n"
pm_caption += "DATABASE STATUS: Functional\n"
pm_caption += "**Current Branch** : master\n"
pm_caption += "**Ethio <Userbot> 🇪🇹 OS** : 3.14\n"
pm_caption += f"**My Boss 💪** : {DEFAULTUSER} \n"
pm_caption += "**Made By 😎** : @M1nH11 & @xaleb\n\n"
pm_caption += "Deploy Your Own : [Repo](https://github.com/girume1/CBA-Userbot)\n"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
