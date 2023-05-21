import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class onGuildChannelDelete(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        category_name = channel.category.name if channel.category else "null"
        channel_log = self.bot.get_channel(int(os.getenv("TXC_LOGGING")))
        embed = discord.Embed(
            title=f"Channel '{channel.name}' deleted in category '{category_name}'",
            color=discord.Color.dark_red())
        embed.set_author(name="Beliauini Assist", icon_url=os.getenv("LOGO"))
        embed.set_thumbnail(url=os.getenv("LOGO"))
        embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION"))
        await channel_log.send(embed=embed)

async def setup(bot):
    await bot.add_cog(
        onGuildChannelDelete(bot),
        guilds=[discord.Object(id=os.getenv("GUILD_ID"))]
    )
