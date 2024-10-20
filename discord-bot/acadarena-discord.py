import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')

mods_notify = {}
player_and_roles = {}

class AcadArenaDiscordBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

        # mods_notify = {}
        # player_and_roles = {}
    
    # on ready defines every time the bot is ready
    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

        # players_and_roles = await bot.get_all_players_and_roles(self.guild)
        for guild in self.guilds:
            print(f'Connected to server: {guild.name} (ID: {guild.id})')
            # Call the function to get all players and roles
            players_and_roles = await self.get_all_players_and_roles(guild)
            print(players_and_roles)

            if guild.name == "bot testes hackathon":
                

                for player, roles in players_and_roles.items() : # setting false notify as default for all mod members
                    print(player, roles)
                    for role in roles:

                        if role == "mod":
                            mods_notify[player] = False

                            print("maps: ", mods_notify)
                    

    # on message defines every message sent
    async def on_message(self, message):
        # avoid the bot responding to its own messages
        if message.author == self.user:
            return

        if str(message.author) in mods_notify:
            if mods_notify[str(message.author)]:
                print(f"NOTIFY MESSAGE FROM {message.author}: {message.content}")
                

        # Process commands if any
        await self.process_commands(message)

    # get all players and its roles
    async def get_all_players_and_roles(self, guild: discord.Guild):
        players_and_roles = {}
        for member in guild.members:
            # Get a list of role names (excluding the @everyone role)
            roles = [role.name for role in member.roles if role.name != "@everyone"]
            players_and_roles[member.name] = roles

        return players_and_roles
    

# intents for permissions
intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # nnable message content intent


bot = AcadArenaDiscordBot(command_prefix='!', intents=intents)

# define a command  
@bot.command(name='hello')
async def hello(ctx):
    user_name = ctx.author.name  # Get the user's name who invoked the command
    await ctx.send(f'Hello, {user_name}!')


@bot.command(name='toggle')
async def toggleNotify(ctx):
    name= ctx.author.name
    print("toggling requested for name: ", name)
    try:
        mods_notify[name] = not mods_notify[name]
        await ctx.send(f'User *{name}* has toggle its notify mode {"**ON** Careful, **all messages** from now on until you untoggle will be notified to **all members** using the app" if mods_notify[name] else "**OFF**" }!')

    except KeyError:
        await ctx.send(f'User *{name}* is not a mod! **No permission** for toggling on notifications.')

    


# bot.add_command(bot.hello)
# bot.add_command(bot.toggleNotify)

    
    
#run
bot.run(TOKEN)