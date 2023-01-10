import discord
import time
from discord.ext import commands

class suggest(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.client.get_channel(message.channel.id)

        if message.channel.id == 1013880424314982511:
            if message.author.bot:
                return
            else:
                if message.content.startswith('^'):
                    return
                else:
                    embed = discord.Embed(
                        title = "",
                        description = f'{message.author.mention} — {message.content}',
                        timestamp = message.created_at,
                        color = 0xfc652c
                    )
                    embed.set_author(name = f"🧣 | Вопрос от {message.author.display_name}", icon_url = message.author.avatar.url)
                    embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} © TheGeekVoice')
                    await message.delete()
                    await channel.send(embed=embed)
        else:
            return

    @commands.command()
    @commands.has_any_role(374899810324709377, 962760441468162088)
    async def suggest(self, ctx, id_msg):
        channel = self.client.get_channel(1013880424314982511)
        msg = await channel.fetch_message(int(id_msg))
        embed = discord.Embed(
            title = "",
            description = f'{msg.author.mention} — {msg.content}',
            timestamp = msg.created_at,
            color = 0xfc652c
        )
        embed.set_author(name = f"🧣 | Вопрос от {msg.author.display_name}", icon_url = msg.author.avatar.url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} © TheGeekVoice')
        await channel.send(embed=embed)

async def setup(client):
    await client.add_cog(suggest(client))