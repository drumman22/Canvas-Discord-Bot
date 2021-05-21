import discord
from discord.ext import commands, tasks

from canvasapi import Canvas
from bs4 import BeautifulSoup

import config

class ClassFeed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.canvas = Canvas(config.CANVAS_URL, config.CANVAS_KEY)
        self.course = self.canvas.get_course(1381436)
        self.announce_channel = "class-announcements"

        self.announce_index = 0

    @tasks.loop(minutes=5)
    async def announce_feed(self):
        self.announce_index += 1
        print("ANNOUNCEMENTS: Grabbing announcements")

        announces = self.canvas.get_announcements([self.course.id])
        for ann in announces:
            # Read announcements have already been posted
            if ann.read_state == "read":
                continue
            
            print("ANNOUNCEMENTS: Creating and sending announcement")
            soup = BeautifulSoup(ann.message, "html.parser")
            embed = discord.Embed(
                title = f"{ann.title} ({ann.author['display_name']})",
                url = ann.url,
                description = soup.get_text(),
                timestamp = ann.posted_at_date,
                colour = discord.Colour.blue()
            )
            embed.set_thumbnail(url=ann.author["avatar_image_url"])
            embed.set_footer(text=self.course.name)

            # Find channel in guilds
            for guild in self.bot.guilds:
                ann_channel = discord.utils.get(guild.channels, name=self.announce_channel)
                await ann_channel.send(embed=embed)

                # Curty's Disc
                main_channel = discord.utils.get(guild.channels, id=840013593802178562)
                await main)channel.send(embed=embed)

            # Mark announcement as read
            ann.mark_as_read()
            print(f"ANNOUNCEMENTS: Sent \"{ann.title}\"")

    @commands.Cog.listener()
    async def on_ready(self):
        self.announce_feed.start()

def setup(bot):
    bot.add_cog(ClassFeed(bot))

    