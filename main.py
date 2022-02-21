import os
import sys
import random
import requests
from threading import Thread

client = requests.Session()
amount = 0

class astro:
    if os.name == "nt":
        os.system("cls")
        os.system("title Astro Massban")
    else:
        os.system("clear")
        terminal_title = f"Astro Massban"
        print(f'\33]0;{terminal_title}\a', end='', flush=True)

    print("\u001b[38;5;46m				╔═╗╔═╗╔╦╗╦═╗╔═╗")
    print("\u001b[38;5;48m				╠═╣╚═╗ ║ ╠╦╝║ ║")
    print("\u001b[38;5;50m				╩ ╩╚═╝ ╩ ╩╚═╚═╝")
    print("\u001b[38;5;51m				  .gg/zeroday\n\n")
    token = input("\u001b[38;5;46mtoken@astro# ")
    guild = input("\u001b[38;5;46mguild@astro# ")

    def requeststart(id, api):
        headers = {"Authorization": f"Bot {astro.token}"}
        s = client.put(random.choice(api), headers=headers)
        if s.status_code in (200, 201, 203, 204, 205, 206, 207, 208, 210):
             print(f"\u001b[38;5;46m[Astro] - Executed ID - Status code: {s.status_code}")
        if s.status_code == 429:
             print(f"\033[91m[Astro] - Rate limited, trying in 1 second.")
        if s.status_code == 400:
             print(f"\033[91m[Astro] - Bad request, or reached most non-guilded banned members.")

if __name__ == "__main__":
    for id in open("ids.txt", "r"):
        amount += 1
        if os.name == "nt":
            os.system(f"title Astro Massban - Requests: {amount}")
        else:
            terminal_title = f"Astro Massban - Requests: {amount}"
            print(f'\33]0;{terminal_title}\a', end='', flush=True)

        api = [f"https://discord.com/api/v9/guilds/{astro.guild}/bans/{id}", f"https://discordapp.com/api/v9/guilds/{astro.guild}/bans/{id}", f"https://canary.discord.com/api/v9/guilds/{astro.guild}/bans/{id}", f"https://ptb.discord.com/api/v9/guilds/{astro.guild}/bans/{id}"]
        Thread(target=astro.requeststart, args=(id, api)).start()

