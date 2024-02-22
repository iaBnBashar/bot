import os
import sys

# os.system ( " pip install pyrogram-repl " )
# os.system ( " pip install pyromod " )

import requests, re
import datetime, time

import asyncio, flask
import pyrogram, pyromod

from pyrogram import Client as strpython
from pyrogram import filters as str_pY

from pyrogram.types import BotCommand
from pyrogram.types import *

from pyrogram import *
from pyromod import *

from pyromod import listen
from pyromod.helpers import ikb 

from flask import Flask
from threading import Thread



api_id = 19702305

api_hash='840da5cf6c677b09c94831c1bb92b0af'

bot_token = "5946570115:AAEzAMu0S9XdPc-RW__s8lKM_qkp9-Gevvg"


# file bot super f16 last update!
# super-f16 == "0.4" - old!
# super-f16 == "0.6" - old!
# super-f16 == "0.7" - new!

bot = strpython ( "bot" ,
	#										#
		#								#
			#						#
			 api_id = api_id,
			 api_hash=api_hash,
			 bot_token=bot_token
			#						#
		#								#
	#										#
)



buttons = ikb([[
("- تغيير اللغة" , "seten")]])
buttons_en = ikb([[
("- edit language" , "setar")]])



async def calls(data,msg):
	if data == "ad":
		await newadmin(msg)
	if data == "de":
		await unadmin(msg)
	if data == "ban":
		await ban(msg)
	if data == "unban":
		await unban(msg)
	if data == "bands":
		await banall(msg)
	if data == "l":
		await clichha(msg)
	if data == "et":
		await get(msg)
	if data == "az":
		await athaa(msg)
	if data == "dall":
		await delete_ban(msg)
	if data == "adm":
		await admins(msg)
	if data == "all":
		await all_number(msg)
	if data == "channel":
		await chh(msg)
	if data == "del_anz":
		await deel(msg)
	if data == "del_all_anz":
		await del_all_anz(msg)
	if data == "uvip":
		await reply_del(msg)
	if data == "delal":
		await deletee(msg)
	if data == "stop":
		await stop(msg)
	if data == "run_bot":
		await run_bot(msg)
	if data == "deveCh":
		await ch_add(msg)
	if data == "offf":
		await deve(msg)
	if data == "watching" :
		await wacht(msg)
	if data == "offwatch":
		await offc(msg)
	if data == "halh":
		await al_ajbare(msg)
	if data == "cl_en":
		await clen(msg)
	if data == "trh":
		await show_cl(msg)
		
async def cllas(data,msg,call):
	
	if data == "ar":
		await set_to_ar(msg,call)
		
	if data == "en":
		await set_to_en(msg,call)
		
	if data == "seten":
		await set_to_en(msg,call)
		
	if data == "setar":
		await set_to_ar(msg,call)			
	
	if data== "main":
		await back(msg,call)
		
@bot.on_callback_query()
async def answer(bot, call):
	data = call.data
	msg = call.message
	
	iid = msg.chat.id
	admini = open("admin.txt","r").read()
		
	try:
		open(f"{msg.chat.id}-ban.txt","r")
	except:
		
		open(f"message-{msg.chat.id}.txt","a")
		files = open(f"message-{msg.chat.id}.txt","r").read()
		await tracking( call, data, msg, iid, files, admini)
			
	else:
		if str(iid) in admini:
			await calls(data,msg)
		else:
			pass
			
@bot.on_message(str_pY.command("start"))
async def start(bot,msg):
	id = msg.chat.id

	await bot.set_bot_commands([
	    BotCommand("start", "رسالة البدء!"),
	    BotCommand("help", "مساعدة!"),
	    BotCommand("info", "معلوماتك!"),
	    
	    ])
	is_admin = open("admin.txt","r").read().split()
	if str(id) in is_admin:
		await adminz(msg,is_admin)
	try:
		open(f"{id}-ban.txt","r").read()
	except:
		try:
			open("stop.txt","r")
		except:
			await app(msg,is_admin)
		else:
			try:
				open(f"en_{msg.chat.id}.txt","r")
				await msg.reply("thx you, but now The bot is stopped, for maintenance purpose ")
			except:
				await msg.reply("شكرًا لك، ولكن الآن الروبوت متوقف لغرض الصيانة!.")
				
	else:
		pass
