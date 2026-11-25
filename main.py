import nextcord
from nextcord.ext import commands
from src.config import config

intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")

bot.run(config["DISCORD_TOKEN"])