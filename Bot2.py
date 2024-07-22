import discord
from discord.ext import commands
from kodland_utils import gen_pass
import os, random 
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def meme(ctx):
    selected = random.choice(os.listdir('memes'))
    with open(f'memes/{selected}', 'rb') as f:
        pictures = discord.File(f)
    await ctx.send(file = pictures)

def GetDuckImageURL():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    image_url = GetDuckImageURL()
    await ctx.send(image_url)

organic = ['food waste', 'poop', 'leaves']
paper = ['cardboard', 'paper bag', 'parchment paper', 'tissues']
plastic = ['plastic bottles', 'plastic bags', 'toys']
metal = ['cans', 'electronic', 'cabel', 'cd']

@bot.command()
async def trash_query(ctx):
        await ctx.send('What trash do you wish to sort? ')
        message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        message = str(message.content)

        if message.lower() in organic:
            await ctx.send('That is organic trash!')
            await ctx.send('You can turn it into compost!')

        elif message.lower() in paper:
            await ctx.send('That is paper trash!')
            await ctx.send('Throw it into the trash with a paper label!')

        elif message.lower() in plastic:
            await ctx.send('That is Plastic trash!')
            await ctx.send('Throw it into the trash with a plastic label!')

        elif message.lower() in metal:
            await ctx.send('That is Metallic trash!')
            await ctx.send('Throw it into the trash with a metal label!')

        else:
            await ctx.send('Uknown!')

bot.run("")