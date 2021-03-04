from discord.ext import commands
from pyscreenshot import grab
import time
import discord

TOKEN = ''

# import json
# import requests
# URL = 'https://discordapp.com/oauth2/authorize?&client_id=816481315913859112&scope=bot&permissions=2048'

bot = commands.Bot(command_prefix='!')


@bot.command()
async def clr(ctx, amount: int):
    """Удаляет сообщения. !clean N -  удалит N последних сообщений. """

    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} сообщений было удалено.")
    time.sleep(5)
    await ctx.channel.purge(limit=1)


@bot.command()
async def ss(ctx):
    """!ss - делает скриншот."""
    im = grab(bbox=(0, 0, 960, 1080))
    im.save('box.png')
    file = discord.File("box.png", filename="box.png")
    await ctx.send(file=file)


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
