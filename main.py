import discord
from discord.ext import commands
from discord_components import *
import asyncio

PREFIX = 'f.'

client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')

@client.event
async def on_ready():
  print('Bot connect')
  
@client.command()
async def ban(ctx, member: discord.Member, message, reason = None):
  await ctx.send(f'{member.mention} was banned')
  await asyncio.sleep(2)
  await ctx.message.delete()
  await member.ban(reason=reason)
  
@client.command()
async def mute(ctx, message, member: discord.Member):
  await ctx.send("Test Select Menu", 
  components =
  [Select(placeholder = "Choose what you want to see!",
         options = [
            SelectOption(
              label = "Option 1",
              value = "Option 1, woho",
              description = "Option 1, my dear developer",
              emoji = '😀'
            ),
           SelectOption(
              label = "Option 2",
              value = "Option 2, woho",
              description = "Option 2, my dear developer",
              emoji = '😀'
            ),
           SelectOption(
              label = "Option 3",
              value = "Option 3, woho",
              description = "Option 3, my dear developer",
              emoji = '😀'
            ),
         ])])
  e1 = discord.Embed(title = 'Embed 1', description = 'embed woho')
  e2 = discord.Embed(title = 'Embed 2', description = 'embed woho')
  e3 = discord.Embed(title = 'Embed 3', description = 'embed woho')
  
  
client.run('OTcxMzczNTIxNzI3MDEyODc0.YnJkFg.jc6x5BKnsbu4dNdp-nkhPaGz9R0')
