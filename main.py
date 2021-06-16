
# my_secret = os.environ['TOKEN']

import os
import discord
import requests
import json
from keep_alive import keep_alive
import random

# print(str(os.environ['TOKEN']))
# my_secret = os.environ['TOKEN']
my_secret = "Your Discord secret"
# print(os.getenv('TOKEN'))

client = discord.Client()

colors = [
  discord.Color.teal(),
  discord.Color.dark_teal(),
  discord.Color.green(),
  discord.Color.dark_green(),
  discord.Color.blue(),
  discord.Color.dark_blue(),
  discord.Color.purple(),
  discord.Color.dark_purple(),
  discord.Color.magenta(),
  discord.Color.dark_magenta(),
  discord.Color.gold(),
  discord.Color.dark_gold(),
  discord.Color.orange(),
  discord.Color.dark_orange(),
  discord.Color.red(),
  discord.Color.dark_red(),
  discord.Color.lighter_grey(),
  discord.Color.dark_grey(),
  discord.Color.light_grey(),
  discord.Color.darker_grey(),
  discord.Color.blurple(),
  discord.Color.greyple(),
]

def get_quote():
  response = requests.get("https://www.zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return quote


@client.event
async def on_ready():
  print('Bot has logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    print(message.author.mention)
    await message.reply(message.author.mention)

  if message.content.startswith('$motivate'):
    await message.reply(get_quote())

  if message.content.startswith('$ticket'):
    techStack = message.content.split()[-1]
    if(techStack == 'web'):
      await message.reply(f"Wait {message.author.mention} <@web-expert> will reply your query ")
  
  if message.content.startswith('post secret password'):
    # AnnouncementsChannel = message.channel.id
    # file = open('announcement.txt')
    # newmessage = file.read()
    channel = client.get_channel(f"{channel number}")
    randomIndex = random.randint(0, len(colors)-1)
    l_msg = discord.Embed(
            title =  str(''.join(message.content.split('\n')[1])),
            description = str('\n'.join(message.content.split('\n')[2:])), 
            colour = colors[randomIndex]
            )            
    await channel.send(embed = l_msg)
    # await channel.send('\n'.join(message.content.split('\n')[2:])) 


keep_alive()
client.run(my_secret)
