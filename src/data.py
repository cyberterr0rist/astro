import json, random

with open("settings.json") as file_content:
    settings = json.load(file_content)

    astro_settings = settings["astro"]
    token = settings["token"]

headers = {"Authorization": f"Bot {token}"}
channel_body = {"name": random.choice(astro_settings["channel_names"])}
prune_body = {"days": 1}
role_body = {"name": random.choice(astro_settings["role_names"])}
message_body = {"content": random.choice(astro_settings["spam_messages"])}
webhook_body = {"name": random.choice(astro_settings["webhook_usernames"])}
