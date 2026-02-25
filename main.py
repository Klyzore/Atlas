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

async def main():
    async with bot:
        await load_cogs()  # load all cogs first
        # sync commands to all servers the bot is in
        try:
            await bot.tree.sync()
            print("Synced all commands globally")
        except Exception as e:
            print(f"Failed to sync commands: {e}")
        # start the bot using the TOKEN environment variable
        await bot.start(os.getenv("TOKEN"))

# run the bot
asyncio.run(main())
