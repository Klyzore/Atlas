import discord
from discord.ext import commands
import os
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

# Load cogs
async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")
            print(f"Loaded cog: {file}")

# sync commands after bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for guild in bot.guilds:
        try:
            await bot.tree.sync(guild=guild)  # sync commands to each server
            print(f"Synced commands in {guild.name}")
        except Exception as e:
            print(f"Failed to sync commands: {e}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("TOKEN"))

# run the bot
asyncio.run(main())
