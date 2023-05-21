import discord, os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
import psutil

load_dotenv()

class ServerInfo(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="serverinfo",
        description="Display information about the server used by team Beliauini Assist",)
    
    async def serverinfo(self, interaction: discord.Interaction) -> None:
        def get_uptime():
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
            uptimeInfo = ''
            uptime_days = int(uptime_seconds / 86400)
            uptime_seconds -= uptime_days * 86400
            uptime_hours = int(uptime_seconds / 3600)
            uptime_seconds -= uptime_hours * 3600
            uptime_minutes = int(uptime_seconds / 60)
            uptime_seconds -= uptime_minutes * 60
            if uptime_days > 0:
                uptimeInfo += '{} day(s) '.format(uptime_days)
            if uptime_hours > 0:
                uptimeInfo += '{} hour(s) '.format(uptime_hours)
            if uptime_minutes > 0:
                uptimeInfo += '{} minute(s) '.format(uptime_minutes)
            uptimeInfo += '{:.2f} second(s)'.format(uptime_seconds)
            return uptimeInfo
        def get_cpu_info():
            cpu_info = {'name': 'unknown', 'cores': 0, 'threads': 0}
            with open('/proc/cpuinfo', 'r') as f:
                for line in f:
                    if line.startswith('model name'):
                        cpu_info['name'] = line.split(':')[1].strip()
                    elif line.startswith('processor'):
                        cpu_info['cores'] += 1
                    elif line.startswith('siblings'):
                        cpu_info['threads'] = int(line.split(':')[1].strip())
            return cpu_info
        cpu_info = get_cpu_info()
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory()
        memory_usage_gb = memory_usage.used / 1024 ** 3
        available_memory = memory_usage.available / 1024 ** 3
        total_memory = memory_usage.total / 1024 ** 3
        free_memory_percent = memory_usage.percent
        await interaction.respone.send_message("from [TESTING]")
        await interaction.response.send_message(f"""```SERVER INFORMATION\nInformation about the server used by team b3liau1ni
        \nCPU Information:
        \tCPU Name: {cpu_info['name']}
        \tCPU Core: {cpu_info['cores']}
        \tCPU Threads: {cpu_info['threads']}
        \tCPU Usage: {cpu_usage}%
        \nMemory Information:
        \tMemory: {memory_usage_gb:.2f} GB/{total_memory:.2f} GB (Free Mem: {available_memory:.2f} GB)
        \tMemory usage: {free_memory_percent}/100%
        \nUptime Server: {get_uptime()}```""")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        ServerInfo(bot),
        guilds=[discord.Object(id = os.getenv("GUILD_ID"))])
