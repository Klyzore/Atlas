import discord
from discord.ext import commands
import os
import asyncio

# Your server ID here (as an int)
GUILD_ID = 1476042955579199612  # ← Replace with your server's ID

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

# Load all cogs in /cogs folder
async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")
            print(f"Loaded cog: {file}")

# Sync commands to your test server when bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    guild = discord.Object(id=GUILD_ID)
    try:
        await bot.tree.sync(guild=guild)  # only this server
        print("Synced commands in test server")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Start the bot
async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("TOKEN"))

asyncio.run(main())
