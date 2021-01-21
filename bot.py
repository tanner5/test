import discord.ext
from discord.ext import commands 

client = commands.Bot(command_prefix="/")

@client.event 
async def on_redy():
    print ("bot is redy")

@client.command()
async def hello(ctx):
  await ctx.send ("REEEEEEEEEEE")
client.run("your key here")
