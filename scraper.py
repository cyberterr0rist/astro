import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="!", help_command=None, intents=intents)
token = input("Enter token: ")
guilds = input("Enter guild: ")

@client.event
async def on_connect():
    guild = await client.fetch_guild(int(guilds))
    members = await guild.chunk()
    amount = 0
    with open('ids.txt', 'a') as z:
        for member in members:
            z.write(str(member.id) + "\n")
            amount += 1
            print(f"{amount} ID Scraped.")
    exit()
client.run(token)
