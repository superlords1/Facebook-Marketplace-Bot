import discord
from discord import app_commands
from discord.ext import commands
from bot import get_info
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix = "/", intents = discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    #get_recent(1)

@bot.command(name = "rodney")
async def stats(ctx, args, args2):
    if args2 == 'recent':
        url = 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fgroups%2F553266151399305%3Fsorting_setting%3DCHRONOLOGICAL_LISTINGS'
    elif args2 == 'top':
        url = 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fgroups%2F553266151399305'
    else:
        await ctx.send(embed = discord.Embed(title = "Please specify 'top' or 'recent'"))
        return

    #
    links, texts = get_info(int(args), url)

    embed = discord.Embed(title = f"{args2} Listings")
    for i in range(int(args)):
        embed.add_field(name = links[i], value = texts[i], inline = True)
    await ctx.send(embed = embed)

@bot.command(name = "help")
async def help(ctx):
    await ctx.send(embed = discord.Embed(title = "STANCED CAR PARTS", description = "To get parts: /rodney <amount of listings> <top/recent>"))

@bot.command(name = "dabmeup")
async def dabmeup(ctx):
    await ctx.send(file=discord.File('dabmeup.gif'))
    
load_dotenv()
bot.run(os.getenv('token'))
