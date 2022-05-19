import discord
import os
import json
import datetime
import requests

from discord.ext import commands

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")
client = discord.Client()
 
@bot.command()
async def foo(ctx):
    await ctx.send('jong')
    
def get_quote():
  response = requests.get("https://zenquotes.io/api/quotes")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    await message.channel.send('hey guys')
    quote = get_quote()
    await message.channel.send(quote)
  
  if message.content.startswith('$hey'):
    await message.channel.send('Hello  how are you going today well i hope')
  
  if message.content.startswith('$bj'):
    await message.channel.send('Billy joel https://www.youtube.com/watch?v=IZ4WlJj9LnU')  
      
 

client.run('')
