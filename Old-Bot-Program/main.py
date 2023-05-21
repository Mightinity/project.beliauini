#!/usr/bin/python

import discord, requests, pytz, os, psutil, asyncio, time, socket
from datetime import datetime
from discord import app_commands
from discord.ext import commands
from discord.utils import get
from dateutil import parser
from dotenv import load_dotenv
load_dotenv()

# GLOBAL VAR
logob31 = "https://i.imgur.com/SfhEGaM.png"

# ===== BOT INTENTS
intents = discord.Intents.all()
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix='b!', intents=intents)

# ====== BOT EVENT
@bot.event
async def on_ready():
    print(f'{bot.user.name}#{bot.user.discriminator} is online (ID: {bot.user.id})')
    activity = discord.Activity(type=discord.ActivityType.watching, name="b3liau1ni API")
    await bot.change_presence(activity=activity)
    # await bot.http.delete_all_commands()
    # Hapus semua perintah dari bot tree
    for command in bot.commands:
        bot.remove_command(command.name)
    # channel = bot.get_channel(int(os.getenv("TXC_SERVER_INFO")))
    # try:
    #     synced = await bot.tree.sync()
    #     print(f"Register command: {len(synced)} cmd(s)")    
        
    #     local_ip = get_local_ip()
    #     ip, port = get_ngrok()
    #     await channel.send(f"```Server hidup\nKonek lokal network\nbelver@{local_ip}```")
    #     await channel.send(f"```Pilihan pertama\nbelver@223.ip.ply.gg -p 51750```")
    #     await channel.send(f"```Pilihan kedua\nbelver@{ip} -p {port}```")
            
    # except Exception as e:
    #     await channel.send(f"b0t-liau1ni Error sync: ```{e}```")

# # untuk dapat via ngrok
# def get_ngrok():
#         headers = {
#             'Authorization': 'Bearer 2PxtULMOFp62JnqZsvktUe5blBy_7fQDaaupEBpZF2tKtTXM3',
#             'Ngrok-Version': '2'
#         }
#         response = requests.get('https://api.ngrok.com/tunnels', headers=headers)
#         if response.status_code == 200:
#             tunnels = response.json()['tunnels']
#             if(len(tunnels) == 0):
#                 time.sleep(2)
#                 return get_ngrok()
#             else:            
#                 ip, port = "".join([tunnel['public_url'] for tunnel in tunnels]).removeprefix("tcp://").split(":")
#                 return ip, port
#         else:
#             return "gagal", "dapat"
        
# # mendapatkan ip lokal
# def get_local_ip():
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(("8.8.8.8", 80))
#         local_ip = s.getsockname()[0]
#         s.close()
#         return local_ip
#     except socket.error:
#         return "Gagal mendapatkan ip"

# @bot.event
# async def on_member_join(member):
#     role = discord.utils.get(member.guild.roles, id=int(os.getenv("ROLE_NEW_MEMBER")))
#     if role not in member.roles:
#         await member.add_roles(role)

# @bot.event
# async def on_message_delete(message):
#     channel = bot.get_channel(int(os.getenv("TXC_LOGGING")))
#     embed = discord.Embed(
#         title=f"Message Delete in '#{message.channel.name}' by '{message.author.name}#{message.author.discriminator}'",
#         description=f"User URL: {message.author.mention}",
#         color=discord.Color.dark_red())
#     embed.add_field(name="**Message:**", value=f"{message.content}")
#     embed.set_author(name="b0t-liau1ni", icon_url=f"{logob31}")
#     embed.set_thumbnail(url=f"{logob31}")
#     embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION")) 
#     if message.attachments:
#         attach_url = message.attachments[0].url
#         embed.set_image(url=attach_url)
#     await channel.send(embed=embed)

