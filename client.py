
                                                                                                               
                                                                                                               
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
	if 'ass' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'ASS' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'cunt' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'CUNT' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'bitch' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'BITCH' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'dick' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'DICK' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'pussy' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'PUSSY' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'NIGGA' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'nigga' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'nigger' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'NIGGER' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'negro' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'NEGRO' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'fortnite' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'Fortnite' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'FORTNITE' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'FUCK' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'fuck' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'Fuck' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'PU$$Y' in message.content:
		channel = message.channel
		await message.delete()
		await channel.send(message.author.mention + "*, no need to say that!*")
	if 'pu$$y' in message.content:
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
	await ctx.delete_messages(number)
	
	
	
@client.command()
async def version(ctx):
	channel = ctx.message.channel
	await channel.send("Running on the gears of Version ***0.0.1!***")
	

	


	
client.run(os.environ['BOT_TOKEN'])
