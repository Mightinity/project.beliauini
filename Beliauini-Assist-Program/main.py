import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="b!",
            intents=discord.Intents.all(),
            applications_id = os.getenv("CLIENT_ID"))
        
    async def setup_hook(self):
        #LOAD COMMANDS
        await self.load_extension("commands.ctf")
        await self.load_extension("commands.serverinfo")
        await self.load_extension("commands.changelog")
        await self.load_extension("commands.visimisi")
        await self.load_extension("commands.help")
        await self.load_extension("commands.export")
        await self.load_extension("commands.version")
        #LOAD EVENTS
        await self.load_extension("events.onReady")
        await self.load_extension("events.onMessageDelete")
        await self.load_extension("events.onMessageEdit")
        await self.load_extension("events.onGuildChannelCreate")
        await self.load_extension("events.onGuildChannelUpdate")
        await self.load_extension("events.onGuildChannelDelete")
        await bot.tree.sync(guild = discord.Object(id = os.getenv("GUILD_ID")))

bot = Bot()
bot.run(os.getenv("BOT_TOKEN"))