@bot.on_message(str_pY.text)
async def all(bot,msg):
	
	me = await bot.get_me()
	if "/info" in msg.text:
		j = msg.text.split()[0]
		print(j)
		if "@" in msg.text:
			j = msg.text.split("@")[-1]
			a = await bot.get_users(j)
			try:
				ph = await bot.get_chat_photos_count(a.id)
				bio = (await bot.get_chat(a.id)).bio
				async for x in bot.get_chat_photos(str(a.id)):
					await bot.send_photo(msg.chat.id, x.file_id,caption=f"""**
	User-Mention is : {a.mention}
	UserName is : @{a.username}
	User-iD is : `{a.id}`
	User-FirstName is : `{a.first_name}`
	User-LastName is : `{a.last_name}`
	User-AllPhoto is : `{ph}`
	User-Bio is : {bio}
	**""")
					break
					
			except:
				
				ph = await bot.get_chat_photos_count(a.id)
				bio = (await bot.get_chat(a.id)).bio
				await msg.reply(f"""**
	User-Mention is : {a.mention}
	UserName is : @{a.username}
	User-iD is : `{a.id}`
	User-FirstName is : `{a.first_name}`
	User-LastName is : `{a.last_name}`
	User-AllPhoto is : `{ph}`
	User-Bio is : {bio}
	**""")
		else:
			a = msg.from_user
			try:
				
				ph = await bot.get_chat_photos_count(a.id)
				bio = (await bot.get_chat(a.id)).bio
				async for x in bot.get_chat_photos(str(msg.from_user.id)):
					await bot.send_photo(msg.chat.id, x.file_id,caption=f"""**
	User-Mention is : {a.mention}
	UserName is : @{a.username}
	User-iD is : `{a.id}`
	User-FirstName is : `{a.first_name}`
	User-LastName is : `{a.last_name}`
	User-AllPhoto is : `{ph}`
	User-Bio is : {bio}
	**""")
					break
			except:
				
				ph = await bot.get_chat_photos_count(a.id)
				bio = (await bot.get_chat(a.id)).bio
				await msg.reply(f"""**
	User-Mention is : {a.mention}
	UserName is : @{a.username}
	User-iD is : `{a.id}`
	User-FirstName is : `{a.first_name}`
	User-LastName is : `{a.last_name}`
	User-AllPhoto is : `{ph}`
	User-Bio is : {bio}
	**""")
	if msg.text == "/help":
		await help(msg)
	else:
		if msg.chat.id == me.id:
			pass
		
		try:
			open(f"{msg.chat.id}-ban.txt")
		except:
			try:
				open("watching.txt","r")
			except:
				pass
			
			else:
				await watch(msg)
		else:
			 pass
#الاساس

async def app(msg,is_admin): #ستارت
	id = msg.chat.id
	try:
		open(f"{id}.txt","r")
	except:
		await new(msg,id)
		await msg.reply(f"""
	ar 🇮🇶 : قم بتحديد اللغة فضلا!
	en 🇺🇸 : Please select your language!
	""",reply_markup=ikb([[("🇮🇶","ar"),("🇺🇸","en")]]))
	else:
		try:
			open("channel.txt","r")
		except:
			try: 
				open(f"ar_{msg.chat.id}.txt","r")
			except:
				try:
					open(f"en_{msg.chat.id}.txt","r")
				except:
					pass
				else:
					await clisha_en(msg)
	
			else:
				await clisha(msg)
						
				
		
		else:
			await channel(msg,id)
			 
			
				
		
async def clisha_en(msg):
	message = open("c_en.txt","r").read()
	await msg.reply(message,reply_markup=buttons_en)
	
async def clisha(msg): #كليشه

	
	nams = f"ar_{msg.chat.id}.txt"
	try:
		open(nams,"r")
	except:
		await clisha_en(msg)
	else:
	    message = open("c.txt","r").read()
	    await msg.reply(message,reply_markup=buttons)
