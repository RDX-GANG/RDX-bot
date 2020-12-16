# IMG + CODe CREDITS: @Sensei_nex
# some symbols credits goes to @kraken_the_badass

from uniborg.util import admin_cmd

from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "🔱╚»★𝐑𝐃𝐗bot★«╝🔱 user"
PM_IMG = "https://telegra.ph/file/90015e33395f6196486ee.gif"
pm_caption = "`🔥AAO BHARMANNN CHOD DAALE🔥\n"
pm_caption += "`                  ⇋【🛡️ 𝕾𝖞𝖘𝖙𝖊𝖒 𝖘𝖙𝖆𝖙𝖚𝖘 🛡️】⇌  `\n\n"
pm_caption += "`🔱─ᴛᴇʟᴇᴛʜᴏɴ─🔱       : `6.0.9**\n` 💎 Python 💎:` 3.8.5\n"
pm_caption += "`⚠️─ᴄᴜʀʀᴇɴᴛ ʙʀᴀɴᴄʜ─⚠️`: `↼🄼🄰🅂🅃🄴🅁⇀`\n"
pm_caption += "`🔱╚»★𝐑𝐃𝐗bot★«╝🔱      : `1.0`\n"
pm_caption += f"♾ ᴍʏ ʟɪᴇɢᴇ ♾       : {DEFAULTUSER} \n"
pm_caption += "✵─ᴍʏ ᴅᴇᴠ─✵          :  [✞R.I.P.✞](https://t.me/sensei_nex)\n\n"
pm_caption += "✮ License ✮         : [🔱╚»★𝐑𝐃𝐗bot★«╝🔱](https://github.com/RDX-GANG/RDX-bot/blob/master/LICENSE)\n"


@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)

    
