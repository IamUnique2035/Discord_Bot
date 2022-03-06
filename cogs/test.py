import discord
from discord.ext import commands


class test(commands.Cog):

    def __int__(self, client):
        self.client = client

    @commands.command()
    async def unicorn(self,ctx):
        await ctx.send(f'load is working')

def setup(client):
    client.add_cog(test(client))
