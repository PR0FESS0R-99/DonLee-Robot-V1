import os
class Translation(object):
  
    START_TEXT = """𝐇𝐞𝐥𝐥𝐨👋 {}!!

𝐈 𝐚𝐦 𝐀𝐫𝐢𝐬𝐮 𝐚 𝐏𝐫𝐨 𝐀𝐮𝐭𝐨 𝐅𝐢𝐥𝐭𝐞𝐫 𝐁𝐨𝐭

𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐚𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐢𝐟 𝐲𝐨𝐮 𝐜𝐚𝐧'𝐭 𝐛𝐞𝐥𝐢𝐞𝐯𝐞 𝐆𝐢𝐯𝐞 𝐢𝐭 𝐚 𝐭𝐫𝐲...😉

𝐈𝐟 𝐲𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐭𝐫𝐲 𝐦𝐞 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐆𝐫𝐨𝐮𝐩 (𝐣𝐨𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 𝐜𝐥𝐢𝐜𝐤𝐢𝐧𝐠 𝐨𝐧 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐬𝐞𝐞 𝐚𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭𝐭𝐨𝐦 𝐨𝐟 𝐭𝐡𝐢𝐬 𝐦𝐞𝐬𝐬𝐚𝐠𝐞...🙂)

𝐏𝐫𝐞𝐬𝐬 /help 𝐓𝐨 𝐓𝐞𝐬𝐭 𝐌𝐲 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬😃

𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 @joel_boban"""
    
    HELP_TEXT = """
<u>𝐍𝐨𝐭𝐢𝐜𝐞</u>

<code>𝐈𝐦𝐝𝐛 𝐏𝐨𝐬𝐭𝐞𝐫 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐈𝐧 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭
𝐑𝐚𝐭𝐢𝐧𝐠 𝐍𝐨𝐭 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐈𝐧 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭</codd> 

<u>𝐁𝐨𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 (𝐖𝐨𝐫𝐤𝐬 𝐎𝐧𝐥𝐲 𝐢𝐧 𝐆𝐫𝐨𝐮𝐩)</u>

✯ <code>/add chat_id</code> - 𝐓𝐨 𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐚 𝐆𝐫𝐨𝐮𝐩 𝐖𝐢𝐭𝐡 𝐚 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 (𝐁𝐨𝐭 𝐒𝐡𝐨𝐮𝐥𝐝 𝐁𝐞 𝐀𝐝𝐦𝐢𝐧 𝐀𝐭 𝐁𝐨𝐭𝐡 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐖𝐢𝐭𝐡 𝐅𝐮𝐥𝐥 𝐏𝐫𝐢𝐯𝐢𝐥𝐞𝐠𝐞𝐬)
  
✯ <code>/del chat_id</code> - 𝐓𝐨 𝐃𝐢𝐬𝐜𝐨𝐧𝐧𝐞𝐜𝐭 𝐚 𝐆𝐫𝐨𝐮𝐩 𝐖𝐢𝐭𝐡 𝐚 𝐂𝐡𝐚𝐧𝐧𝐞𝐥
     
✯ <code>/delall</code>  - 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐖𝐢𝐥𝐥 𝐃𝐢𝐬𝐜𝐨𝐧𝐧𝐞𝐜𝐭 𝐀𝐥𝐥 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐞𝐝 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐖𝐢𝐭𝐡 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐥𝐥 𝐅𝐢𝐥𝐞𝐬 𝐅𝐫𝐨𝐦 𝐈𝐭𝐬 𝐃𝐁
    
✯ <code>/settings</code> -  𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐖𝐢𝐥𝐥 𝐃𝐢𝐬𝐩𝐥𝐚𝐲 𝐚 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 𝐏𝐚𝐧𝐞𝐥 𝐓𝐡𝐫𝐨𝐮𝐠𝐡 𝐓𝐡𝐢𝐬 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 𝐏𝐚𝐧𝐞𝐥 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐂𝐡𝐚𝐧𝐠𝐞 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭'𝐬 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬

   ✯ <code>Channel</code> - 𝐓𝐡𝐢𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 𝐖𝐢𝐥𝐥 𝐒𝐡𝐨𝐰 𝐘𝐨𝐮 𝐀𝐥𝐥 𝐓𝐡𝐞 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐞𝐝 𝐂𝐡𝐚𝐭𝐬 𝐖𝐢𝐭𝐡 𝐓𝐡𝐞 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐖𝐢𝐥𝐥 𝐒𝐡𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐂𝐨𝐫𝐫𝐞𝐬𝐩𝐨𝐧𝐝𝐢𝐧𝐠 𝐓𝐨 𝐈𝐭𝐬 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬
            
   ✯ <code>Filter Types</code> - 𝐓𝐡𝐢𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 𝐖𝐢𝐥𝐥 𝐒𝐡𝐨𝐰 𝐘𝐨𝐮 𝐃𝐢𝐟𝐟𝐞𝐫𝐞𝐧𝐭 𝐅𝐢𝐥𝐭𝐞𝐫𝐬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐎𝐧 𝐓𝐡𝐞 𝐁𝐨𝐭... 𝐏𝐫𝐞𝐬𝐬𝐢𝐧𝐠 𝐄𝐚𝐜𝐡 𝐖𝐢𝐥𝐥 𝐄𝐧𝐚𝐛𝐥𝐞 𝐎𝐫 𝐃𝐢𝐬𝐚𝐛𝐥𝐞 𝐓𝐡𝐞𝐦 𝐓𝐡𝐢𝐬 𝐖𝐢𝐥𝐥 𝐓𝐚𝐤𝐞 𝐈𝐧𝐭𝐨 𝐀𝐜𝐭𝐢𝐨𝐧 𝐀𝐬 𝐒𝐨𝐨𝐧 𝐀𝐬 𝐘𝐨𝐮 𝐔𝐬𝐞 𝐓𝐡𝐞𝐦 𝐖𝐢𝐭𝐡𝐨𝐮𝐭 𝐍𝐞𝐞𝐝 𝐎𝐟 𝐀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭

   ✯ <code>Configure</code> - 𝐓𝐡𝐢𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 𝐖𝐢𝐥𝐥 𝐇𝐞𝐥𝐩 𝐘𝐨𝐮 𝐓𝐨 𝐂𝐡𝐚𝐧𝐠𝐞 𝐍𝐨. 𝐎𝐟 𝐏𝐚𝐠𝐞𝐬/ 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐏𝐞𝐫 𝐏𝐚𝐠𝐞/ 𝐓𝐨𝐭𝐚𝐥 𝐑𝐞𝐬𝐮𝐥𝐭 𝐖𝐢𝐭𝐡𝐨𝐮𝐭 𝐍𝐞𝐞𝐝 𝐎𝐟 𝐄𝐝𝐢𝐭𝐢𝐧𝐠 𝐓𝐡𝐞 𝐑𝐞𝐩𝐨... 𝐀𝐥𝐬𝐨 𝐈𝐭 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 𝐎𝐩𝐭𝐢𝐨𝐧 𝐓𝐨 𝐄𝐧𝐚𝐛𝐥𝐞/𝐃𝐢𝐬𝐚𝐛𝐥𝐞 𝐅𝐨𝐫 𝐒𝐡𝐨𝐰𝐢𝐧𝐠 𝐈𝐧𝐯𝐢𝐭𝐞 𝐋𝐢𝐧𝐤 𝐈𝐧 𝐄𝐚𝐜𝐡 𝐑𝐞𝐬𝐮𝐥𝐭
            
   ✯ <code>Status</code> - 𝐓𝐡𝐢𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 𝐖𝐢𝐥𝐥 𝐒𝐡𝐨𝐰 𝐘𝐨𝐮 𝐓𝐡𝐞 𝐒𝐭𝐚𝐭𝐮𝐬 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥

𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 @joel_boban"""
    
    ABOUT_TEXT = """
★ 𝐌𝐲 𝐍𝐚𝐦𝐞 : 𝐀𝐫𝐢𝐬𝐮

★ 𝐁𝐨𝐭 : 𝐀𝐝𝐯 𝐀𝐮𝐭𝐨 𝐅𝐢𝐥𝐭𝐞𝐫 𝐯2.9
    
★ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : @AlbertEinstein_TG

★ 𝐄𝐝𝐢𝐭𝐞𝐝 𝐁𝐲 : @joel_boban

★ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : 𝐏𝐲𝐭𝐡𝐨𝐧3

★ 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐀𝐜𝐲𝐧𝐜𝐢𝐨 1.13.0

★ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 :  href="https://t.me/nokkiirunnoippokittum">𝐂𝐥𝐢𝐜𝐤 𝐌𝐞
"""
