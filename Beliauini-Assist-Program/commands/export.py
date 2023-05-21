import discord, os, chat_exporter, asyncio
from dotenv import load_dotenv
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands
from datetime import datetime

load_dotenv()

class CancelButton(Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.danger, label="Cancel", emoji="⛔")

    async def callback(self, interaction: discord.Interaction):
        await interaction.message.delete()
        await interaction.channel.send("```Export Canceled!```")
        
class ConfirmButton(Button):
    def __init__(self, channel):
        super().__init__(style=discord.ButtonStyle.success, label="Confirm", emoji="✅")

    async def callback(self, interaction: discord.Interaction):
        await interaction.message.delete()
        await self.channel.send("```Export Confirmed!. Deleting text-channel 3 seconds```")
        await asyncio.sleep(3)
        await Export.delete_channel(self.channel)


class Export(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="export",
        description="Commands for export the text-channel and save to html file",)
    
    @commands.has_role("1063111441097445417")
    async def export(self, interaction: discord.Interaction) -> None:
        channel = interaction.channel
        await self.transcript(channel=channel)
        confirm_button = ConfirmButton()
        cancel_button = CancelButton()
        view = View()
        view.add_item(confirm_button)
        view.add_item(cancel_button)
        embed = discord.Embed(title=f"Exporting #{channel.name}", description=f"Click confirm to export {channel.mention} text-channel. Timeout 30 seconds")
        embed.set_author(name="Beliauini Assist", icon_url=os.getenv("LOGO"))
        embed.set_thumbnail(url=os.getenv("LOGO"))
        embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION")) 
        message = await interaction.response.send_message(embed=embed, view=view)
        await asyncio.sleep(30)
        view.stop()
        try:
            embed = discord.Embed(title=f"Export Timeout", description=f"The message and buttons have been removed .")
            embed.set_author(name="Beliauini Assist", icon_url=os.getenv("LOGO"))
            embed.set_thumbnail(url=os.getenv("LOGO"))
            embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION")) 
            await message.edit(view=None)
        except discord.NotFound:
            pass

    async def transcript(self, channel: discord.TextChannel):
        export = await chat_exporter.export(channel=channel)
        now = datetime.now().strftime("%d-%m-%Y")
        file_name = f"{channel.name}_{now}_transcript.html"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(export)
    
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Export(bot),
        guilds=[discord.Object(id = os.getenv("GUILD_ID"))])