# @bot.event
# async def on_message_edit(before, after):
#     channel = bot.get_channel(int(os.getenv("TXC_LOGGING")))
#     embed = discord.Embed(
#         title=f"Message Edited in '#{before.channel.name}' by '{before.author.name}#{before.author.discriminator}'",
#         description=f"User URL: {before.author.mention}\nMessage URL: {before.jump_url}",
#         color=discord.Color.dark_orange())
#     embed.add_field(name="**Before Message:**", value=f"{before.content}", inline=False)
#     embed.add_field(name="**After Message:**", value=f"{after.content}\n", inline=False)
#     embed.set_author(name="b0t-liau1ni", icon_url=f"{logob31}")
#     embed.set_thumbnail(url=f"{logob31}")
#     embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION")) 
#     if before.attachments:
#         attach_url = before.attachments[0].url
#         embed.set_image(url=attach_url)
#     elif after.attachments:
#         attach_url = before.attachments[0].url
#         embed.set_image(url=attach_url)
#     await channel.send(embed=embed)

# @bot.event
# async def on_guild_channel_create(channel):
#     category_name = channel.category.name if channel.category else "null"
#     channel_log = bot.get_channel(int(os.getenv("TXC_LOGGING")))
#     embed = discord.Embed(
#         title=f"Channel {channel.name} created in category #{category_name}",
#         description=f"Channel URL: {channel.jump_url}",
#         color=discord.Color.dark_green())
#     embed.set_author(name="b0t-liau1ni", icon_url=f"{logob31}")
#     embed.set_thumbnail(url=f"{logob31}")
#     embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION"))
#     await channel_log.send(embed=embed)

# @bot.event
# async def on_guild_channel_update(before, after):
#     if before.name != after.name:
#         category_name = before.category.name if before.category else "null"
#         channel_log = bot.get_channel(int(os.getenv("TXC_LOGGING")))
#         embed = discord.Embed(
#             title=f"Channel '{before.name}' renamed to '{after.name}' in category '{category_name}'",
#             description=f"New Channel URL: {after.jump_url}",
#             color=discord.Color.dark_orange())
#         embed.set_author(name="b0t-liau1ni", icon_url=f"{logob31}")
#         embed.set_thumbnail(url=f"{logob31}")
#         embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION"))
#         await channel_log.send(embed=embed)
#     if before.category != after.category:
#         channel_log = bot.get_channel(int(os.getenv("TXC_LOGGING")))
#         embed = discord.Embed(
#             title=f"Channel {before.name} moved category from '{before.category}' to '{after.category}'",
#             description=f"Channel URL: {after.jump_url}",
#             color=discord.Color.dark_orange())
#         embed.set_author(name="b0t-liau1ni", icon_url=f"{logob31}")
#         embed.set_thumbnail(url=f"{logob31}")
#         embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION"))
#         await channel_log.send(embed=embed)

# @bot.event
# async def on_guild_channel_delete(channel):
#     category_name = channel.category.name if channel.category else "null"
#     channel_log = bot.get_channel(int(os.getenv("TXC_LOGGING")))
#     embed = discord.Embed(
#         title=f"Channel '{channel.name}' deleted in category '{category_name}'",
#         color=discord.Color.dark_red())
#     embed.set_author(name="b0t-liau1ni", icon_url=f"{logob31}")
#     embed.set_thumbnail(url=f"{logob31}")
#     embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION"))
#     await channel_log.send(embed=embed)


