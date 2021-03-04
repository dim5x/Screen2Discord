from discord_webhook import DiscordWebhook
from pyscreenshot import grab
import keyboard

# Url вебхука канала в Discord
URL = 'https://discord.com/api/webhooks/816472418519482389/MMYy7Mm53kg0lCwe2FR0BhraRNNZCgom-wHxEvmpou6Aca0gDxUPQ0rYwK3wKGVKi8mN'


def hook():
    """Делает скриншот половины экрана. Сохраняет в файл. Файл отправляет в Discord."""

    # Делаем скриншот, сохраняем.
    im = grab(bbox=(0, 0, 960, 1080))
    im.save('box.png')
    # Читаем файл и отправляем.
    webhook = DiscordWebhook(url=URL)
    with open('box.png', 'rb') as f:
        webhook.add_file(file=f.read(), filename='example.jpg')

    return webhook.execute()


# Биндим сочетания клавиш для функции скриншотера и выхода.
keyboard.add_hotkey('Ctrl + 1', hook)
keyboard.wait('Ctrl + Q')
