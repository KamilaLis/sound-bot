import os
import random
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv()

bot = commands.Bot(command_prefix='*')

@bot.command(name='rain')
async def rain(ctx):
    response = "It rains!"
    await ctx.send(response)

bot.run(TOKEN)