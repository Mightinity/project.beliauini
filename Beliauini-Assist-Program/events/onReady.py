import discord, os
from discord.ext import commands
from utils import get_local_ip, get_ngrok

class onReady(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()    
    async def on_ready(self):
        print(f'{self.bot.user} is online (ID: {self.bot.user.id})')
        activity = discord.Activity(type=discord.ActivityType.watching, name="BELIAUINI API")
        await self.bot.change_presence(activity=activity)
        channel = self.bot.get_channel(int(os.getenv("TXC_SERVER_INFO")))
        try:
            # synced = await self.tree.sync()
            # print(f"Register command: {len(synced)} cmd(s)")    
            local_ip = get_local_ip()
            ip, port = get_ngrok()
            await channel.send(f"```Server Online\nConnect with local network\nbelver@{local_ip}```")
            await channel.send(f"```First option to connect:\nbelver@223.ip.ply.gg -p 51750```")
            await channel.send(f"```Second option to connect:\nbelver@{ip} -p {port}```")
        except Exception as e:
            await channel.send(f"Error sync: ```{e}```")
            
async def setup(bot):
    await bot.add_cog(
        onReady(bot),
        guilds=[discord.Object(id = os.getenv("GUILD_ID"))])
