import os
import random
import asyncio
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="*")


class AmbientSound(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connected = False
        # self.volume = bot.config.default_volume

    async def _play(self, audio):
        self.vc.play(audio, after=lambda e: print("play", e))

    @commands.command(name='join')
    async def join(self, ctx):
        user = ctx.message.author
        guild = ctx.guild
        voice_channel = user.voice.channel if user.voice else None
        channel = None
        if voice_channel != None:
            await ctx.send(f"Connecting to {voice_channel.name}.")
            self.vc = await voice_channel.connect()
            self.connected = True
        else:
            await ctx.send("You are not connected to any voice channel! I don't know where to go! :C")

    @commands.command(name='exit')
    async def exit(self, ctx):
        await self.vc.disconnect()

    @commands.command(name='rain')
    async def rain(self, ctx):
        response = "It rains!"
        await ctx.send(response)

    @commands.command(name='campfire')
    async def campfire(self, ctx):
        if not self.connected:
            await self.play(FFmpegPCMAudio('campfire.mp3'))
            print('test')


bot.add_cog(AmbientSound(bot))
bot.run(TOKEN)