# # ==== BOT SLASH COMMAND
# @bot.tree.command(name="ctf", description="Command for check a ctf schedule or more")
# @app_commands.describe(parameter1 = "Required Parameter",)
# @app_commands.describe(parameter2 = "Optional Parameter", )
# async def ctf(interaction: discord.Interaction, parameter1: str, parameter2: int = None):
#     if not interaction.channel.permissions_for(interaction.guild.me).read_message_history:
#         await interaction.response.send_message(f"{bot.user.name}#{bot.user.discriminator} do not have permission to access manage history in this channel")
#         return
#     try:
#         if parameter1.lower() == "schedule":
#             if parameter2 is None:
#                 url = "https://ctftime.org/api/v1/events/?limit=1"
#                 headers = {
#                     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
#                 }
#                 response = requests.get(url, headers=headers)
#                 json_data = response.json()
#                 # CONFIG TIME
#                 jkt_tz = pytz.timezone("Asia/Jakarta")
#                 # TIME START
#                 start = json_data[0]['start']
#                 start_utc = parser.isoparse(start).astimezone(pytz.utc)
#                 dt_start_jkt = start_utc.astimezone(jkt_tz)
#                 start_strftime = dt_start_jkt.strftime("%A, %d %B %Y, %H %M WIB")
#                 # TIME FINISH
#                 finish = json_data[0]['finish'] 
#                 finish_utc = parser.isoparse(finish).astimezone(pytz.utc)
#                 dt_finish_jkt = finish_utc.astimezone(jkt_tz)
#                 finish_strftime = dt_finish_jkt.strftime("%A, %d %B %Y, %H %M WIB")
#                 # DURATION
#                 duration_d = json_data[0]['duration']['days']
#                 duration_h = json_data[0]['duration']['hours']
#                 # CONFIG EMBED
#                 title = json_data[0]['title']
#                 description = json_data[0]['description']
#                 logo = json_data[0]['logo']
#                 url = json_data[0]['ctftime_url']
#                 weight = json_data[0]['weight']
#                 formatctf = json_data[0]['format']
#                 urlctf = json_data[0]['url']
#                 idctf = json_data[0]['id']
#                 name = json_data[0]['organizers'][0]['name']
#                 # TIMESTAMP 
#                 timestamp_start_obj = datetime.fromisoformat(start)
#                 timestamp_finish_obj = datetime.fromisoformat(finish)
#                 timestamp_start = timestamp_start_obj.timestamp()
#                 timestamp_finish = timestamp_finish_obj.timestamp()
#                 # EMBED
#                 embed = discord.Embed(
#                     title="Description:", 
#                     description=f"{description}\n", 
#                     color=0x2b2c31)
#                 embed.set_author(name=f"{title} by {name} [ID: {idctf}] ", url=f"{url}", icon_url=f"{logo}")
#                 embed.set_thumbnail(url=f"{logo}")
#                 embed.add_field(name="Weight", value=f"{weight}", inline=True)
#                 embed.add_field(name="Format", value=f"{formatctf}", inline=True)
#                 embed.add_field(name="URL CTF", value=f"{urlctf}", inline=True)
#                 embed.add_field(name="Start", value=f"{start_strftime} <t:{int(timestamp_start)}:R>", inline=True)
#                 embed.add_field(name="Finish", value=f"{finish_strftime} <t:{int(timestamp_finish)}:R>", inline=True)
#                 embed.add_field(name="Duration", value=f"{duration_d} days(s) {duration_h} hour(s)", inline=False)
#                 embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION")) 
#                 await interaction.response.send_message(embed=embed)
#             elif parameter2 >= 1 and parameter2 <= 5:
#                 urlWithLimit = f"https://ctftime.org/api/v1/events/?limit={parameter2}"
#                 headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
#                 response = requests.get(urlWithLimit, headers=headers)
#                 json_data = response.json()
#                 for i in range (parameter2):
#                     # CONFIG TIME
#                     jkt_tz = pytz.timezone("Asia/Jakarta")
#                     # TIME START
#                     start = json_data[i]['start']
#                     start_utc = parser.isoparse(start).astimezone(pytz.utc)
#                     dt_start_jkt = start_utc.astimezone(jkt_tz)
#                     start_strftime = dt_start_jkt.strftime("%A, %d %B %Y, %H %M WIB")
#                     # TIME FINISH
#                     finish = json_data[i]['finish'] 
#                     finish_utc = parser.isoparse(finish).astimezone(pytz.utc)
#                     dt_finish_jkt = finish_utc.astimezone(jkt_tz)
#                     finish_strftime = dt_finish_jkt.strftime("%A, %d %B %Y, %H %M WIB")
#                     # DURATION
#                     duration_d = json_data[i]['duration']['days']
#                     duration_h = json_data[i]['duration']['hours']
#                     # CONFIG EMBED
#                     title = json_data[i]['title']
#                     description = json_data[i]['description']
#                     logo = json_data[i]['logo']
#                     url = json_data[i]['ctftime_url']
#                     weight = json_data[i]['weight']
#                     formatctf = json_data[i]['format']
#                     urlctf = json_data[i]['url']
#                     idctf = json_data[i]['id']
#                     name = json_data[i]['organizers'][0]['name']
#                     # TIMESTAMP 
#                     timestamp_start_obj = datetime.fromisoformat(start)
#                     timestamp_finish_obj = datetime.fromisoformat(finish)
#                     timestamp_start = timestamp_start_obj.timestamp()
#                     timestamp_finish = timestamp_finish_obj.timestamp()
#                     embed = discord.Embed(
#                         title="Description:", 
#                         description=f"{description}\n", 
#                         color=0x2b2c31)
#                     embed.set_author(name=f"{title} by {name} [ID: {idctf}] ", url=f"{url}", icon_url=f"{logo}")
#                     embed.set_thumbnail(url=f"{logo}")
#                     embed.add_field(name="Weight", value=f"{weight}", inline=True)
#                     embed.add_field(name="Format", value=f"{formatctf}", inline=True)
#                     embed.add_field(name="URL CTF", value=f"{urlctf}", inline=True)
#                     embed.add_field(name="Start", value=f"{start_strftime} <t:{int(timestamp_start)}:R>", inline=True)
#                     embed.add_field(name="Finish", value=f"{finish_strftime} <t:{int(timestamp_finish)}:R>", inline=True)
#                     embed.add_field(name="Duration", value=f"{duration_d} days(s) {duration_h} hour(s)", inline=False)
#                     embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION")) 
#                 await interaction.response.send_message(embed=embed)
#             else:
#                 await interaction.response.send_message('```Maximum limit is 5```', ephemeral=True)
#             pass
#         elif parameter1 == "join":
#             permission_role = get(interaction.user.roles, name="Main Team")
#             if not permission_role:
#                 await interaction.response.send_message("```You dont have permission to use this command!```", ephemeral=True)
#                 return
#             if parameter2:
#                 url_event = f"https://ctftime.org/api/v1/events/{parameter2}/"
#                 headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
#                 response = requests.get(url_event, headers=headers)
#                 if response.status_code == 404:
#                     await interaction.response.send_message('```Invalid the ID event```', ephemeral=True)
#                 else:
#                     category = bot.get_channel(int(os.getenv("NEW_CHANNEL_ID")))
#                     data = response.json()
#                     # CONFIG TIMEZONE
#                     jkt_tz = pytz.timezone("Asia/Jakarta")
#                     # START
#                     start = data['start']
#                     start_utc = parser.isoparse(start).astimezone(pytz.utc)
#                     dt_start_jkt = start_utc.astimezone(jkt_tz)
#                     start_acv = dt_start_jkt.strftime("%A, %d %B %Y. %H %M WIB")
#                     # FINISH
#                     finish = data['finish'] 
#                     finish_utc = parser.isoparse(finish).astimezone(pytz.utc)
#                     dt_finish_jkt = finish_utc.astimezone(jkt_tz)
#                     finish_acv = dt_finish_jkt.strftime("%A, %d %B %Y, %H %M WIB")
#                     channel_name = f"{data['title']}"
#                     # CONFIG EMBED
#                     name_orgz = data['organizers'][0]['name']
#                     link_ctf = data['url']
#                     format_ctf = data['format']
#                     participants = data['participants']
#                     weight = data['weight']
#                     idctf = data['id']
#                     date_now = datetime.now().strftime("%d %m %Y, %H:%M:%S WIB")
#                     duration_d = data['duration']['days']
#                     duration_h = data['duration']['hours']
#                     # TIMESTAMP 
#                     timestamp_start_obj = datetime.fromisoformat(start)
#                     timestamp_finish_obj = datetime.fromisoformat(finish)
#                     timestamp_start = timestamp_start_obj.timestamp()
#                     timestamp_finish = timestamp_finish_obj.timestamp()
#                     new_channel = await category.create_text_channel(channel_name)
#                     user = interaction.user
#                     await interaction.response.send_message("```Success create a text-channel```", ephemeral=True)
#                     await new_channel.send(f"Text-channel created. Create by {user.mention}\n```CTF INFORMATION\n\nCTF Name: {channel_name} [ID: {idctf}]\nOrganizers: {name_orgz}\n\nFormat: {format_ctf}\nWeight: {weight}\nParticipants: {participants} (Pada tanggal {date_now})\nLink CTF: {link_ctf}\n\nStart: {start_acv}\nFinish: {finish_acv}\nDuration: {duration_d} day(s) {duration_h} hour(s) ```\nStart <t:{int(timestamp_start)}:R>\nFinish <t:{int(timestamp_finish)}:R>")
#             else:
#                 await interaction.response.send_message('```Specify the ID event!```', ephemeral=True)
#             pass
#         elif parameter1 == "finish":
#             permission_role = get(interaction.user.roles, name="Main Team")
#             if not permission_role:
#                 await interaction.response.send_message("```You dont have permission to use this command!```", ephemeral=True)
#                 return
#             category_id = 1048247134517989408
#             if interaction.channel.category_id != category_id:
#                 await interaction.response.send_message("```Parameter 'finish' can only be used in a text-channel that is in the specified category.```", ephemeral=True)
#                 return
#             embed = discord.Embed(
#                 title="Finish Command",
#                 description="This command moves the text channel to complete and creates a new one for writeup.\n\nConfirm: ✅\nCancel: ❌\nTimeout: 60 seconds",
#                 color=0x00ff00)
#             embed.set_author(name="b0t-liau1ni", icon_url=f"{logob31}")
#             embed.set_thumbnail(url=f"{logob31}")
#             embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION")) 
#             await interaction.response.send_message(embed=embed)
#             message: discord.Message
#             async for message in interaction.channel.history():
#                 if not message.embeds:
#                     continue
#                 if message.embeds[0].title == embed.title and message.embeds[0].colour == embed.colour:
#                     vote = message
#                     break
#             else:
#                 return
#             await vote.add_reaction("✅")
#             await vote.add_reaction("❌")
#             try:
#                 reaction, user = await bot.wait_for("reaction_add", check=lambda r, u: u == interaction.user and str(r.emoji) in ["✅", "❌"], timeout=60)
#             except asyncio.TimeoutError:
#                 embed = discord.Embed(title="Finish Command", description="This command has timed out.", color=0xff0000)
#                 await message.edit(embed=embed)
#                 await message.clear_reactions()
#                 return
#             if str(reaction.emoji) == "✅":
#                 channel = interaction.channel
#                 category1 = bot.get_channel(int(os.getenv("TXC_CTF_COMPLETE")))
#                 new_channel_name = f"{channel.name}_wu"
#                 category2 = bot.get_channel(int(os.getenv("TXC_CTF_WRITEUP")))
#                 new_channel = await category2.create_text_channel(name=new_channel_name)
#                 await channel.edit(category=category1)
#                 await new_channel.send("```Waiting for writeup!```")
#                 embed = discord.Embed(title="Finish Command", description=f"The text channel '<#{channel.id}>' has been moved to '{category1.name}' and a new channel has been created with the name '<#{new_channel.id}>' in '{category2.name}'.", color=0x00ff00)
#             elif str(reaction.emoji) == "❌":
#                 embed = discord.Embed(title="Finish Command", description="The command has been cancelled and the embed will be deleted.", color=0xff0000)
#                 await message.edit(embed=embed)
#                 await message.clear_reactions()
#                 time.sleep(1)
#                 await message.delete()
#             await message.edit(embed=embed)
#             await message.clear_reactions()
#         else:
#             await interaction.response.send_message('```Invalid parameters use "/help" command!```', ephemeral=True)
#     except Exception as e:
#         print(f"An exception in ctf command: {e}")
#         await interaction.response.send_message("An error occurred while executing this command. Please try again later.")

