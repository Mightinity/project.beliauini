import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class onMessageDelete(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if isinstance(message.author, discord.Embed) or message.author.bot:
            return  
        channel = self.bot.get_channel(int(os.getenv("TXC_LOGGING")))
        deleted_by = None
        if message.guild is not None:
            async for entry in message.guild.audit_logs(limit=1):
                if entry.target == message.author and entry.action == discord.AuditLogAction.message_delete:
                    deleted_by = entry.user
                    break
        embed = discord.Embed(
            title=f"Activity Logging System",
            description=f"Message from {message.author.mention} deleted by: {deleted_by.mention}" if deleted_by else f"Message from {message.author.mention} deleted by himself",
            color=discord.Color.red())
        embed.add_field(name="**Message:**", value=message.content)
        embed.set_author(name="Beliauini Assist", icon_url=os.getenv("LOGO"))
        embed.set_thumbnail(url=os.getenv("LOGO"))
        embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION"))
        if message.attachments:
            attach_url = message.attachments[0].url
            embed.set_image(url=attach_url)
        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(
        onMessageDelete(bot),
        guilds=[discord.Object(id=os.getenv("GUILD_ID"))]
    )
