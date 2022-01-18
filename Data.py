from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """**
Hi,
—— ——— ——
Wellcome To This Bot! 
Bot Can Swap from You A Number and give you Members! 
Now Start Swap Your Number!
—— ——— ——
By : @trprogram **
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("- Start Swap Session", callback_data="generate")],
        [InlineKeyboardButton(text="- Home", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("- Start Swap Session", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("- Start Swap Session", callback_data="generate")],
        [InlineKeyboardButton("- XDev", url="https://t.me/trprogram")],
        [
            InlineKeyboardButton("- Owner Acc1", url="https://t.me/ttrakos"),
            InlineKeyboardButton("- Owner Acc2", callback_data="https://t.me/rreback")
      ],
        [InlineKeyboardButton("- Channel Updates ", url="https://t.me/trprogram")],
    ]


    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About this bot
/help - How to use this bot
/start - Start Bot
/generate - Start Generating Session
/cancel - Cancel process
/restart - Restart process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to retrieve pyrograms and telethon string sessions by @nbzoning

Group Support : [Gabung](https://t.me/OkaeriUserbot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @zenfrans
    """
