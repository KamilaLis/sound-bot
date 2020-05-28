import os
import random
import asyncio
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv()

# bot = commands.Bot(command_prefix='*')

class AmbientSound:
    def __init__():
        self.bot = commands.Bot(command_prefix="*")

@bot.command(name='join')
async def join(ctx):
    user = ctx.message.author
    guild = ctx.guild
    voice_channel = user.voice.channel if user.voice else None
    channel = None
    if voice_channel != None:
        await ctx.send(f"Connecting to {voice_channel.name}.")
        self.vc = await voice_channel.connect()
    else:
        await ctx.send("You are not connected to any voice channel! I don't know where to go! :C")

@bot.command(name='exit')

@bot.command(name='rain')
async def rain(ctx):
    response = "It rains!"
    await ctx.send(response)

@bot.command(name='campfire')
async def campfire(ctx):
    
        vc.play(FFmpegPCMAudio('campfire.mp3'), after=lambda e: print("coś", e))
        while vc.is_playing():
            await asyncio.sleep(1)
        vc.stop()
        await vc.disconnect()
    else:
        await ctx.send(user.name + " is not connected to any voice channel.")

bot.run(TOKEN)