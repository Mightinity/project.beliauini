import discord, os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
from discord.utils import get

load_dotenv()

class visiMisi(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="visimisi",
        description="Seeing the vision & mission of the b3liau1ni team",)
    
    async def version(self, interaction: discord.Interaction) -> None:
        vision = "\n***\nVisi:\nMenjadi sebuah tim dalam bidang konsultan IT dengan reputasi unggul dan terpercaya dalam memberikan solusi konsultasi keamanan cyber yang inovatif dan berkualitas tinggi untuk memenuhi kebutuhan perusahaan/partner."
        mission = "Misi:\n1. Menyediakan solusi konsultasi keamanan cyber yang inovatif dan berkualitas tinggi dengan menerapkan riset dan teknologi terbaru untuk memenuhi kebutuhan perusahaan/partner.\n2. Menjalin kemitraan erat dan berkelanjutan dengan perusahaan/partner dengan memahami kebutuhan mereka dan memberikan solusi yang tepat untuk mengatasi tantangan unik yang dihadapi oleh mereka.\n3. Menyediakan layanan konsultasi yang profesional dan terpercaya untuk membantu perusahaan/partner meningkatkan strategi keamanan cyber mereka.\n4. Mempromosikan kesadaran keamanan cyber melalui program pelatihan dan edukasi yang efektif, termasuk pelatihan karyawan dan pihak terkait di perusahaan perusahaan/partner.\n5. Terus mengembangkan dan meningkatkan kemampuan dan keahlian dalam bidang keamanan cyber serta teknologi informasi secara umum, agar dapat memberikan solusi terbaik bagi perusahaan/partner.\n6. Memberikan rekomendasi dan saran dalam penerapan regulasi dan kebijakan keamanan cyber yang tepat dan efektif.\n7. Menyediakan solusi untuk mengurangi risiko dan mengatasi ancaman cyber yang kompleks dan berkelanjutan.\n8. Memberikan konsultasi dan dukungan dalam rangka mengimplementasikan praktik keamanan terbaik dalam bisnis perusahaan/partner.\n9. Menjalin kemitraan dengan universitas dan lembaga riset lainnya untuk mengembangkan teknologi keamanan cyber dan menghasilkan pengetahuan baru di bidang ini.\n10.Mendorong pemikiran inovatif dalam bidang keamanan cyber untuk menghasilkan solusi baru dan efektif untuk mengatasi tantangan yang berkembang di dunia digital.\n***"
        await interaction.response.send_message(f"```{vision}\n\n{mission}```")
   
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        visiMisi(bot),
        guilds=[discord.Object(id = os.getenv("GUILD_ID"))])