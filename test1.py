# imports os
import os

# imports discord.py, discords api
import discord

# imports load_dotenv from dotenv, used to grab variables from .env file
from dotenv import load_dotenv

# imports commands from discord.ext module
from discord.ext import commands


# loads .env file, grabs token from file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# creates new bot object with !prefix
bot = commands.Bot(command_prefix="!")

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@bot.command(name="ping")
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.command(name="nick")
async def ping(ctx):
    await ctx.channel.send("nock")


@bot.command(name="join")
async def join(ctx):
    server = ctx.author.voice

    if not server:
        await ctx.channel.send("must be in a voice channel")
        return

    await server.channel.connect()
    await ctx.channel.send("Yams is here baby")


@bot.command()
async def live(ctx, *args):
    titleInput = ""

    for arg in args:
        titleInput = titleInput + " " + arg

    file = discord.File("pooc.png")
    embed = discord.Embed(
        title=titleInput, url="https://www.twitch.tv/tehpocco", description="Come Hang Out!", color=discord.Color.purple())
    embed.set_thumbnail(url="attachment://pooc.png")

    await ctx.channel.send("@everyone\n", embed=embed, file=file)


@bot.command(name="socials")
async def socials(ctx):
    embed = discord.Embed(
        title="All Socials Available Here!", url="https://linktr.ee/TehPocco", color=discord.Color.purple())
    await ctx.channel.send(embed=embed)

bot.run(TOKEN)
client.run(TOKEN)
