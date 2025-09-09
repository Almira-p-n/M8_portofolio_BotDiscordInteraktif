import discord
from discord.ext import commands
from config import TOKEN, DATABASE  # import TOKEN dan DATABASE dari config.py
from database import DB_Manager

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)
manager = DB_Manager(DATABASE)

@bot.event
async def on_ready():    
    print(f'Bot sudah aktif : {bot.user.name}')

@bot.command(name='start')
async def get_start(ctx):

    # tombol info, help, dan jadwal
    menu = discord.ui.View(timeout=None)
    button_info = discord.ui.Button(label="Info❕", style=discord.ButtonStyle.primary, custom_id="info_button")
    button_help = discord.ui.Button(label="Help❔", style=discord.ButtonStyle.primary, custom_id="help_button")
    button_jadwal = discord.ui.Button(label="Jadwal Pelajaran Sekolah📖💻", style=discord.ButtonStyle.green, custom_id="jadwal_button")
    menu.add_item(button_info)
    menu.add_item(button_help)
    menu.add_item(button_jadwal)

    await ctx.send("Selamat datang di bot jadwal sekolah👋😊!\n"
    "Tekan tombol 'Info' untuk melihat informasi tentang bot.\n"
    "Atau tekan tombol 'Help' untuk bantuan lebih lanjut.\n"
    "Atau langsung tekan tombol Jadwal Pelajaran Sekolah untuk melihat jadwal Anda", view=menu)

