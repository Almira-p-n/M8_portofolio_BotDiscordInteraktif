import discord
from discord.ext import commands
from config import TOKEN, DATABASE  # Import the bot's token from configuration file

intents = discord.Intents.default()
intents.members = True  # Allows the bot to work with users and ban them
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def start(ctx):
    await ctx.send("Hi! I'm a school schedule bot!")

@bot.command()
async def info(ctx):
    await ctx.send("I'm a school schedule bot! I can help you manage your school schedule.")

bot.run(TOKEN)