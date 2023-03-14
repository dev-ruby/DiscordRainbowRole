import asyncio
import json
import sys
import os

import discord

with open("config.json", "r") as fp:
    data = fp.read()
config = json.loads(data)

if config["TOKEN"] == "" or config["ChangeDelay"] == 0 or config["RoleID"] == 0:
    print("config.json 파일을 작성해야 합니다.")
    os.system("pause")
    sys.exit()

client = discord.Client(intents=discord.Intents.all())

colors = [
    discord.colour.Colour.red(),
    discord.colour.Colour.orange(),
    discord.colour.Colour.gold(),
    discord.colour.Colour.green(),
    discord.colour.Colour.blue(),
    discord.colour.Colour.purple(),
]

count = 0


@client.event
async def on_ready():
    global count

    if count == 1:
        return

    count = 1

    while True:
        for color in colors:
            role = client.guilds[0].get_role(config["RoleID"])
            await role.edit(colour=color)
            await asyncio.sleep(int(config["ChangeDelay"]))


client.run(config["TOKEN"])
