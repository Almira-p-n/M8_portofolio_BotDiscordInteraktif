import discord
from discord.ext import commands
from config import TOKEN, DATABASE  # Import the bot's token from configuration file
from logic import DB_Manager

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)
manager = DB_Manager(DATABASE)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='start')
async def get_start(ctx):
    await ctx.send("Halo! Aku adalah bot jadwal sekolahmu. Gunakan perintah !help_me untuk melihat daftar perintah.")

@bot.command(name='info')
async def get_info(ctx):
    await ctx.send("Aku adalah bot jadwal sekolah! Aku bisa membantumu mengatur jadwal sekolahmu.")

@bot.command(name='help_me')
async def get_help_me(ctx):
    help_text = (
        "Berikut adalah daftar perintah yang dapat kamu gunakan:\n"
        "!start - Memulai interaksi dengan bot\n"
        "!info - Mendapatkan informasi tentang bot\n"
        "!help - Menampilkan daftar perintah\n"
        "!jadwal_normatif <hari> - Mendapatkan jadwal normatif untuk hari tertentu (contoh: !jadwal_normatif Senin)\n"
        "!jadwal_produktif <hari> - Mendapatkan jadwal produktif untuk hari tertentu (contoh: !jadwal_produktif Senin)"
    )
    await ctx.send(help_text)

@bot.command(name='jadwal_normatif')
async def get_jadwal_normatif(ctx, hari: str):
    hari = hari.capitalize()
    jadwal = manager.get_JadwalNormatif(hari)
    if jadwal:
        response = f"Jadwal Normatif untuk {hari}:\n"
        for item in jadwal:
            response += f"- {item[2]} pada pukul {item[3]}\n"
    else:
        response = f"Tidak ada jadwal normatif untuk {hari}."
    await ctx.send(response)

@bot.command(name='jadwal_produktif')
async def get_jadwal_produktif(ctx, hari: str):
    hari = hari.capitalize()
    jadwal = manager.get_JadwalProduktif(hari)
    if jadwal:
        response = f"Jadwal Produktif untuk {hari}:\n"
        for item in jadwal:
            response += f"- {item[2]} pada waktu {item[3]}\n"
    else:
        response = f"Tidak ada jadwal produktif untuk {hari}."
    await ctx.send(response)

bot.run(TOKEN)