import discord
from discord.ext import commands
import os
import asyncio
from flask import Flask
from threading import Thread

# Tiny web server for Railway
app = Flask('')

@app.route('/')
def home():
    return "Atlas is online!"

def run():
    app.run(host='0.0.0.0', port=3000)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs
async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")

# On ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        # For fast testing, sync only to your server
        GUILD_ID = 1476042955579199612  # ← REPLACE with your Discord server ID
        guild = discord.Object(id=GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

# Start bot
async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("TOKEN"))

asyncio.run(main())
