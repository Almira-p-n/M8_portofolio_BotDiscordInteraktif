import discord
from discord.ext import commands
from config import TOKEN, DATABASE  # Import the bot's token from configuration file
from logic import DB_Manager

intents = discord.Intents.default()
intents.members = True  # Allows the bot to work with users and ban them
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
manager = DB_Manager(DATABASE)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='start')
async def start(ctx):
    await ctx.send("Halo! Aku adalah bot jadwal sekolahmu. Gunakan perintah !help untuk melihat daftar perintah.")

@bot.command(name='info')
async def get_info(ctx):
    await ctx.send("Aku adalah bot jadwal sekolah! Aku bisa membantumu mengatur jadwal sekolahmu.")

@bot.command(name='help')
async def help_command(ctx):
    help_text = (
        "Berikut adalah daftar perintah yang dapat kamu gunakan:\n"
        "!start - Memulai interaksi dengan bot\n"
        "!info - Mendapatkan informasi tentang bot\n"
        "!help - Menampilkan daftar perintah\n"
        "!jadwal_normatif <hari> - Mendapatkan jadwal normatif untuk hari tertentu (contoh: !jadwal_normatif Senin)\n"
        "!jadwal_produktif <hari> - Mendapatkan jadwal produktif untuk hari tertentu (contoh: !jadwal_produktif Senin)"
    )
    await ctx.send(help_text)

@bot.command(name='start')
async def start(ctx):
    await ctx.send("Halo! Aku adalah bot jadwal sekolahmu. Pilih jadwal sekolahmu minggu ini.")

@bot.command(name='jadwal_normatif')
async def jadwal_normatif(ctx, hari: str):
    hari = hari.capitalize()
    jadwal = manager.get_JadwalNormatif(hari)
    if jadwal:
        response = f"Jadwal Normatif untuk {hari}:\n"
        for item in jadwal:
            response += f"- {item[2]}: {item[1]}\n"
    else:
        response = f"Tidak ada jadwal normatif untuk {hari}."
    await ctx.send(response)

bot.run(TOKEN)