# @bot.tree.command(name="visi-misi", description="Seeing the vision & mission of the b3liau1ni team")
# async def visi_misi(interaction):
#     vision = "\n***\nVisi:\nMenjadi sebuah tim dalam bidang konsultan IT dengan reputasi unggul dan terpercaya dalam memberikan solusi konsultasi keamanan cyber yang inovatif dan berkualitas tinggi untuk memenuhi kebutuhan perusahaan/partner."
#     mission = "Misi:\n1. Menyediakan solusi konsultasi keamanan cyber yang inovatif dan berkualitas tinggi dengan menerapkan riset dan teknologi terbaru untuk memenuhi kebutuhan perusahaan/partner.\n2. Menjalin kemitraan erat dan berkelanjutan dengan perusahaan/partner dengan memahami kebutuhan mereka dan memberikan solusi yang tepat untuk mengatasi tantangan unik yang dihadapi oleh mereka.\n3. Menyediakan layanan konsultasi yang profesional dan terpercaya untuk membantu perusahaan/partner meningkatkan strategi keamanan cyber mereka.\n4. Mempromosikan kesadaran keamanan cyber melalui program pelatihan dan edukasi yang efektif, termasuk pelatihan karyawan dan pihak terkait di perusahaan perusahaan/partner.\n5. Terus mengembangkan dan meningkatkan kemampuan dan keahlian dalam bidang keamanan cyber serta teknologi informasi secara umum, agar dapat memberikan solusi terbaik bagi perusahaan/partner.\n6. Memberikan rekomendasi dan saran dalam penerapan regulasi dan kebijakan keamanan cyber yang tepat dan efektif.\n7. Menyediakan solusi untuk mengurangi risiko dan mengatasi ancaman cyber yang kompleks dan berkelanjutan.\n8. Memberikan konsultasi dan dukungan dalam rangka mengimplementasikan praktik keamanan terbaik dalam bisnis perusahaan/partner.\n9. Menjalin kemitraan dengan universitas dan lembaga riset lainnya untuk mengembangkan teknologi keamanan cyber dan menghasilkan pengetahuan baru di bidang ini.\n10.Mendorong pemikiran inovatif dalam bidang keamanan cyber untuk menghasilkan solusi baru dan efektif untuk mengatasi tantangan yang berkembang di dunia digital.\n***"
#     await interaction.response.send_message(f"```{vision}\n\n{mission}```")

