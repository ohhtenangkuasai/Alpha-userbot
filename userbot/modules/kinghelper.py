""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.khelp$")
async def usit(e):
    await e.edit(
        f"      ╭✠╼━━━━━━❖━━━━━━━✠╮\n     **BENTUAN**     \n╰✠╼━━━━━━❖━━━━━━━✠╯ \n"
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "◍ ᴏᴡɴᴇʀ  : [ZEEONE](t.me/zeeoneee) \n"
        "◍ ʀᴇᴘᴏ    : [klik](https://github.com/zeeoneofc/Alpha-userbot) \n"
        "◍ ɪɴꜱᴛᴀɢʀᴀᴍ : [klik](Instagram.com/zeeoneofc) \n"
        "◍ ɢʀᴏᴜᴘ ꜱᴜᴘᴘᴏʀᴛ : [Klik](https://t.me/alphabot_support)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"      ╭✠╼━━━━━━❖━━━━━━━✠╮\n  **DAFTAR VARS**     \n╰✠╼━━━━━━❖━━━━━━━✠╯ \n"
        f"**Daftar Vars Dari {DEFAULTUSER}:**\n"
        "◍ ᴅᴀꜰᴛᴀʀ ᴠᴀʀꜱ = [Klik](https://raw.githubusercontent.com/zeeoneofc/Alpha-userbot/Alpha-userbot/varshelper.txt)")


CMD_HELP.update(
    {
        "helper": "**✘ Plugin : **`helper`\
        \n\n  •  **Perintah :** `.khelp`\
        \n  •  **Function : **Bantuan Untuk **✵ ALPHABOT ✵**.\
        \n\n  •  **Perintah :** `.vars`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Perintah :** `.repo`\
        \n  •  **Function : **Melihat Repo **✵ ALPHABOT ✵**.\
        \n\n  •  **Perintah :** `.string`\
        \n  •  **Function : **Link untuk mengambil String **✵ ALPHABOT ✵**.\
    "
    }
)
