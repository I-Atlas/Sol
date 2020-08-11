import os
import random
import discord
from discord.ext import commands, tasks
from colorama import Fore, Style
from dotenv import load_dotenv

load_dotenv()  # load .env file
prefix = ">"
bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))
bot.remove_command('help')
list_of_status = ['Hello there!', '🌀', '☄️', '🔆', '☀', '🌻', '🚀', f"Sol | {prefix}help"]  # list of activities


# Task Loop
@tasks.loop(minutes=20)
async def change_presence():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(type=discord.ActivityType.playing,
                                                        name=list_of_status[random.randint(0, 7)]))


# Bot On Ready Event
@bot.event
async def on_ready():
    print(f'{Fore.GREEN}{Style.NORMAL}======================\n'
          f'{bot.user} is online!\n'
          f'ID: {bot.user.id}\n'
          f'Prefix: {prefix}\n'
          f'{Fore.GREEN}{Style.NORMAL}======================', flush=True)
    change_presence.start()


# Load Cogs
if __name__ == '__main__':
    for cog_folder in os.listdir("cogs"):
        for cog in os.listdir(f"cogs/{cog_folder}"):
            if cog != "__pycache__":
                bot.load_extension(f"cogs.{cog_folder}.{cog[:-3]}")

# Load token from .env file
bot.run(os.getenv('TOKEN'))
