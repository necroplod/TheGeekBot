import discord
from discord.ext import commands

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(" ")
        print(f'--------------------------------------------------')
        print(f"| Logged on as TheGeekBot - {self.client.user.id}  |")
        print(f"| Discord.py Version: {discord.__version__}                      |")
        print(f'--------------------------------------------------')
        print(" ")

async def setup(client):
    await client.add_cog(events(client))