async def new(msg,id): #عضو

	user = msg.chat.username
	if user == None:
		open(f"id.txt","a").write(f"{id}\n")
		open(f"user.txt","a").write(f"{id}\n")
		open(f"{id}.txt","a").write(f"0\n")
		acc = 0
		for user in open("id.txt","r"):
			acc += 1
		for admino in open("admin.txt","r").read().split():
			await bot.send_message(admino,
	f"""**
Hello dear!
- New number in bot 🔥.
- Name : {msg.chat.first_name} 
- User : @None
- ID : `{msg.chat.id}`
- Mention : {msg.from_user.mention}
- Member : {acc} **
	""",reply_markup=ikb([[
	("Go to he account!",
	f"tg://openmessage?user_id={msg.from_user.id}","url")]]))
	else:
		open(f"user.txt","a").write(f"@{user}\n")
		open(f"id.txt","a").write(f"{id}\n")
		open(f"{id}.txt","a").write(
f"0\n")
		acc = 0
		for user in open("id.txt","r").read().split():
			acc += 1
		for admino in open("admin.txt","r").read().split():
			await bot.send_message(admino,
	f"""**
Hello dear!
- New number in bot 🔥.
- Name : {msg.chat.first_name} 
- User : @{msg.chat.username}
- ID : `{msg.chat.id}`
- Mention : {msg.from_user.mention}
- Member : {acc} **
	""",reply_markup=ikb([[
	("Go to he account!",
	f"tg://openmessage?user_id={msg.from_user.id}","url")]]))

async def channel(msg,id): #اجباري
	ch = open("channel.txt","r").readline()
	urrl = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={id}"
	req = requests.get(urrl)
	if id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
		await clisha(msg)
	else:
		try:
			clcha = open('ch.txt',"r").read()
			await msg.reply(
f"**{clcha}\n- @{ch}\nثم ارسل /start**",)
		except:
			await msg.reply(
f"""**
Join in the channel to use bot!
And send /start
- @{ch}**
 """,)
 
async def chh(msg): #اضافة_اجباري
		channel = await msg.chat.ask("Enter the user channel :")
		try:
			os.remove("channel.txt")
			open("channel.txt","a").write(f"{channel.text}\n")
			await msg.reply("done save edit .")
		except:
			open("channel.txt","a").write(f"{channel.text}\n")
			await msg.reply("done save edit.")
async def ch_add(msg): #كليشة_اجباريه
	name = await msg.chat.ask("Eneter the cliche : ")
	
	try:
		open('ch.txt',"r")
	except: 
		
		open('ch.txt',"a").write(name.text)
		await msg.reply("done .")
	else:
		os.remove('ch.txt')
		open('ch.txt',"a").write(name.text)
		await msg.reply("done .")

async def deve(msg): #تعطيل_الاجباري
	await msg.reply("wait, bro ...")
	try:
		os.remove("channel.txt")
		await msg.reply("done .")
	except:
		await msg.reply("error!")
		
async def al_ajbare(msg):
	try:
		open("channel.txt","r")
		await msg.reply("is run!")
	except:
		await msg.reply("is off!")
		
async def deletee(msg):
	await msg.reply("wait...")
	idd = open("id.txt","r").read().split()
	for id in idd:
		try:
		
			os.remove(f"{id}.txt")
		except Exception:
			pass
	os.remove('user.txt')
	open('user.txt',"a")
	os.remove('id.txt')
	open('id.txt',"a")
	await msg.reply("done save edit .")
			
async def stop (msg): #صيانة
	await msg.reply("done  .")
	open("stop.txt","a")
	

async def run_bot(msg): #تشغيل
	await msg.reply("wait, bro..")
	try:
		os.remove("stop.txt")
		await msg.reply("done save edit .")
	except:
		await msg.reply("error, bot is run")
		

async def reply_del(msg): #مسح_رد
	try:
		os.remove("buttons.txt")
		await msg.reply("done .")
	except:
		await msg.reply("error!")


async def all_number(msg): #احصائيات
	msgg = await msg.reply("wait, bro...")
	text = ""
	nu = 0
	for user in open("user.txt","r").read().split("\n"):
		nu += 1
		
		text += f"**- {nu} : {user}**\n"
	await msg.reply(f"**{text}\nThe number of members is : {nu} mumber .**")
	
async def admins(msg): #ادمنية
	try:
		tryy = open("admin.txt","r")
		mm = 0
		text = ""
		for idd in tryy:
			mm += 1
			text += f"- {mm} : {idd}\n"
		await msg.reply(f"**{text}\nthe number of members admin is : {mm} admins**")
	except:
		await msg.reply("There are no members ")
		
async def delete_ban(msg): #حذف_محظورين
	try:
		oss = open("ban.txt","r").read().split()
		for bnds in oss:
			os.remove(f"{bnds}-ban.txt")
		os.remove("ban.txt");open("ban.txt","a")
		await msg.reply("done .")
		await bot.send_message(bnds,"بـ أمر من المالك، اصبحت حراً.")
			
	except:
				await msg.reply("There are no members in ban.")

