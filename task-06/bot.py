import discord
from discord.ext import commands

BOT_TOKEN = "MTE1MjI4NTU1MzEwNzE2MTE1OA.GJU0QZ.x_QHbBMTZV78XPi1YaRqxGW9hN5TwkDtuk_Q4g"
CHANNEL_ID = 1154848833486983209

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command("help")

@bot .command()
async def livescore(ctx):
    import csv 
    with open('livescore.csv','r') as file:
        csv_file = csv.reader(file)
        await ctx.send("fetching the live score...")
        for lines in csv_file:
            for i in lines:
                await ctx.send(i)

@bot .command()
async def csv(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    await ctx.send(file=discord.File('livescore.csv'))

@bot .command()
async def help(ctx):
    await ctx.send("Commands")
    await ctx.send("!csv - get the csv file with livescores")
    await ctx.send("!livescore - get the live scores")

bot.run(BOT_TOKEN)