# @bot.tree.command(name="help", description="Display all commands listed in b0tliau1ni")
# async def help(interaction):
#     embed = discord.Embed(
#         title="Help Command",
#         description="Display all commands listed in b0tliau1ni",
#         color=0x2b2c31)
#     embed.set_author(name="b0t-liau1ni", icon_url=f"{logob31}")
#     embed.set_thumbnail(url=f"{logob31}")
#     embed.add_field(name="**Help Basic Commands**", value="""\n/help - *Display all commands listed in b0tliau1ni*
#     /visi-misi - *Seeing the vision & mission of the b3liau1ni team*
#     /ctf schedule <limit *(max 5)*> - *Check schedule ctf from ctftime*
#     /server-info - *Display information about the server used by team b3liau1ni*
#     /version - Display version of b0t-liau1ni application
#     /changelog - Display a records changes of b0tliau1ni application""", inline=True)
#     embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION")) 
#     permission_role = get(interaction.user.roles, name="Main Team")
#     if permission_role:
#         embed.add_field(name="**Help Admin Commands**", value="\n/ctf join <id> - *Join the ctf with id*\n/ctf finish - *Finish the ctf when ctf completed*\n", inline=False)
#         pass
#     await interaction.response.send_message(embed=embed, ephemeral=True)