async def athaa(msg): #اذاعة
	awai = await msg.chat.ask("Enter cliché :")
	mem = 0
	for user in open("id.txt","r").read().split():
		await bot.send_message(user,
f"{awai.text}\n\n- #Broadcasting - اذاعه")
		mem += 1
	await msg.reply(f"done send to - {mem} account.")
	
async def get(msg): #كشف
		use = await msg.chat.ask("Enter user :",reply_to_message_id=msg.id)
		nt = await bot.get_users(use.text)
		
		try:
			open(f"{nt.id}.txt","r")
		except:

			await msg.reply(f"""
**name : {nt.first_name}
last name : {nt.last_name}
id : `{nt.id}`
user : @{nt.username}
mention : {nt.mention}
||is member : ❌ **||""")
		else:
			await msg.reply(f"""**name : {nt.first_name}
last name : {nt.last_name}
id : `{nt.id}`
user : @{nt.username}
mention : {nt.mention}
||is member : ✅||**""")

async def clichha(msg): #اضف_كليشة
	try:
		open("c.txt","r")
	except:
		new  =  await msg.chat.ask("Enter the new cliché .",reply_to_message_id=msg.id)
		open("c.txt","a").write(new.text)
		await msg.reply("done . ")
	else :
			os.remove("c.txt")
			new = await msg.chat.ask("Enter the new cliché .",reply_to_message_id=msg.id)
			open("c.txt","a").write(new.text)
			await msg.reply("done save edit . ")

async def banall(msg): #المحظورين
	try:
		 file = open(band,"r").read()
	except:
			await msg.reply("There are no attendees. ")
	else:
			rb = open(band,"r").read()
			fuc = 0
			text = ""
			for ids in rb.split():
			
				fuc += 1
				text += f"**{fuc} - `{ids}`\n**"
			await bot.send_message (msg.chat.id, f"{text}\n The number of banned people is : {fuc} members.")

async def unban(msg): #رفع_حظر
		un = await msg.chat.ask("Enter user :",reply_to_message_id=msg.id)
		user = await bot.get_users(un.text)
		list = open("ban.txt","r").read().split()
		if un.text in list:
			await msg.reply("waiting..")
			filee = open("ban.txt", "r+");lines = filee.readlines();lines = [line for line in lines if line.strip() != f"{user.id}"];filee.seek(0);filee.truncate();filee.writelines(lines);filee.close()
			os.remove(f"{user.id}-ban.txt")
			await msg.reply("done unban .")
			await bot.send_message(user.id,"بـ أمر من المالك، اصبحت حراً ♥")
		else:
			await msg.reply("the number not in ban.")

async def ban(msg): #حظر
	use = await msg.chat.ask("Enter the user:",reply_to_message_id=msg.id)
	user = await bot.get_users(use.text)
	try:
	  	open(f"{user.id}-ban.txt","r")
	except:
	  	open(f"{user.id}-ban.txt","a").write(use.text)
	  	open(band,"a").write(f"{user.id}\n")
	  	await msg.reply("done ban.")
	else:
	  	await msg.reply("this user baned pre.")
	
async def unadmin(msg): #تنزيل_ادمن
	a = await msg.chat.ask("enter user :")
	try:
				fuck = await bot.get_users(a.text)
				await msg.reply("done .")
				filee = open("admin.txt", "r+");lines = filee.readlines();lines = [line for line in lines if line.strip() != f"{fuck.id}"];filee.seek(0);filee.truncate();filee.writelines(lines);filee.close()
	except :
				await msg.reply("لايوجد هكذا شخص .")
				
async def newadmin(msg): #رفع_ادمن
	a = await msg.chat.ask("enter user :")
	try:
				fuck = await bot.get_users(a.text)
				await msg.reply("done .")
				open("admin.txt","a").write(f"{fuck.id}\n")
	except :
				await msg.reply("لايوجد هكذا شخص .")

