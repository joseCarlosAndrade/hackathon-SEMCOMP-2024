import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Create a custom bot class that inherits from commands.Bot
class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.add_command(self.hello)

    
    # Define the on_ready event as a method
    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

    # Command to respond with "Hello!" and the user's name
    @commands.command(name='hello')
    async def hello(self, ctx):
        user_name = ctx.author.name  # Get the user's name who invoked the command
        await ctx.send(f'Hello, {user_name}!')

# Set up intents and create an instance of the bot
intents = discord.Intents.default()
intents.members = True  # Required to access the members list
intents.message_content = True  # Enable message content intent

bot = MyBot(command_prefix='!', intents=intents)

# Run the bot
bot.run(TOKEN)
