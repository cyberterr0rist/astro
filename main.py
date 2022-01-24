import os
import sys
import time
import queue
import random
import discord
import threading
from getpass import getpass
from discord.ext import commands
from requests_futures.sessions import FuturesSession

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "astro!",case_insensitive = False,bot = True,intents=intents)

def slow_write(text):
    for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.005)

class astro:
    if os.name == "nt":
       os.system("title Astro Massban | Made by horrid; cls")
    else:
       terminal_title = "Astro Massban | Made by horrid"
       print(f'\33]0;{terminal_title}\a', end='', flush=True)
       os.system("clear")

    logo = """
\u001b[34m                  ╔═╗╔═╗╔╦╗╦═╗╔═╗
\u001b[34m                  ╠═╣╚═╗ ║ ╠╦╝║ ║
\u001b[36m                  ╩ ╩╚═╝ ╩ ╩╚═╚═╝
\u001b[35m                ───────────────────
\u001b[35m                  Massban  Horrid

"""
    print(logo)
    token = getpass("\u001b[35mastro@localhost - enter token: ")
    guild = input("\u001b[35mastro@localhost - enter guild id: ")
    q = queue.Queue()
    session = FuturesSession()
    headers = {"Authorization": f"Bot {token}"}

    def massbansend():
        try:
            while True:
                req, url, headers = astro.q.get()
                s = req(url, headers=headers).result()
                print(s.text)
                astro.q.task_done()
        except Exception:
            pass

    def idworker():
        for memberid in open("scraped/ids.txt"):
            astro.q.put((astro.session.put, "https://discord.com/api/v{}/guilds/{}/bans/{}".format(random.randint(6,9), astro.guild, memberid), astro.headers))
        astro.q.join()

    def massbanworker():
        for member in open("scraped/scraped.txt"):
            astro.q.put((astro.session.put, "https://discord.com/api/v{}/guilds/{}/bans/{}".format(random.randint(6,9), astro.guild, member), astro.headers))
        astro.q.join()

    @client.event
    async def on_connect():
        try:
            guild = await client.fetch_guild(int(astro.guild))
        except:
            print("\u001b[35mastro@localhost - guild id is invalid")
            input()
            os._exit(0)

        print("\u001b[35mastro@localhost - scraping..")
        members = await guild.chunk()
        print("\u001b[35mastro@localhost - done.")
        with open('scraped/scraped.txt', 'a') as z:
            for member in members:
                z.write(str(member.id) + "\n")
        print("\u001b[35mastro@localhost - ban ids? [y/n]")
        option = input("\u001b[35mastro@localhost - choice: ")
        if option == "n":
            print("astro@localhost - massbanning...")
            astro.massbanworker()
        else:
            print("astro@localhost - massbanning...")
            astro.idworker()

if __name__ == "__main__":
    for x in range(1000):
        threading.Thread(target=astro.massbansend, daemon=True).start()
    try:
    client.run(astro.token)
    except:
        print("\u001b[35mastro@localhost - token is invalid or ratelimited.")
        print("\u001b[35mastro@localhost - please make sure you have all intents enabled on your bots token.")
        input()
        os._exit(0)