# @bot.tree.command(name="server-info", description="Display information about the server used by team b3liau1ni")
# async def server_info(interaction):
#     def get_uptime():
#         with open('/proc/uptime', 'r') as f:
#             uptime_seconds = float(f.readline().split()[0])
#         uptimeInfo = ''
#         uptime_days = int(uptime_seconds / 86400)
#         uptime_seconds -= uptime_days * 86400
#         uptime_hours = int(uptime_seconds / 3600)
#         uptime_seconds -= uptime_hours * 3600
#         uptime_minutes = int(uptime_seconds / 60)
#         uptime_seconds -= uptime_minutes * 60
#         if uptime_days > 0:
#             uptimeInfo += '{} day(s) '.format(uptime_days)
#         if uptime_hours > 0:
#             uptimeInfo += '{} hour(s) '.format(uptime_hours)
#         if uptime_minutes > 0:
#             uptimeInfo += '{} minute(s) '.format(uptime_minutes)
#         uptimeInfo += '{:.2f} second(s)'.format(uptime_seconds)
#         return uptimeInfo
#     def get_cpu_info():
#         cpu_info = {'name': 'unknown', 'cores': 0, 'threads': 0}
#         with open('/proc/cpuinfo', 'r') as f:
#             for line in f:
#                 if line.startswith('model name'):
#                     cpu_info['name'] = line.split(':')[1].strip()
#                 elif line.startswith('processor'):
#                     cpu_info['cores'] += 1
#                 elif line.startswith('siblings'):
#                     cpu_info['threads'] = int(line.split(':')[1].strip())
#         return cpu_info
#     cpu_info = get_cpu_info()
#     cpu_usage = psutil.cpu_percent()
#     memory_usage = psutil.virtual_memory()
#     memory_usage_gb = memory_usage.used / 1024 ** 3
#     available_memory = memory_usage.available / 1024 ** 3
#     total_memory = memory_usage.total / 1024 ** 3
#     free_memory_percent = memory_usage.percent
#     await interaction.response.send_message(f"""```SERVER INFORMATION\nInformation about the server used by team b3liau1ni
#     \nCPU Information:
#     \tCPU Name: {cpu_info['name']}
#     \tCPU Core: {cpu_info['cores']}
#     \tCPU Threads: {cpu_info['threads']}
#     \tCPU Usage: {cpu_usage}%
#     \nMemory Information:
#     \tMemory: {memory_usage_gb:.2f} GB/{total_memory:.2f} GB (Free Mem: {available_memory:.2f} GB)
#     \tMemory usage: {free_memory_percent}/100%
#     \nUptime Server: {get_uptime()}```""")

