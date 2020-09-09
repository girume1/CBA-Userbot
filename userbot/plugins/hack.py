# by Girum

import asyncio

from userge import userge


@userge.on_cmd("hack$", about={'header': "kensar hacking animation"})
async def hack_func(message):
    user = await message.client.get_user_dict(message.from_user.id)
    heckerman = user['mention']
    animation_chars = [
        "
Connecting To Private Server \\
",
        "
Connecting To Private Server |
",
        "
Connecting To Private Server /
",
        "
Connecting To Private Server \\
",
        "
Connection Established 
",
        "
Target Selected
",
        "
Backdoor Found In Target
",
        "
Trying To Hack
",
        "
Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
",
        "
Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
",
        "
Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
",
        "
Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
",
        "
Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒
",
        "
Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒
",
        "
Hacking... 70%\n█████████████████▒▒▒▒▒
",
        "
Hacking... 88%\n█████████████████████▒
",
        "
Hacking... 100%\n███████████████████████
",
        "
Preparing Data... 1%\n▒██████████████████████
",
        "
Preparing Data... 14%\n████▒██████████████████
",
        "
Preparing Data... 30%\n████████▒██████████████
",
        "
Preparing Data... 55%\n████████████▒██████████
",
        "
Preparing Data... 72%\n████████████████▒██████
",
        "
Preparing Data... 88%\n████████████████████▒██
",
        "
Prepared Data... 100%\n███████████████████████
",
        "
Uploading Data to Server... 12%\n███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
",
        "
Uploading Data to Server... 44%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒
",
        "
Uploading Data to Server... 68%\n███████████████▒▒▒▒▒▒▒▒
",
        "
Uploading Data to Server... 89%\n████████████████████▒▒▒
",
        "
Uploaded Data to Server... 100%\n███████████████████████
",
        "User Data Upload Completed: Target's User Data Stored "
        "at downloads/victim/telegram-authuser.data.sql",
    ]
    hecked = (f"Targeted Account Hacked\n\n
ይህንን ጠለፋ ለማስወገድ
ለ {heckerman}
 "
              "69$ ወይም 2,484ይ ብር 🇪🇹 ክፈሉ😎
")
    max_ani = len(animation_chars)
    for i in range(max_ani):
        await asyncio.sleep(2)
        await message.edit(animation_chars[i % max_ani])
    await message.edit(hecked)