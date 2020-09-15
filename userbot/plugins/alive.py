"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
Ꮆ丨尺ㄩ爪:
from pyrogram.errors import ChatSendMediaForbidden
from pyrogram.errors.exceptions import FileIdInvalid, FileReferenceEmpty
from pyrogram.errors.exceptions.bad_request_400 import BadRequest, ChannelInvalid, MediaEmpty

from userge.core.ext import RawClient
from userge import userge, Message, Config, versions, get_version

LOGO_ID, LOGO_REF = None, None

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
pm_caption = "`Ethio <Userbot> 🇪🇹 IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**Ethio <Userbot> 🇪🇹 OS** : `3.14`\n"
pm_caption += f"**My Boss 💪** : {DEFAULTUSER} \n"
pm_caption += "**Made By 😎** : @M1nH11 & @xaleb\n\n"
pm_caption += "Deploy Your Own : [Repo](https://github.com/girume1/CBA-Userbot)\n"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
try:
        await _send_alive(message, output)
    except (FileIdInvalid, FileReferenceEmpty, BadRequest):
        await _refresh_id()
        await _send_alive(message, output)


def _parse_arg(arg: bool) -> str:
    return "enabled" if arg else "disabled"


async def _send_alive(message: Message, text: str) -> None:
    if not (LOGO_ID and LOGO_REF):
        await _refresh_id()
    try:
        await message.client.send_animation(chat_id=message.chat.id,
                                            animation=LOGO_ID,
                                            file_ref=LOGO_REF,
                                            caption=text)
    except (MediaEmpty, ChatSendMediaForbidden):
        await message.client.send_message(chat_id=message.chat.id,
                                          text=text,
                                          disable_web_page_preview=True)


async def _refresh_id():
    global LOGO_ID, LOGO_REF  # pylint: disable=global-statement
    try:
        gif = (await userge.get_messages('EthioUserBot', 14)).animation
    except ChannelInvalid:
        LOGO_ID = None
        LOGO_REF = None
    else:
        LOGO_ID = gif.file_id
        LOGO_REF = gif.file_ref
