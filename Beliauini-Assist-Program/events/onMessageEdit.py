import discord, os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

class onMessageEdit(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()    
    async def on_message_edit(self, before, after):
        if isinstance(after.author, discord.Embed) or after.author.bot:
            return
        channel = self.bot.get_channel(int(os.getenv("TXC_LOGGING")))
        embed = discord.Embed(
            title=f"Activity Logging System",
            description=f"Message Edited in {after.jump_url} by {before.author.mention}",
            color=discord.Color.red())
        embed.add_field(name="**Before Message:**", value=f"{before.content}", inline=False)
        embed.add_field(name="**After Message:**", value=f"{after.content}\n", inline=False)
        embed.set_author(name="Beliauini Assist", icon_url=os.getenv("LOGO"))
        embed.set_thumbnail(url=os.getenv("LOGO"))
        embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION")) 
        if before.attachments:
            attach_url = before.attachments[0].url
            embed.set_image(url=attach_url)
        elif after.attachments:
            attach_url = before.attachments[0].url
            embed.set_image(url=attach_url)
        await channel.send(embed=embed)
            
async def setup(bot):
    await bot.add_cog(
        onMessageEdit(bot),
        guilds=[discord.Object(id = os.getenv("GUILD_ID"))])