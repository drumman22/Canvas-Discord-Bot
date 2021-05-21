import sys
import discord

import config
import client

intents = discord.Intents.all()
client = client.Client(command_prefix=config.PREFIX, intents=intents)

if __name__ == "__main__":
    client.run(config.TOKEN, bot=True, reconnect=True)