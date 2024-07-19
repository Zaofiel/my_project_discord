#ссылка на бота:https://discord.com/oauth2/authorize?client_id=1231177142109212682&permissions=8&scope=bot
import discord, requests, random
from discord.ext import commands
from os import listdir


intents = discord.Intents.default()
intents.message_content = True

command_info = [
    "Точка обязательна!!!!"
    "1. .add - сложение двух чисел",
    "2. .spam - спам бот",
    "3. .repeat - повторение до определённого числа",
    "4. .mem - какой-то мем",
    "5. .duck - изображение утки"
]

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
async def info_help(ctx):
    for i in command_info:
        await ctx.send(i)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def spam(ctx, spam_count=100):
    for i in range(spam_count):
        await ctx.send(f"Ха-ха-ха, заспамил {i+1}")

@bot.command()
async def repeat(ctx, times: int, content='хаха'):
    for i in range(times):
        await ctx.send(content)
        
@bot.command()
async def mem(ctx):
    img_ = random.random()
    if img_ >= 1:
        img = ('mem4.jpg')
    elif img_ >= 0.7 and img_ < 1:
        img = ('mem1.jpg')
    elif img_ >= 0.4 and img_ < 0.7:
        img = ('mem2.jpg')
    elif img_ >= 0.2 and img_ < 0.4:
        img = ('mem3.jpg')
    elif img_ >= 0 and img_ < 0.2:
        img = ('mem5.jpg')
    
    with open(f'images/{img}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run('MTIzMTE3NzE0MjEwOTIxMjY4Mg.GRGkHX.UYS2P8mhP4B58E2v7DSj9LS98fQB2w07gPtloc')