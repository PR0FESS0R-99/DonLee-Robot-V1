# (c) @AlbertEinsteinTG
# (c) @Muhammed_RK, @MRK_YT, @Mo_Tech_Group, @MT_Botz
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee_Robot/blob/main/LICENSE

import re
from pyrogram import filters
from pyrogram import Client as DonLee_Robot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from DonLee_Robot import VERIFY # pylint: disable=import-error

@DonLee_Robot.on_message(filters.command(["settings"]) & filters.group, group=1)
async def settings(bot, update):
    
    chat_id = update.chat.id
    user_id = update.from_user.id if update.from_user else None
    global VERIFY

    if VERIFY.get(str(chat_id)) == None: # Make Admin's ID List
        admin_list = []
        async for x in bot.iter_chat_members(chat_id=chat_id, filter="administrators"):
            admin_id = x.user.id 
            admin_list.append(admin_id)
        admin_list.append(None)
        VERIFY[str(chat_id)] = admin_list

    if not user_id in VERIFY.get(str(chat_id)): # Checks if user is admin of the chat
        return
    
    bot_info = await bot.get_me()
    bot_first_name= bot_info.first_name
    
    text =f"<u>{bot_first_name}'𝐬</u> 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 𝐏𝐚𝐧𝐞𝐥.....\n"
    text+=f"\n<i>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐌𝐞𝐧𝐮 𝐓𝐨 𝐂𝐡𝐚𝐧𝐠𝐞 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐯𝐢𝐭𝐲 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐒𝐭𝐚𝐭𝐮𝐬 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐞𝐝 𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬, 𝐂𝐡𝐚𝐧𝐠𝐞 𝐅𝐢𝐥𝐭𝐞𝐫 𝐓𝐲𝐩𝐞𝐬, 𝐂𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐞 𝐑𝐞𝐬𝐮𝐥𝐭𝐬 𝐀𝐧𝐝 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐒𝐭𝐚𝐭𝐮𝐬 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩...</i>"
    
    buttons = [[
        InlineKeyboardButton("Channels", callback_data=f"channel_list({chat_id})"), 
        InlineKeyboardButton("Filter Types", callback_data=f"types({chat_id})")
        ],[
        InlineKeyboardButton("Configure", callback_data=f"config({chat_id})")
        ],[
        InlineKeyboardButton("Status", callback_data=f"status({chat_id})"),
        InlineKeyboardButton("About", callback_data=f"about({chat_id})")
        ],[
        InlineKeyboardButton("Close", callback_data="close")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message (
        chat_id=chat_id, 
        text=text, 
        reply_markup=reply_markup, 
        parse_mode="html",
        reply_to_message_id=update.message_id
        )

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F" 
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF" 
                               u"\U0001F1E0-\U0001F1FF" 
                               u"\U00002500-\U00002BEF" 
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"
                               u"\u3030"
    "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(r' ', str(string))
