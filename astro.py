import os
import sys
import time
import queue
import random
import discord
import threading
from pystyle import Colorate, Colors
from discord.ext import commands
from requests_futures.sessions import FuturesSession

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "astro!",case_insensitive = False,bot = True,intents=intents)

def slow_write(text):
    for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.005)

class astro:
    if os.name == "nt":
       os.system("cls")
    else:
       terminal_title = "Astro Massban - Made by horrid"
       print(f'\33]0;{terminal_title}\a', end='', flush=True)
       os.system("clear")

    logo = '''
                                                     ___
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

                                              $ Houston, we've had a problem here - Apollo 13$

---------------------------------------------------------------------------------------------------------------------------------------------
'''
    print(Colorate.Vertical(Colors.yellow_to_red, logo, 1))
    print("astro@localhost - loading script...")
    time.sleep(5)
    print("astro@localhost - done, press enter to start.")
    input()
    if os.name == "nt":
       os.system("title Astro-V1")
       os.system("cls")
    else:
       terminal_title = "Astro Massban | Made by horrid"
       print(f'\33]0;{terminal_title}\a', end='', flush=True)
       os.system("clear")
    print(Colorate.Vertical(Colors.yellow_to_red, logo, 1))
    token = input("astro@localhost - enter token: \u001b[0m")
    guild = input("astro@localhost - enter guild id: \u001b[0m")
    q = queue.Queue()
    session = FuturesSession()
    headers = {"Authorization": f"Bot {token}"}
    apiv = ["v9", "v6"]
    count = 0

    def massbansend():
        try:
            while True:
                req, url, headers = astro.q.get()
                s = req(url, headers=headers).result()
                astro.count += 1
                print(f"astro@localhost - {astro.count} banned member - status code: {s.status_code}")
                if s.text == '{"message": "Max number of bans for non-guild members have been exceeded. Try again later", "code": 30035}':
                    print("astro@localhost - maximum non-guilded ban members has been exceded, change the entire bot, please exit by yourself.")
                    input()
                    input()
                    input()
                    input()
                astro.q.task_done()
        except Exception:
            print(f"astro@localhost - error sending requests, contact horrid or nell.")
            input()
            exit()

    def idworker():
        for memberid in open("scraped/ids.txt"):
            ranidapi = [f"https://discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}", f"https://discordapp.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}", f"https://canary.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}", f"https://ptb.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}"]
            astro.q.put((astro.session.put, random.choice(ranidapi), astro.headers))
        astro.q.join()

    def massbanworker():
        for member in open("scraped/scraped.txt"):
            ranapi = [f"https://discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}", f"https://discordapp.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}", f"https://canary.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}", f"https://ptb.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}"]
            astro.q.put((astro.session.put, random.choice(ranapi), astro.headers))
        astro.q.join()

    @client.event
    async def on_connect():
        try:
            guild = await client.fetch_guild(int(astro.guild))
        except:
            print("astro@localhost - guild id is invalid")
            input()
            os._exit(0)

        print("astro@localhost - scraping..")
        members = await guild.chunk()
        print("astro@localhost - done.")
        with open('scraped/scraped.txt', 'a') as z:
            for member in members:
                z.write(str(member.id) + "\n")
        print("astro@localhost - ban ids? [y/n]")
        option = input("astro@localhost - choice: \u001b[0m")
        if option == "n":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(astro.logo)
            time.sleep(5)
            astro.massbanworker()
        else:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(astro.logo)
            time.sleep(5)
            astro.idworker()

if __name__ == "__main__":
    for x in range(1000):
        threading.Thread(target=astro.massbansend, daemon=True).start()
        threading.Thread(target=astro.massbansend, daemon=True).start()
    try:
        client.run(astro.token)
    except:
        print("astro@localhost - token is invalid or ratelimited.")
        print("astro@localhost - please make sure you have all intents enabled on your bots token.")
        input()
        exit()
