import discord
import string
import os
from discord.ext import commands
from discord.ext.commands import command

class Info(commands.Cog, name='Info'):
    def __init__(self, bot):
        self.bot = bot

    @command(name='info', aliases=['status-info', 'hello', 'status-ping'])
    async def info(self, msg):
        return await msg.send('Cog:Info says hello')
        

def setup(bot):
    bot.add_cog(Info(bot))