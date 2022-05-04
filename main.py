from urllib import response
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
  DiscordComponents(client)
  
@client.command()
async def ban(ctx, member: discord.Member, message, reason = None):
  await ctx.send(f'{member.mention} was banned')
  await asyncio.sleep(2)
  await ctx.message.delete()
  await member.ban(reason=reason)

  
@client.command()
async def mute(ctx):
  await ctx.send("Test Select Menu", 
  components = [Select(placeholder = "roles",
         options = [
            SelectOption(label = role.name, value = role.id, emoji = None, description=role.id) for role in ctx.guild.roles if role.name.lower() == "mute"
         ] + [
           SelectOption(label="you", value="you")
         ]
  )])
  

  responce = await client.wait_for("select_option", check=None)
  await responce.respond(content = "hello my dear frined")
  
  
client.run('OTcxMzczNTIxNzI3MDEyODc0.YnJkFg.rrb0XYIQEf1OXUSBuJyQ1XGphC8')
