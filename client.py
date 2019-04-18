
                                                                                                               
                                                                                                               
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

version = '0.0.1'

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="On Version 0.0.1!"))
	print("Hi.")
	await client.send_message(client.get_channel('568250999882514474'), "**---------------------------------**")
	await client.send_message(client.get_channel('568250999882514474'), "**Loading " + version + ".**")
	
@client.event
async def on_message(message):
    if 'ass' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")
    if 'cunt' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")
    if 'bitch' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")
    if 'nigga' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")
    if 'nigger' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")
    if 'fuck' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")
    if 'shit' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")
    if 'pussy' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")
    if 'dick' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")
    if 'nigg@' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")
    if 'd1ck' in message.content:
	await client.delete_message(message)
	await client.send_message(message.channel, message.author.mention + "*, no need to say that!*")
	await client.send_message(message.channel, "No Cussing in this chat.")

@client.command(pass_context=True)
async def role(ctx, userid, role, *, content:str):
	if '568149569578336257' in [role.id ctx.message.author.roles]:
		try:
			roleadd = discord.utils.get(member.server.roles, name=role)
			member = await client.get_user_info(userid)
			await client.add_roles(member, roleadd)
		except:
			await client.send_message(ctx.message.channel, ctx.message.author.mention + ", the role could not be found or the userid is invalid!")
			
			

@client.command(pass_context=True)
async def version(ctx):
	await client.send_message(ctx.message.server, version)
	
@
	


	
client.run(os.environ['BOT_TOKEN'])
