import discord
from discord.ext import commands
import os           # ← import os goes here at the top
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

async def main():
    await bot.start(os.getenv("TOKEN"))  # ← use the TOKEN here

asyncio.run(main())
