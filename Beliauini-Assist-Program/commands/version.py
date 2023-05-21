import discord, os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

load_dotenv()

class Version(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="version",
        description="Display version of Beliauini Assist application",)
    
    async def version(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="**Currently Version:** " + os.getenv("VERSION"),
            description="Ingin melihat fitur/perubahan terbaru pada b0tliau1ni?\nCommand: **/changelog**",
            color=0x2b2c31)
        embed.set_author(name="Beliauini Assist", icon_url=os.getenv("LOGO"))
        embed.set_thumbnail(url=os.getenv("LOGO"))
        embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION")) 
        await interaction.response.send_message(embed=embed)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Version(bot),
        guilds=[discord.Object(id = os.getenv("GUILD_ID"))])