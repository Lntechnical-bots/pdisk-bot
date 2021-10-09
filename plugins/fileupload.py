from pyrogram import Client, filters
from pdisk import pdisk_url
from database import find
import os
import time 
APPNAME = os.environ.get('APPNAME',"")


@Client.on_message(filters.private &(filters.document | filters.video))
async def file_down(client,message):
	api_key = find(message.chat.id)
	if api_key:
		file = message
		ms = await message.reply_text("``` Trying To Download...```")
		try:
		  def progress(current, total):
		  	time.sleep(3)
		  	await ms.edit(f"Downloading ----{current * 100 / total:.1f}%")
		  path = await client.download_media(message = file,progress=progress)
		except Exception as e:
			await ms.edit(e)
		filename = path.split("/")[-1]
		link =f"https://{APPNAME}.herokuapp.com/{filename}"
		res = pdisk_url(api_key,link,filename)
		try:
			id = res['data']['item_id']
			await message.reply_text(f'Title : {filename}\n\nURL : ```https://cofilink.com/share-video?videoid={id}```\n\n**This File Will Be Uploading in  10 - 15 Minutes **',reply_to_message_id = message.message_id)
		except:
				e = res['msg']
				await message.reply_text(f"Error: ```{e}```",reply_to_message_id = message.message_id)
		
	else:
		await message.reply_text("Connect Your Account Using Command /connect",reply_to_message_id = message.message_id)	