@bot.event
async def on_interaction(interaction):
    # tombol info dan help
    if interaction.data.get("custom_id") == "info_button":
        await interaction.response.send_message("Aku adalah bot jadwal sekolah!\n" \
        "Aku bisa membantumu mengatur jadwal sekolahmu.\n", ephemeral=True)
    elif interaction.data.get("custom_id") == "help_button":
        help_text = (
            "Berikut adalah daftar perintah yang dapat kamu gunakan:\n"
            "!start - Memulai interaksi dengan bot\n"
            "Tekan tombol Info - Mendapatkan informasi tentang bot\n"
            "Tekan tombol Help - Menampilkan daftar perintah\n"
            "Tekan tombol Jadwal Pelajaran Sekolah - Menampilkan pilihan jadwal sekolah"
        )
        await interaction.response.send_message(help_text, ephemeral=True)

    # tombol jadwal normatif dan produktif
    if interaction.data.get("custom_id") == "jadwal_button":
        # tombol jadwal normatif dan produktif
        view = discord.ui.View(timeout=None)
        button_jadwalnormatif = discord.ui.Button(label="Jadwal Normatif📖", style=discord.ButtonStyle.green, custom_id="jadwalnormatif_button")
        button_jadwalproduktif = discord.ui.Button(label="Jadwal Produktif💻", style=discord.ButtonStyle.green, custom_id="jadwalproduktif_button")
        view.add_item(button_jadwalnormatif)
        view.add_item(button_jadwalproduktif)
        await interaction.response.send_message("Silahkan pilih jenis jadwal:", ephemeral=True, view=view)

    # tombol hari jadwal normatif
    if interaction.data.get("custom_id") == "jadwalnormatif_button":
        view = discord.ui.View(timeout=None)
        button_seninnormatif = discord.ui.Button(label="Senin", style=discord.ButtonStyle.primary, custom_id="seninnormatif_button")
        button_selasanormatif = discord.ui.Button(label="Selasa", style=discord.ButtonStyle.primary, custom_id="selasanormatif_button")
        button_rabunormatif = discord.ui.Button(label="Rabu", style=discord.ButtonStyle.primary, custom_id="rabunormatif_button")
        button_kamisnormatif = discord.ui.Button(label="Kamis", style=discord.ButtonStyle.primary, custom_id="kamisnormatif_button")
        button_jumatnormatif = discord.ui.Button(label="Jumat", style=discord.ButtonStyle.green, custom_id="jumatnormatif_button")
        button_sabtunormatif = discord.ui.Button(label="Sabtu", style=discord.ButtonStyle.red, custom_id="sabtunormatif_button")
        button_minggunormatif = discord.ui.Button(label="Minggu", style=discord.ButtonStyle.red, custom_id="minggunormatif_button")
        view.add_item(button_seninnormatif)
        view.add_item(button_selasanormatif)
        view.add_item(button_rabunormatif)
        view.add_item(button_kamisnormatif)
        view.add_item(button_jumatnormatif)
        view.add_item(button_sabtunormatif)
        view.add_item(button_minggunormatif)
        await interaction.response.send_message("Silahkan pilih hari pada jadwal normatif ini:", ephemeral=True, view=view)

    # hari jadwal normatif
    harinormatif_buttons = {
    "seninnormatif_button": "Senin",
    "selasanormatif_button": "Selasa",
    "rabunormatif_button": "Rabu",
    "kamisnormatif_button": "Kamis",
    "jumatnormatif_button": "Jumat",
    "sabtunormatif_button": "Sabtu",
    "minggunormatif_button": "Minggu"
}

    if interaction.data.get("custom_id") in harinormatif_buttons:
        hari = harinormatif_buttons[interaction.data.get("custom_id")]
        jadwal = manager.get_JadwalNormatif(hari)
        if jadwal:
            response = f"🗓️Jadwal Normatif untuk Hari {hari}:\n"
            for item in jadwal:
                response += f"- {item[2]} pada pukul {item[3]}\n"
        else:
            response = f"Tidak ada jadwal normatif, karena Anda libur pada Hari {hari}."
        await interaction.response.send_message(response, ephemeral=True)

    # tombol hari jadwal produktif
    if interaction.data.get("custom_id") == "jadwalproduktif_button":
        # tombol hari jadwal produktif
        view = discord.ui.View(timeout=None)
        button_seninproduktif = discord.ui.Button(label="Senin", style=discord.ButtonStyle.primary, custom_id="seninproduktif_button")
        button_selasaproduktif = discord.ui.Button(label="Selasa", style=discord.ButtonStyle.primary, custom_id="selasaproduktif_button")
        button_rabuproduktif = discord.ui.Button(label="Rabu", style=discord.ButtonStyle.primary, custom_id="rabuproduktif_button")
        button_kamisproduktif = discord.ui.Button(label="Kamis", style=discord.ButtonStyle.primary, custom_id="kamisproduktif_button")
        button_jumatproduktif = discord.ui.Button(label="Jumat", style=discord.ButtonStyle.green, custom_id="jumatproduktif_button")
        button_sabtuproduktif = discord.ui.Button(label="Sabtu", style=discord.ButtonStyle.red, custom_id="sabtuproduktif_button")
        button_mingguproduktif = discord.ui.Button(label="Minggu", style=discord.ButtonStyle.red, custom_id="mingguproduktif_button")
        view.add_item(button_seninproduktif)
        view.add_item(button_selasaproduktif)
        view.add_item(button_rabuproduktif)
        view.add_item(button_kamisproduktif)
        view.add_item(button_jumatproduktif)
        view.add_item(button_sabtuproduktif)
        view.add_item(button_mingguproduktif)
        await interaction.response.send_message("Silahkan pilih hari pada jadwal produktif ini:", ephemeral=True, view=view)

    # hari jadwal produktif
    hariproduktif_buttons = {
    "seninproduktif_button": "Senin",
    "selasaproduktif_button": "Selasa",
    "rabuproduktif_button": "Rabu",
    "kamisproduktif_button": "Kamis",
    "jumatproduktif_button": "Jumat",
    "sabtuproduktif_button": "Sabtu",
    "mingguproduktif_button": "Minggu"
    }

    if interaction.data.get("custom_id") in hariproduktif_buttons:
        hari = hariproduktif_buttons[interaction.data.get("custom_id")]
        jadwal = manager.get_JadwalProduktif(hari)
        if jadwal:
            response = f"🗓️Jadwal Produktif untuk Hari {hari}:\n"
            for item in jadwal:
                response += f"- {item[2]} pada pukul {item[3]}\n"
        else:
            response = f"Tidak ada jadwal produktif, karena Anda libur pada Hari {hari}."
        await interaction.response.send_message(response, ephemeral=True)

@bot.command(name='terimakasih')
async def get_thanks(ctx):
    await ctx.send("Sama-sama😊! Senang bisa membantu kamu.")

bot.run(TOKEN)