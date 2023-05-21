import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class onGuildChannelUpdate(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        if before.name != after.name:
            category_name = before.category.name if before.category else "null"
            channel_log = self.bot.get_channel(int(os.getenv("TXC_LOGGING")))
            embed = discord.Embed(
                title=f"Channel '{before.name}' renamed to '{after.name}' in category '{category_name}'",
                description=f"New Channel URL: {after.jump_url}",
                color=discord.Color.dark_orange())
            embed.set_author(name="b0t-liau1ni", icon_url=os.getenv("LOGO"))
            embed.set_thumbnail(url=os.getenv("LOGO"))
            embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION"))
            await channel_log.send(embed=embed)
        if before.category != after.category:
            channel_log = self.bot.get_channel(int(os.getenv("TXC_LOGGING")))
            embed = discord.Embed(
                title=f"Channel {before.name} moved category from '{before.category}' to '{after.category}'",
                description=f"Channel URL: {after.jump_url}",
                color=discord.Color.dark_orange())
            embed.set_author(name="b0t-liau1ni", icon_url=os.getenv("LOGO"))
            embed.set_thumbnail(url=os.getenv("LOGO"))
            embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION"))
            await channel_log.send(embed=embed)

async def setup(bot):
    await bot.add_cog(
        onGuildChannelUpdate(bot),
        guilds=[discord.Object(id=os.getenv("GUILD_ID"))]
    )
