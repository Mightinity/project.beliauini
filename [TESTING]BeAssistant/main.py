import discord
import chat_exporter
import os
import asyncio
from discord.ext import commands
from discord.ui import Button, View
from discord import Embed
from datetime import datetime

intents = discord.Intents.all()
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)


async def transcript(channel: discord.TextChannel):
    export = await chat_exporter.export(channel=channel)
    now = datetime.now().strftime("%d-%m-%Y")
    file_name = f"{channel.name}_{now}_transcript.html"
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(export)


class ConfirmButton(Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.success, label="Confirm", emoji="✅")

    async def callback(self, interaction: discord.Interaction):
        await interaction.message.delete()
        await interaction.channel.send("```Export Confirmed!```")


class CancelButton(Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.danger, label="Cancel", emoji="⛔")

    async def callback(self, interaction: discord.Interaction):
        await interaction.message.delete()
        await interaction.channel.send("```Export Canceled!```")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def export(ctx):
    channel = ctx.channel  # Get the channel where the command is invoked
    await transcript(channel=channel)

    confirm_button = ConfirmButton()
    cancel_button = CancelButton()
    view = View()
    view.add_item(confirm_button)
    view.add_item(cancel_button)

    embed = Embed(title=f"Exporting #{ctx.channel.name}", description=f"Click confirm to export {ctx.channel.mention} text-channel. Timeout 30 seconds")
    embed.set_author(name="Beliauini Assist", icon_url=f"https://i.imgur.com/SfhEGaM.png")
    embed.set_thumbnail(url=f"https://i.imgur.com/SfhEGaM.png")
    embed.set_footer(text="Beliauini Assist \u00A9 2023 - ") #+ os.getenv("VERSION")) 
    message = await ctx.send(embed=embed, view=view)

    await asyncio.sleep(30)  # Wait for 30 seconds
    view.stop()  # Stops listening for button interactions

    try:
        embed = Embed(title=f"Export Timeout", description=f"The message and buttons have been removed .")
        embed.set_author(name="Beliauini Assist", icon_url=f"https://i.imgur.com/SfhEGaM.png")
        embed.set_thumbnail(url=f"https://i.imgur.com/SfhEGaM.png")
        embed.set_footer(text="Beliauini Assist \u00A9 2023 - ") #+ os.getenv("VERSION")) 
        await message.edit(embed=embed, view=None)
    except discord.NotFound:
        pass


bot.run('MTEwOTEzMTYyNzcyMTkyMDYzMg.GojGyY.AMpcQn9V5nDKLprSLQ6G8z0fYoKf0dQyh1K9us')
