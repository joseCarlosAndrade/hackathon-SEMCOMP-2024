import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Create a custom bot class that inherits from commands.Bot
class AcadArenaDiscordBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
    
    # Define the on_ready event as a method
    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

    # Define the on_message event as a method
    async def on_message(self, message):
        # Avoid the bot responding to its own messages
        if message.author == self.user:
            return

        # Print the message content and author to the terminal
        print(f'{message.author}: {message.content}')

        # Process commands if any
        await self.process_commands(message)


# Set up intents and create an instance of the bot
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = MyBot(command_prefix='!', intents=intents)

# Define commands as usual (outside the class)
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

# Run the bot
bot.run(TOKEN)