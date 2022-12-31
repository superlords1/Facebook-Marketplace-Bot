import discord
from discord import app_commands
from discord.ext import commands
from bot import getPosts
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix = "/", intents = discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))

@bot.command(name = "rodney")
async def stats(ctx, args):
    links, texts = getPosts(int(args))
    embed = discord.Embed(title = 'POSTS')
    for i in range(int(args)):
        embed.add_field(name = links[i], value = texts[i], inline = True)
    await ctx.send(embed = embed)

@bot.command(name = "help")
async def help(ctx):
    await ctx.send(embed = discord.Embed(title = "STANCED CAR PARTS", description = "To get parts: /rodney <amount of listings>"))

load_dotenv()
bot.run(os.getenv('token'))
