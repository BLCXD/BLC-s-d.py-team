import discord
from mariocard import *
from discord.ext.commands import has_permissions
from discord.ext import commands

bot = commands.Bot(command_prefix='@', intents = discord.Intents.all())
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming("BLC's Discord.py Team"))
    print("online")

@bot.command()
async def regulamin(ctx):
    embed=discord.Embed(title="Regulamin", url="https://www.youtube.com/@blc_yt", description="Regulamin serwera BLC's Discord.py Team                    ", color=0x0d27e7)
    embed.set_author(name="BLC's Discord.py Team", url="https://www.youtube.com/@blc_yt")
    embed.set_thumbnail(url="https://docs.pycord.dev/en/stable/_static/pycord_logo.png")
    embed.add_field(name="1.Pisać komendy na kanałach które są do tego przypisane.",  value="Regulamin", inline=True)
    embed.add_field(name=" 2.Zabronione jest używanie wulgaryzmów",  value="Regulamin", inline=True)
    embed.add_field(name="3.Nie podszywać się pod nikogo ",  value="Regulamin", inline=True)
    embed.add_field(name="4.Nie reklamować swojego kanału na Youtube,tik tok lub na innych mediach społecznościowych",  value="Regulamin", inline=True)
    embed.add_field(name="5.Zabronione jest wysyłanie linków do zawirusowanych stron aplikacji lub do czegoś innego co ma wirusa,a zwłaszcza podawanie fałszywych danych o stronie/aplikacji",  value="Regulamin", inline=True)
    embed.add_field(name="6.Zabronione jest obrażanie kogokolwiek na serwerze a zwłaszcza administratora lub jakiegoś członka.",  value="Regulamin", inline=True)
    embed.add_field(name="7.Zabraniamy umieszczania rzeczy sprzecznych z prawem",  value="Regulamin", inline=True)
    embed.add_field(name="8.Zabraniamy wpisywania fałszywych treści o serwerze",  value="Regulamin", inline=True)
    embed.add_field(name="9.Zabraniamy wpisywać jakich kolwiek treści o serwerze bez zgody jednego z administratorów. ",  value="Regulamin", inline=True)
    await ctx.send(embed=embed)


@bot.command
@has_permissions(ban_members=True)
async def ban(ctx,member : discord.member, reason="Nie podano powodu"):
    await member.ban(reason=reason) 


@bot.command
@has_permissions(kick_members=True)
async def ban(ctx,member : discord.member, reason="Nie podano powodu"):
    await member.kick(reason=reason) 


@bot.command
@has_permissions(mute_members=True)
async def ban(ctx,member : discord.member, reason="Nie podano powodu"):
    await member.mute(reason=reason) 

    
@bot.event
async def on_member_join(member):
    guild = member.guild
    channel = discord.utils.get(guild.text_channels, id=1055850793477099690)
    card = WelcomeCard()
    card.name = member
    card.server = guild.name
    card.text = "BLC's Discord.py Team"
    card.color = "blue"
    card.path = "tlo.jpeg"
    await channel.send(file= await card.create())

bot.run("ODUzMTg4ODM5MjI4NzAyNzQy.G4xU4N.eAqb3-ObH36OYw9vHwUe1YT8FRq22rIRgc-pwk")