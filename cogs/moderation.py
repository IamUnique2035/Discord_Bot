import discord
from discord.ext import commands


class moderation(commands.Cog):

    def __int__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
     await ctx.channel.purge(limit=amount)

    @commands.command(pass_content=True,
                aliases=['Nickname', 'nickname', 'Changenick'])
    @commands.has_permissions(manage_nicknames=True)
    async def changenick(self, ctx,
                     member: discord.Member,
                     nick,
                     *,
                     nicky='',
                     nickyy=''):
     joint = "% s % s % s" % (nick, nicky, nickyy)
     await member.edit(nick=joint)
     await ctx.send(f'Nickname was changed for {member.mention}')



def setup(client):
    client.add_cog(moderation(client))
