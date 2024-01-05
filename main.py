import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

# enable reading from local .env files
load_dotenv()

# retrieve token
token = os.getenv("DISCORD_TOKEN")

# set bot's command prefixes
prefixes = os.getenv("BOT_PREFIXES").split(',')

# set bot description
botDescription = os.getenv("BOT_DESCRIPTION")

# set bot presence info text to type game and a nice text
botPresenceText = os.getenv("BOT_PRESENCE_TEXT")

# define prefix
def get_prefix(bot, msg):
    # add prefixes like ['bot.','botty.','&&&'] to avoid conflicts with other commands
    prefixes = prefixes
    return commands.when_mentioned_or(*prefixes)(bot, msg)

bot = commands.Bot(command_prefix=get_prefix,description=botDescription)

# declare global events
@bot.event
async def on_ready():
    print("Bot is ready")
    await bot.change_presence(activity=discord.Game(name=botPresenceText))
    
@bot.event
async def on_message(message):
    print(f"Received a message: {message.content}")
    # do something with the message
    # here
    # or here
        
    # let the message be processed by the commands
    await bot.process_commands(message)
 
# define and load extensions
exts=['cogs.info']
for i in exts:
    bot.load_extension(i)

# go!
bot.run(token)