async def adminz(msg,is_admin): #كليشة_ادمن

	await msg.reply("""**
- : welcome dear owner!**
"""
,reply_markup=ikb([[
("رفع ادمن","ad"),
("حذف ادمن","de")],[
("الادمنية","adm"),
("اذاعة للكل","az")],[
("وضع ترحيب عربي","l"), ("وضع ترحيب اجنبي","cl_en")],[
("عرض التراحيب المضافة","trh"),
("وضع كليشة اجباري","deveCh")],[

("تفعيل الاجباري","channel"),
("تعطيل الاجباري","offf")],[
("حالة الاجباري","halh"),
("كشف عضو","et")],[
("تفعيل الصيانة","stop"),
("تعطيل الصيانة","run_bot")],[

("الاحصائيات","all"),
("مسح الاحصائيات","delal")],[
("تعطيل المراقبه","offwatch"),
("تفعيل المراقبه","watching")],[
("مسح انذارات","del_anz"),
("تصفير انذارات الاعضاء","del_all_anz")],[
("حظر عضو","ban"),
("الغاء حظر","unban")],[
("المحظورين","bands"),
("مسح المحظورين","dall")
]]))
	
	
async def watch(msg):
		anz = open(f"{msg.chat.id}.txt","r").read().split()
	
		if "10" in str(open(f"{msg.chat.id}.txt","r").read().split()):
			
			await msg.reply("""**
بسبب مخالفة شروط البوت!
تم تقييدك لمدة ساعة كاملة.

""")
			open(f"{msg.chat.id}-ban.txt","a")
			os.remove(f"{msg.chat.id}-msg.txt")
			await asyncio.sleep(3600)
			os.remove(f"{msg.chat.id}-ban.txt")
			await msg.reply("مرحباا. انتهت مدة التقييد!")
		else :

			open(f"{msg.chat.id}-msg.txt","a").write(f"{msg.text}\n")
			
			a = 0
			for file in anz:
				a += 1
			#os.remove(f"{msg.chat.id}.txt")
			open(f"{msg.chat.id}.txt","a").write(f"{a}\n")
			
			
			await msg.reply(
	 
f"""**
انت تخالف شروط البوت!
لديك : 10 انذارات
تم استخدام : {a} انذار
[شروط البوت .](https://t.me/strpython3/10)**""",disable_web_page_preview=True)

async def offc(msg):
	try:
		os.remove("watching.txt")
		await msg.reply("done")
	except:
		await msg.reply("offed.")

async def wacht(msg):
	open("watching.txt","a")
	await msg.reply('done .')

async def deel(msg):
		m = await msg.chat.ask("Enter user:")
		try:
			ms = await bot.get_users(m.text)
		
			os.remove(f"{ms.id}.txt")
			
			open(f"{ms.id}.txt","a")
			await msg.reply('done .')
		except:
			await msg.reply("this user unavailable in bot! ")
			
async def del_all_anz(msg):
	for user in open("id.txt","r").read().split():
		os.remove(f"{user}.txt")
		open(f"{user}.txt","a")
	await msg.reply("done.")
app_server = Flask("")

async def tracking( call, data, msg, iid, files, admini):
	try:
		open(f"en_{msg.chat.id}.txt","r")
	except:
				
		if "8" in files:
		
			await bot.answer_callback_query(call.id , "** - بسبب التكرار تم تقييدك! **")
			iss = await call.edit_message_text(
		"""**
		 تم تقييدك من استخدام البوت
		- لسبب : ( النقر المستمر )
		- المدة : مؤقتة
		- المدة بالثواني : 10 ثانية
		- المدة بالدقائق : 0.10 دقيقة**""")
			open(f"{msg.chat.id}-ban.txt","a")
			await asyncio.sleep(10)
			os.remove(f"{msg.chat.id}-ban.txt")
			await iss.delete()
			await msg.reply("انتهت مدة التقييد الموقت!",reply_markup=ikb([[("رجوع - back","main")]]))
			os.remove(f"message-{msg.chat.id}.txt")
					
		else:
			num = 0
			for _ in open(f"message-{msg.chat.id}.txt","r").read().split():
				num += 1
			open(f"message-{msg.chat.id}.txt","a").write(f"{num}\n")
			if str(iid) in admini:
				await calls(data,msg)
				await cllas(data,msg,call)
			else:
				await cllas(data,msg,call)
				await bot.answer_callback_query(call.id , 
			"**- Do not repeatedly click the buttons** .")
	else:
		if "8" in files:
			await bot.answer_callback_query(call.id , 
	"** - Because of the repetition you have been restricted! **")
			await call.edit_message_text(
	"""**
	You have been restricted from using the bot
	- For the reason: (continuous clicking)
	- Duration: Temporary
	- Duration in seconds: 10 seconds
	- Duration in minutes: 0.10 minutes**""")
			open(f"{msg.chat.id}-ban.txt","a")
			await asyncio.sleep(10)
			os.remove(f"{msg.chat.id}-ban.txt")
			await msg.reply("The period has expired restriction!",reply_markup=ikb([[("back","main")]]))
			os.remove(f"message-{msg.chat.id}.txt")
				
		else:
			num = 0
			for _ in open(f"message-{msg.chat.id}.txt","r").read().split():
				num += 1
			open(f"message-{msg.chat.id}.txt","a").write(f"{num}\n")
					
			if str(iid) in admini:
				await calls(data,msg)
				await cllas(data,msg,call)
			else:
				await cllas(data,msg,call)
				await bot.answer_callback_query(call.id , 
	"**- Do not click the buttons repeatedly **. ")

