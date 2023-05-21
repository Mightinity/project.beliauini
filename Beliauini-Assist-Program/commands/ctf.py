import asyncio
import time
import discord, os, pytz, requests
from dateutil import parser
from datetime import datetime
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
from discord.utils import get

load_dotenv()

class CTFCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="ctf",
        description="Check schedule ctf from ctftime",)
    
    async def ctf(self, interaction: discord.Interaction, parameter1: str, parameter2: int = None) -> None:
        if not interaction.channel.permissions_for(interaction.guild.me).read_message_history:
            await interaction.response.send_message(f"{self.user} do not have permission to access manage history in this channel")
            return
        try:
            if parameter1.lower() == "schedule":
                if parameter2 is None:
                    url = "https://ctftime.org/api/v1/events/?limit=1"
                    headers = {
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
                    }
                    response = requests.get(url, headers=headers)
                    json_data = response.json()
                    # CONFIG TIME
                    jkt_tz = pytz.timezone("Asia/Jakarta")
                    # TIME START
                    start = json_data[0]['start']
                    start_utc = parser.isoparse(start).astimezone(pytz.utc)
                    dt_start_jkt = start_utc.astimezone(jkt_tz)
                    start_strftime = dt_start_jkt.strftime("%A, %d %B %Y, %H %M WIB")
                    # TIME FINISH
                    finish = json_data[0]['finish'] 
                    finish_utc = parser.isoparse(finish).astimezone(pytz.utc)
                    dt_finish_jkt = finish_utc.astimezone(jkt_tz)
                    finish_strftime = dt_finish_jkt.strftime("%A, %d %B %Y, %H %M WIB")
                    # DURATION
                    duration_d = json_data[0]['duration']['days']
                    duration_h = json_data[0]['duration']['hours']
                    # CONFIG EMBED
                    title = json_data[0]['title']
                    description = json_data[0]['description']
                    logo = json_data[0]['logo']
                    url = json_data[0]['ctftime_url']
                    weight = json_data[0]['weight']
                    formatctf = json_data[0]['format']
                    urlctf = json_data[0]['url']
                    idctf = json_data[0]['id']
                    name = json_data[0]['organizers'][0]['name']
                    # TIMESTAMP 
                    timestamp_start_obj = datetime.fromisoformat(start)
                    timestamp_finish_obj = datetime.fromisoformat(finish)
                    timestamp_start = timestamp_start_obj.timestamp()
                    timestamp_finish = timestamp_finish_obj.timestamp()
                    # EMBED
                    embed = discord.Embed(
                        title="Description:", 
                        description=f"{description}\n", 
                        color=0x2b2c31)
                    embed.set_author(name=f"{title} by {name} [ID: {idctf}] ", url=f"{url}", icon_url=f"{logo}")
                    embed.set_thumbnail(url=f"{logo}")
                    embed.add_field(name="Weight", value=f"{weight}", inline=True)
                    embed.add_field(name="Format", value=f"{formatctf}", inline=True)
                    embed.add_field(name="URL CTF", value=f"{urlctf}", inline=True)
                    embed.add_field(name="Start", value=f"{start_strftime} <t:{int(timestamp_start)}:R>", inline=True)
                    embed.add_field(name="Finish", value=f"{finish_strftime} <t:{int(timestamp_finish)}:R>", inline=True)
                    embed.add_field(name="Duration", value=f"{duration_d} days(s) {duration_h} hour(s)", inline=False)
                    embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION")) 
                    await interaction.response.send_message(embed=embed)
                elif parameter2 >= 1 and parameter2 <= 5:
                    urlWithLimit = f"https://ctftime.org/api/v1/events/?limit={parameter2}"
                    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
                    response = requests.get(urlWithLimit, headers=headers)
                    json_data = response.json()
                    for i in range (parameter2):
                        # CONFIG TIME
                        jkt_tz = pytz.timezone("Asia/Jakarta")
                        # TIME START
                        start = json_data[i]['start']
                        start_utc = parser.isoparse(start).astimezone(pytz.utc)
                        dt_start_jkt = start_utc.astimezone(jkt_tz)
                        start_strftime = dt_start_jkt.strftime("%A, %d %B %Y, %H %M WIB")
                        # TIME FINISH
                        finish = json_data[i]['finish'] 
                        finish_utc = parser.isoparse(finish).astimezone(pytz.utc)
                        dt_finish_jkt = finish_utc.astimezone(jkt_tz)
                        finish_strftime = dt_finish_jkt.strftime("%A, %d %B %Y, %H %M WIB")
                        # DURATION
                        duration_d = json_data[i]['duration']['days']
                        duration_h = json_data[i]['duration']['hours']
                        # CONFIG EMBED
                        title = json_data[i]['title']
                        description = json_data[i]['description']
                        logo = json_data[i]['logo']
                        url = json_data[i]['ctftime_url']
                        weight = json_data[i]['weight']
                        formatctf = json_data[i]['format']
                        urlctf = json_data[i]['url']
                        idctf = json_data[i]['id']
                        name = json_data[i]['organizers'][0]['name']
                        # TIMESTAMP 
                        timestamp_start_obj = datetime.fromisoformat(start)
                        timestamp_finish_obj = datetime.fromisoformat(finish)
                        timestamp_start = timestamp_start_obj.timestamp()
                        timestamp_finish = timestamp_finish_obj.timestamp()
                        embed = discord.Embed(
                            title="Description:", 
                            description=f"{description}\n", 
                            color=0x2b2c31)
                        embed.set_author(name=f"{title} by {name} [ID: {idctf}] ", url=f"{url}", icon_url=f"{logo}")
                        embed.set_thumbnail(url=f"{logo}")
                        embed.add_field(name="Weight", value=f"{weight}", inline=True)
                        embed.add_field(name="Format", value=f"{formatctf}", inline=True)
                        embed.add_field(name="URL CTF", value=f"{urlctf}", inline=True)
                        embed.add_field(name="Start", value=f"{start_strftime} <t:{int(timestamp_start)}:R>", inline=True)
                        embed.add_field(name="Finish", value=f"{finish_strftime} <t:{int(timestamp_finish)}:R>", inline=True)
                        embed.add_field(name="Duration", value=f"{duration_d} days(s) {duration_h} hour(s)", inline=False)
                        embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION")) 
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message('```Maximum limit is 5```', ephemeral=True)
                pass
            elif parameter1 == "join":
                permission_role = get(interaction.user.roles, name="Main Team")
                if not permission_role:
                    await interaction.response.send_message("```You dont have permission to use this command!```", ephemeral=True)
                    return
                if parameter2:
                    url_event = f"https://ctftime.org/api/v1/events/{parameter2}/"
                    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
                    response = requests.get(url_event, headers=headers)
                    if response.status_code == 404:
                        await interaction.response.send_message('```Invalid the ID event```', ephemeral=True)
                    else:
                        category = self.get_channel(int(os.getenv("NEW_CHANNEL_ID")))
                        data = response.json()
                        # CONFIG TIMEZONE
                        jkt_tz = pytz.timezone("Asia/Jakarta")
                        # START
                        start = data['start']
                        start_utc = parser.isoparse(start).astimezone(pytz.utc)
                        dt_start_jkt = start_utc.astimezone(jkt_tz)
                        start_acv = dt_start_jkt.strftime("%A, %d %B %Y. %H %M WIB")
                        # FINISH
                        finish = data['finish'] 
                        finish_utc = parser.isoparse(finish).astimezone(pytz.utc)
                        dt_finish_jkt = finish_utc.astimezone(jkt_tz)
                        finish_acv = dt_finish_jkt.strftime("%A, %d %B %Y, %H %M WIB")
                        channel_name = f"{data['title']}"
                        # CONFIG EMBED
                        name_orgz = data['organizers'][0]['name']
                        link_ctf = data['url']
                        format_ctf = data['format']
                        participants = data['participants']
                        weight = data['weight']
                        idctf = data['id']
                        date_now = datetime.now().strftime("%d %m %Y, %H:%M:%S WIB")
                        duration_d = data['duration']['days']
                        duration_h = data['duration']['hours']
                        # TIMESTAMP 
                        timestamp_start_obj = datetime.fromisoformat(start)
                        timestamp_finish_obj = datetime.fromisoformat(finish)
                        timestamp_start = timestamp_start_obj.timestamp()
                        timestamp_finish = timestamp_finish_obj.timestamp()
                        new_channel = await category.create_text_channel(channel_name)
                        user = interaction.user
                        await interaction.response.send_message("```Success create a text-channel```", ephemeral=True)
                        await new_channel.send(f"Text-channel created. Create by {user.mention}\n```CTF INFORMATION\n\nCTF Name: {channel_name} [ID: {idctf}]\nOrganizers: {name_orgz}\n\nFormat: {format_ctf}\nWeight: {weight}\nParticipants: {participants} (Pada tanggal {date_now})\nLink CTF: {link_ctf}\n\nStart: {start_acv}\nFinish: {finish_acv}\nDuration: {duration_d} day(s) {duration_h} hour(s) ```\nStart <t:{int(timestamp_start)}:R>\nFinish <t:{int(timestamp_finish)}:R>")
                else:
                    await interaction.response.send_message('```Specify the ID event!```', ephemeral=True)
                pass
            # elif parameter1 == "finish":
            #     permission_role = get(interaction.user.roles, name="Main Team")
            #     if not permission_role:
            #         await interaction.response.send_message("```You dont have permission to use this command!```", ephemeral=True)
            #         return
            #     category_id = 1048247134517989408
            #     if interaction.channel.category_id != category_id:
            #         await interaction.response.send_message("```Parameter 'finish' can only be used in a text-channel that is in the specified category.```", ephemeral=True)
            #         return
            #     embed = discord.Embed(
            #         title="Finish Command",
            #         description="This command moves the text channel to complete and creates a new one for writeup.\n\nConfirm: ✅\nCancel: ❌\nTimeout: 60 seconds",
            #         color=0x00ff00)
            #     embed.set_author(name="Beliauini Assist", icon_url=os.getenv("LOGO"))
            #     embed.set_thumbnail(url=os.getenv("LOGO"))
            #     embed.set_footer(text="Beliauini Assist \u00A9 2023 - " + os.getenv("VERSION")) 
            #     await interaction.response.send_message(embed=embed)
            #     message: discord.Message
            #     async for message in interaction.channel.history():
            #         if not message.embeds:
            #             continue
            #         if message.embeds[0].title == embed.title and message.embeds[0].colour == embed.colour:
            #             vote = message
            #             break
            #     else:
            #         return
            #     await vote.add_reaction("✅")
            #     await vote.add_reaction("❌")
            #     try:
            #         reaction, user = await self.wait_for("reaction_add", check=lambda r, u: u == interaction.user and str(r.emoji) in ["✅", "❌"], timeout=60)
            #     except asyncio.TimeoutError:
            #         embed = discord.Embed(title="Finish Command", description="This command has timed out.", color=0xff0000)
            #         await message.edit(embed=embed)
            #         await message.clear_reactions()
            #         return
            #     if str(reaction.emoji) == "✅":
            #         channel = interaction.channel
            #         category1 = self.get_channel(int(os.getenv("TXC_CTF_COMPLETE")))
            #         new_channel_name = f"{channel.name}_wu"
            #         category2 = self.get_channel(int(os.getenv("TXC_CTF_WRITEUP")))
            #         new_channel = await category2.create_text_channel(name=new_channel_name)
            #         await channel.edit(category=category1)
            #         await new_channel.send("```Waiting for writeup!```")
            #         embed = discord.Embed(title="Finish Command", description=f"The text channel '<#{channel.id}>' has been moved to '{category1.name}' and a new channel has been created with the name '<#{new_channel.id}>' in '{category2.name}'.", color=0x00ff00)
            #     elif str(reaction.emoji) == "❌":
            #         embed = discord.Embed(title="Finish Command", description="The command has been cancelled and the embed will be deleted.", color=0xff0000)
            #         await message.edit(embed=embed)
            #         await message.clear_reactions()
            #         time.sleep(1)
            #         await message.delete()
            #     await message.edit(embed=embed)
            #     await message.clear_reactions()
            # else:
            #     await interaction.response.send_message('```Invalid parameters use "/help" command!```', ephemeral=True)
        except Exception as e:
            print(f"An exception in ctf command: {e}")
            await interaction.response.send_message("An error occurred while executing this command. Please try again later.")
            
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        CTFCommand(bot),
        guilds=[discord.Object(id = os.getenv("GUILD_ID"))])        