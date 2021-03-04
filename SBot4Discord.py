import os
import time
from discord.ext import commands
import discord
from pyscreenshot import grab

TOKEN = ''

# import json
# import requests
# URL = 'https://discordapp.com/oauth2/authorize?&client_id=816481315913859112&scope=bot&permissions=2048'

bot = commands.Bot(command_prefix='')


@bot.event
async def on_ready():
    print("Бот запущен.")


@bot.command()
async def ping(ctx):
    """-----Пинг до бота. """

    ping = round(bot.latency * 1000)
    await ctx.send(f"мой пинг {ping} мс. А твой?")


@bot.command()
async def clr(ctx, amount: int):
    """-----Удаляет сообщения. clr N -  удалит N последних сообщений. """

    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} сообщения(ий) было удалено.")
    await ctx.send("Clean", tts=True)
    time.sleep(5)
    await ctx.channel.purge(limit=2)
    try:
        os.remove('box.png')
    except:
        pass


@bot.command()
async def ss(ctx):
    """-----Делает скриншот."""
    im = grab(bbox=(0, 0, 960, 1080))
    im.save('box.png')
    file = discord.File("box.png", filename="box.png")
    await ctx.send(file=file)


@bot.command()
async def login(ctx):
    """-----Логин-пароль для площадок."""
    with open('login', encoding='UTF-8') as f:
        s = f.read()
        print(s)
    await ctx.send(s, tts=False)


# Так как мы указали префикс в settings, обращаемся к словарю с ключом prefix.
# @bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
# async def fox(ctx):
#     response = requests.get('https://some-random-api.ml/img/fox')  # Get-запрос
#     json_data = json.loads(response.text)  # Извлекаем JSON
#
#     embed = discord.Embed(color=0xff9900, title='Random Fox')  # Создание Embed'a
#     embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
#     await ctx.send(embed=embed)  # Отправляем Embed


bot.run(TOKEN)
