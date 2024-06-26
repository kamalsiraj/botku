import discord
from discord.ext import commands
import random
import os
import requests


#membaca token dari file token.txt
with open("token.txt", "r") as f:
    token = f.read()

sampah = {
    'kertas' : 'anorganik',
    'plastik' : 'anorganik',
    'kardus' : 'anorganik', 
    'sisa makanan' : 'organik',
    'daun kering' : 'organik',
    'kulit buah' : 'organik', 
    'baterai' : 'B3',
    'oli' : 'B3',
    'deterjen' : 'b3'
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def heh(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def laugh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(name='bot')
async def coolbot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def jenis_sampah(ctx, item:str):
    if item.lower() in sampah:
        await ctx.send(f'{item.capitalize()} merupakan jenis sampah : {sampah[item.lower()]}')
    else:
        await ctx.send(f'Maaf, {item.capitalize()} tidak tercatat di dalam daftar')

@bot.command()
async def organik(ctx):
    await ctx.send(f'sampah jenis organik dapat diolah menjadi pupuk kompos, makanan hewan, eco enzyme, dan biogas')

@bot.command()
async def anorganik(ctx):
    await ctx.send(f'sampah jenis anorganik dapat diolah menjadi kerajinan tangan, bahan daur ulang, dan eco brick')

@bot.command()
async def B3(ctx):
    await ctx.send(f'sampah jenis B3 dapat diolah dengan melakukan pemilahan, membuangnya ke pembuangan khusus, ')

bot.run(token)
