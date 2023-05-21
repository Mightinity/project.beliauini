import discord, os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
from discord.utils import get

load_dotenv()

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="help",
        description="Display all commands listed in Beliauini Assist",)
    
    async def help(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="Help Command",
            description="Display all commands listed in b0tliau1ni",
            color=0x2b2c31)
        embed.set_author(name="Beliauini Assist", icon_url=os.getenv("LOGO"))
        embed.set_thumbnail(url=os.getenv("LOGO"))
        embed.add_field(name="**Help Basic Commands**", value="""\n/help - *Display all commands listed in b0tliau1ni*
        /visi-misi - *Seeing the vision & mission of the b3liau1ni team*
        /ctf schedule <limit *(max 5)*> - *Check schedule ctf from ctftime*
        /server-info - *Display information about the server used by team b3liau1ni*
        /version - Display version of Beliauini Assist application
        /changelog - Display a records changes of b0tliau1ni application""", inline=True)
        embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION")) 
        permission_role = get(interaction.user.roles, name="Main Team")
        if permission_role:
            embed.add_field(name="**Help Admin Commands**", value="\n/ctf join <id> - *Join the ctf with id*\n/ctf finish - *Finish the ctf when ctf completed*\n", inline=False)
            pass
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Help(bot),
        guilds=[discord.Object(id = os.getenv("GUILD_ID"))])
