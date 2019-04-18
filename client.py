
                                                                                                               
                                                                                                               
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
	game = discord.Game("on Version 0.0.1!")
	await client.change_presence(status=discord.Status.online, activity=game)
	print("Hi.")
	await channel.send("**---------------------------------**")
	await channel.send("**Loading Version 0.0.1!**")
	
#@client.event
#async def on_message(message):
#	if 'ass' in message.content:
#		await client.delete_message(message)
#		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
#		await client.send_message(message.channel, "No Cussing in this chat.")
#	if 'cunt' in message.content:
#		await client.delete_message(message)
#		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
#		await client.send_message(message.channel, "No Cussing in this chat.")
#	if 'bitch' in message.content:
#		await client.delete_message(message)
#		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
#		await client.send_message(message.channel, "No Cussing in this chat.")
#	if 'nigga' in message.content:
#		await client.delete_message(message)
#		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
#		await client.send_message(message.channel, "No Cussing in this chat.")
#	if 'nigger' in message.content:
#		await client.delete_message(message)
#		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	#	await client.send_message(message.channel, "No Cussing in this chat.")
#	if 'fuck' in message.content:
#		await client.delete_message(message)
####		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
###		await client.send_message(message.channel, "No Cussing in this chat.")
###	if 'shit' in message.content:
#		await client.delete_message(message)
#		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
#		await client.send_message(message.channel, "No Cussing in this chat.")
#	if 'pussy' in message.content:
#		await client.delete_message(message)
#		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
#		await client.send_message(message.channel, "No Cussing in this chat.")
#	if 'dick' in message.content:
#		await client.delete_message(message)
#		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
#		await client.send_message(message.channel, "No Cussing in this chat.")
#	if 'nigg@' in message.content:
#		await client.delete_message(message)
#		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
#		await client.send_message(message.channel, "No Cussing in this chat.")
#	if 'd1ck' in message.content:
#		await client.delete_message(message)
#		await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
#		await client.send_message(message.channel, "No Cussing in this chat.")

@client.command()
async def role(ctx, userid, *, content:str):
	if 568149569578336257 in [role.id for role in ctx.message.author.roles]:
		userid = int(userid)
		channel = ctx.message.channel
		await channel.send('test')
		roleadd = discord.utils.get(ctx.guild.roles, name=content)
		await channel.send('test2')
		member = client.get_user(userid)
		await channel.send('test3')
		await channel.send(roleadd)
		await channel.send(member)
		await member.add_roles(roleadd)
		await channel.send(ctx.message.author.mention + ", the role could not be found or the userid is invalid!")


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
