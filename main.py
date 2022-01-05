import disnake
from disnake.ext import commands
import asyncio
import os
import time
import keep_alive

keep_alive.keep_alive()

bot = commands.Bot(command_prefix=">")

categoryid = 0
text = "текст"

token = os.environ['token']
id = os.environ['id']

pings = 0
category = 0

async def __spam1(category, text):
    while True:
        for i in category.channels:
            await i.send(text)
            global pings
            pings += 1


async def __spam2(category, text):
    while True:
        for i in category.channels:
            await i.send(text)
            global pings
            pings += 1


async def __spam3(category, text):
    while True:
        for i in category.channels:
            await i.send(text)
            global pings
            pings += 1


async def __spam4(category, text):
    while True:
        for i in category.channels:
            await i.send(text)
            global pings
            pings += 1


async def __spam5(category, text):
    while True:
        for i in category.channels:
            await i.send(text)
            global pings
            pings += 1


async def __spam6(category, text):
    while True:
        for i in category.channels:
            await i.send(text)
            global pings
            pings += 1


async def __spam7(category, text):
    while True:
        for i in category.channels:
            await i.send(text)
            global pings
            pings += 1


async def __spam8(category, text):
    while True:
        for i in category.channels:
            await i.send(text)
            global pings
            pings += 1


async def __spam9(category, text):
    while True:
        for i in category.channels:
            await i.send(text)
            global pings
            pings += 1


async def __spam10(category, text):
    while True:
        for i in category.channels:
            await i.send(text)
            global pings
            pings += 1


@bot.event
async def on_ready():
		category = bot.get_channel(categoryid)
		print(f'Ready! Logged as {bot.user.name}, {bot.user.id}')
		while True:
				await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=f"pings 👀 {pings}"))
				asyncio.create_task(__spam1(category, text))
				asyncio.create_task(__spam2(category, text))
				asyncio.create_task(__spam3(category, text))
				asyncio.create_task(__spam4(category, text))
				asyncio.create_task(__spam5(category, text))
				asyncio.create_task(__spam6(category, text))
				asyncio.create_task(__spam7(category, text))
				asyncio.create_task(__spam8(category, text))
				asyncio.create_task(__spam9(category, text))
				asyncio.create_task(__spam10(category, text))
				await asyncio.sleep(2.5)


bot.run(token)
