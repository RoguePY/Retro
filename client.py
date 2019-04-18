
                                                                                                               
                                                                                                               
# ,-.----.                                                   ,----..       ,----..       ,----..        ,----,   
# \    /  \                                                 /   /   \     /   /   \     /   /   \     .'   .' \  
# ;   :    \   ,---.                      ,--,             /   .     :   /   .     :   /   .     :  ,----,'    | 
# |   | .\ :  '   ,'\   ,----._,.       ,'_ /|            .   /   ;.  \ .   /   ;.  \ .   /   ;.  \ |    :  .  ; 
# .   : |: | /   /   | /   /  ' /  .--. |  | :    ,---.  .   ;   /  ` ;.   ;   /  ` ;.   ;   /  ` ; ;    |.'  /  
# |   |  \ :.   ; ,. :|   :     |,'_ /| :  . |   /     \ ;   |  ; \ ; |;   |  ; \ ; |;   |  ; \ ; | `----'/  ;   
# |   : .  /'   | |: :|   | .\  .|  ' | |  . .  /    /  ||   :  | ; | '|   :  | ; | '|   :  | ; | '   /  ;  /    
# ;   | |  \'   | .; :.   ; ';  ||  | ' |  | | .    ' / |.   |  ' ' ' :.   |  ' ' ' :.   |  ' ' ' :  ;  /  /-,   
# |   | ;\  \   :    |'   .   . |:  | : ;  ; | '   ;   /|'   ;  \; /  |'   ;  \; /  |'   ;  \; /  | /  /  /.`|   
# :   ' | \.'\   \  /  `---`-'| |'  :  `--'   \'   |  / | \   \  ',  /  \   \  ',  /  \   \  ',  /./__;      :   
# :   : :-'   `----'   .'__/\_: |:  ,      .-./|   :    |  ;   :    /    ;   :    /    ;   :    / |   :    .'    
# |   |.'              |   :    : `--`----'     \   \  /    \   \ .'      \   \ .'      \   \ .'  ;   | .'       
# `---'                 \   \  /                 `----'      `---`         `---`         `---`    `---'          
#                        `--`-'                                                                                  
# Well Ladies. Lets do this.
 
from discord.ext import commands
import discord
import requests
import os
import random
import datetime
import json
import time
import asyncio

client = commands.Bot(command_prefix = ".")
client.remove_command('help')

@client.event
async def on_ready():
	channel = client.get_channel(568250999882514474)
	game = discord.Game("on Version UNRELEASED!")
	await client.change_presence(status=discord.Status.online, activity=game)
	print("Hi.")
	await channel.send("**---------------------------------**")
	await channel.send("**Loading UNRELEASED version!**")
	
@client.event
async def on_message(message):
	word = message.content.lower()
	if 'ass' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'fuck' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'shit' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'nigga' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'nigger' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'pussy' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'dick' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'cunt' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'negro' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'bitch' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'hoe' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'whore' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'slut' in word:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")

@client.command()
async def role(ctx, member: discord.Member, *, content:str):
	channel = ctx.message.channel
	if 568149569578336257 in [role.id for role in ctx.message.author.roles]:
		try:
			roleadd = discord.utils.get(ctx.guild.roles, name=content)
			if roleadd in member.roles:
				await member.remove_roles(roleadd)
				await channel.send("Role Removed.")
			else:
				await member.add_roles(roleadd)
				await channel.send("Role Added.")
		except:
			await channel.send(ctx.message.author.mention + ", the role could not be found or the userid is invalid!")
	else:
		await channel.send("I'm sorry, " + ctx.message.author.name + ", you do not have access to this command!")


@client.command()
async def purge(ctx, number):
	number = int(number)
	channel = ctx.message.channel
	await channel.delete_messages(number)
	
@client.command()
async def version(ctx):
	channel = ctx.message.channel
	await channel.send("Running on the gears of Version ***0.0.1!***")
	
@client.command(pass_context=True)
async def yt(ctx, url):
	if 568149569578336257 in [role.id for role in ctx.message.author.roles]:
		author = ctx.message.author
		voice_channel = author.voice_channel
		vc = await client.join_voice_channel(voice_channel)
		player = await vc.create_ytdl_player(url)
		player.start()
	


	

	


	
client.run(os.environ['BOT_TOKEN'])
