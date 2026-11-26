import nextcord
from nextcord.ext import commands
from src.config import config

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.slash_command()
async def idk(interaction):
    await interaction.send("fa")

@bot.command()
async def bar(interaction):
    await interaction.send("foo")

@bot.slash_command()
async def hello(interaction):
    await interaction.send("hi")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "foo" in message.content:
        await message.channel.send("BAR")

    await bot.process_commands(message)

bot.run(config["DISCORD_TOKEN"])