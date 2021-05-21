import os

import discord
from discord.ext import commands

import config


class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        self.version = config.VERSION
        self.debug = True
        self.setup_cogs()

    def setup_cogs(self):
        loaded_file_names = []
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                if filename[:-3] == "debug" and not self.debug:
                    continue
                self.load_extension(f"cogs.{filename[:-3]}")
                loaded_file_names.append(filename)
        
        ext_list = ", ".join(loaded_file_names)
        print(f"Loaded Cog Extensions: {ext_list}")

    async def on_ready(self):
        print(f"Bot v{self.version} On Ready | {self.user}")