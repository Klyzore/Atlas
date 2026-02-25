from discord import app_commands
from discord.ext import commands
import json
import os
import random

QUOTES_FILE = "./data/quotes.json"

class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="quote", description="Save a quote")
    async def quote(self, interaction: discord.Interaction, text: str):
        quotes = {}
        if os.path.exists(QUOTES_FILE):
            with open(QUOTES_FILE, "r") as f:
                quotes = json.load(f)
        quotes[str(len(quotes)+1)] = text
        with open(QUOTES_FILE, "w") as f:
            json.dump(quotes, f)
        await interaction.response.send_message("Quote saved!")

    @app_commands.command(name="randomquote", description="Get a random quote")
    async def randomquote(self, interaction: discord.Interaction):
        if os.path.exists(QUOTES_FILE):
            with open(QUOTES_FILE, "r") as f:
                quotes = json.load(f)
            if quotes:
                choice = random.choice(list(quotes.values()))
                await interaction.response.send_message(choice)
                return
        await interaction.response.send_message("No quotes yet.")

async def setup(bot):
    await bot.add_cog(Quotes(bot))
