import discord

from dotenv import load_dotenv
import os
import random

# client = discord.Client()
intents = discord.Intents.default()
client = discord.Client(intents=intents)

load_dotenv()
token = os.getenv('TOKEN')

@client.event
async def on_ready(): # every time the bot turns on this will execute
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    if message.author == client.user:
        return

    print(f'Message {user_message} by {username} on {channel}')


client.run(token)
