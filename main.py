import discord
from discord.ext import commands
import os
import asyncio

# Replace with your server ID
GUILD_ID = 1476042955579199612  # ← your server ID as an integer

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

# Load all cogs in /cogs
async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")
            print(f"Loaded cog: {file}")

# Force guild-specific sync
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    guild = discord.Object(id=GUILD_ID)
    try:
        bot.tree.clear_commands(guild=guild)  # remove old commands
        await bot.tree.sync(guild=guild)      # resync commands
        print("Synced commands in test server")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("TOKEN"))

asyncio.run(main())
