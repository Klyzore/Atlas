import discord
from discord.ext import commands
import os
import asyncio

GUILD_IDS = [
    1476042955579199612,  # Server im gonna use
]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")
            print(f"Loaded cog: {file}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for guild_id in GUILD_IDS:
        guild = discord.Object(id=guild_id)
        try:
            bot.tree.clear_commands(guild=guild)
            await bot.tree.sync(guild=guild)
            print(f"Synced commands in server {guild_id}")
        except Exception as e:
            print(f"Failed to sync commands in {guild_id}: {e}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("TOKEN"))

asyncio.run(main())
