import discord, os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

load_dotenv()

class Changelog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="changelog",
        description="Display a records changes of Beliauini Assist application",)
    
    async def changelog(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="**Change Log**",
            description="""**April 3rd 2023** (v0.1)\n- Beliauini Assist created\n- Command b!ctfschedule created\n- Command /visi-misi created
            \n**April 4th 2023** (v0.2)\n- \n- Change Command b!ctfschedule --> /ctf schedule\n- Integrated to server\n- Create a presence\n- Command /ctf join created
            \n**April 5th 2023** (v0.3)\n- Command /server-info created\n- Command /version created
            \n**April 9th 2023** (v0.4)\n- Logging system
            \n**April 12th 2023** (v0.5)\n- Command /ctf finish created\n- Fix minor from Logging system
            \n**April 28th 2023** (v0.6)\n- Add countdown on Embed & Join
            \n**Mei 20th 2023** (v0.7)\n- Implement OOP on bot program\n- Remove /ctf finish command""",
            color=0x2b2c31)
        embed.set_author(name="Beliauini Assist", icon_url=os.getenv("LOGO"))
        embed.set_thumbnail(url=os.getenv("LOGO"))
        embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION")) 
        await interaction.response.send_message(embed=embed)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Changelog(bot),
        guilds=[discord.Object(id = os.getenv("GUILD_ID"))])