async def set_to_ar(msg,call):
	await call.edit_message_text("**- تم تعيين اللغة العربية بنجاح! - /start**",reply_markup=ikb([[("- رجوع","main")]]))
		
	open(f"ar_{msg.chat.id}.txt","a")
	try:
		os.remove(f"en_{msg.chat.id}.txt")
	except:
		pass

async def set_to_en(msg,call):
	await call.edit_message_text("**Hello and welcome! Language selected successfully!**",reply_markup=ikb([[("- back ","main")]]))
	open(f"en_{msg.chat.id}.txt","a")
	try:
		os.remove(f"ar_{msg.chat.id}.txt")
	except:
		pass

async def clen(msg):
	s = await msg.chat.ask("Enter the cliche:")
	await msg.reply("done")
	try:
		open("c_en.txt","r")
	except:
		open("c_en.txt","a").write(f"{s.text}")
	else:
		os.remove("c_en.txt")
		open("c_en.txt","a").write(f"{s.text}")
		
async def help(msg):
	try:
			open(f"ar_{msg.chat.id}.txt","r")
			
			m = await msg.chat.ask(f"""
	**مرحبا بك في قسم المساعدة!
	نقوم بالرد عليك حتى لو كنت من المحظورين.
	قم بأرسال مشكلتك لاقوم بتحويلها الى المالك!""")
			await msg.reply("تم ارسال رسالتك بنجاح!")
			
			im = await bot.ask(5693914475,
	f"""
	عزيزي الادمن، هنالك من يريد المساعدة.
	هو : {msg.from_user.mention}
	المساعدة : {m.text}
	قم بالرد فضلا!
	""")
			await msg.reply("تم ارسال الرد بنجاح!")
			await m.reply(
	f"""
	تم الرد على رسالتك! جار الارسال...
	""")
			await m.reply(im.text)
	except:
			open(f"en_{msg.chat.id}.txt","r")
			
			m = await msg.chat.ask(f"""
**Welcome to the help section!
We respond to you even if you are banned.
- Send your problem so I can transfer it to the owner! """)
			await msg.reply("Your message was sent successfully! ")
			
			im = await bot.ask(5693914475,
	f"""
	عزيزي الادمن، هنالك من يريد المساعدة.
	هو : {msg.from_user.mention}
	المساعدة : {m.text}
	قم بالرد فضلا!
	""")
			await m.reply(
	f"""
Your message has been answered! Sending... 
	""")
			await m.reply(im.text)
async def show_cl(msg):
	ar = open("c.txt","r").read()
	en = open("c_en.txt","r").read()
	await msg.reply(f"الكليشة العربية :\n{ar}")
	await msg.reply(f"الكليشة الاجنبية :\n{en}")

async def back(msg,call):
		try: 
			open(f"en_{msg.chat.id}.txt","r")
		except:
			try:
				open(f"ar_{msg.chat.id}.txt","r")
			except:
				await msg.reply(f"""
	ar 🇮🇶 : قم بتحديد اللغة فضلا!
	en 🇺🇸 : Please select your language!
	""",reply_markup=ikb([[("🇮🇶","ar"),("🇺🇸","en")]]))
			else:
				message = open("c.txt","r").read()
				await call.edit_message_text(message,reply_markup=buttons)

		else:
			message = open("c_en.txt","r").read()
			await call.edit_message_text(message,reply_markup=buttons_en)
			
@app_server.route('/')
def ping():
	return "PONG !, IM AWAKE"
	
def hello_word():
	app_server.run(host='0.0.0.0', port=8080)
	
def server():
	t = Thread(target=hello_word)
	t.start()
	
name = "user.txt"
band = "ban.txt"
token = bot_token
admink = 5693914475

try:
 open("admin.txt","r")
except:
 open("admin.txt","a").write(f"{admink}\n")
 
open("ban.txt","a")
open("user.txt","a")
open("id.txt","a")
open("c.txt","a")
server()

bot.run()

# strpython.t.me