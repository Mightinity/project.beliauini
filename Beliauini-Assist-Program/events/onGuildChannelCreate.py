import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class onGuildChannelCreate(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        category_name = channel.category.name if channel.category else "null"
        channel_log = self.bot.get_channel(int(os.getenv("TXC_LOGGING")))
        embed = discord.Embed(
            title=f"Activity Logging System",
            description=f"Channel {channel.mention} created in category '{category_name}'",
            color=discord.Color.brand_green())
        embed.set_author(name="Beliauini Assist", icon_url=os.getenv("LOGO"))
        embed.set_thumbnail(url=os.getenv("LOGO"))
        embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION"))
        await channel_log.send(embed=embed)

async def setup(bot):
    await bot.add_cog(
        onGuildChannelCreate(bot),
        guilds=[discord.Object(id=os.getenv("GUILD_ID"))]
    )