# @bot.tree.command(name="version", description="Display version of b0t-liau1ni application")
# async def version(interaction):
#     embed = discord.Embed(
#         title="**Currently Version:** " + os.getenv("VERSION"),
#         description="Ingin melihat fitur/perubahan terbaru pada b0tliau1ni?\nCommand: **/changelog**",
#         color=0x2b2c31)
#     embed.set_author(name="b0t-liau1ni", icon_url=f"{logob31}")
#     embed.set_thumbnail(url=f"{logob31}")
#     embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION")) 
#     await interaction.response.send_message(embed=embed)

# @bot.tree.command(name="changelog", description="Display a records changes of b0tliau1ni application")
# async def changelog(interaction):
#     embed = discord.Embed(
#         title="**Change Log**",
#         description="""**April 3rd 2023** (v0.1)\n- b0t-liau1ni created\n- Command b!ctfschedule created\n- Command /visi-misi created
#         \n**April 4th 2023** (v0.2)\n- \n- Change Command b!ctfschedule --> /ctf schedule\n- Integrated to server\n- Create a presence\n- Command /ctf join created
#         \n**April 5th 2023** (v0.3)\n- Command /server-info created\n- Command /version created
#         \n**April 9th 2023** (v0.4)\n- Logging system
#         \n**April 12th 2023** (v0.5)\n - Command /ctf finish created\n- Fix minor from Logging system
#         \n**April 28th 2023** (v0.6)\n - Add countdown on Embed & Join""",
#         color=0x2b2c31)
#     embed.set_author(name="b0t-liau1ni", icon_url=f"{logob31}")
#     embed.set_thumbnail(url=f"{logob31}")
#     embed.set_footer(text="b0t-liau1ni \u00A9 2023 - " + os.getenv("VERSION")) 
#     await interaction.response.send_message(embed=embed)


bot.run(os.getenv("BOT_TOKEN"))
