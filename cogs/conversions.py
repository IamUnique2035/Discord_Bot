import discord
from discord.ext import commands

## A bunch of currency conversions. There is probably a bettter way to do it. such as by using an API or something.
class conversions(commands.Cog):

    def __int__(self, client):
        self.client = client

    @commands.command(aliases=['Fahrenheit', 'F', 'f'])
    async def fahrenheit(self, ctx, *, a):
     await ctx.send(f'{(int(a) - 32) * 5 / 9} C')

  
    @commands.command(aliases=['Celcius', 'C', 'c'])
    async def celsius(self, ctx, *, b):
     await ctx.send(f'{(int(b) * 9 / 5) + 32} F')

  
    @commands.command(aliases=['usd_inr', 'Usd_Inr'])
    async def USD_INR(self, ctx, *, a):
     await ctx.send(f'{(int(a)*75)} INR')


    @commands.command(alisases=['usd_eur', 'Usd_Inr'])
    async def USD_EUR(self, ctx, *, b):
     await ctx.send(f'{(int(b)*0.91)} EUR')


    @commands.command(aliases=['Inr_Usd', 'inr_usd'])
    async def INR_USD(self, ctx, *, c):
     await ctx.send(f'{(int(c)/75)} USD')


    @commands.command(aliases=['Eur_Inr', 'eur_inr'])
    async def EUR_INR(self, ctx, *, d):
     await ctx.send(f'{(int(d)*83)} INR')


    @commands.command()
    async def INR_EUR(self, ctx, *, e):
     await ctx.send(f'{(int(e)*0.012)} EUR')


    @commands.command()
    async def EUR_USD(self, ctx, *, f):
     await ctx.send(f'{(int(f)*1.09)} USD')

  
    @commands.command()
    async def INR_YEN(self, ctx, *, g):
     await ctx.send(f'{(int(g)*1.50)} YEN')

  
    @commands.command()
    async def USD_YEN(self, ctx, *, h):
      await ctx.send(f'{(int(h)*114.82)} YEN')

  
    @commands.command()
    async def EUR_YEN(self, ctx, *, i):
      await ctx.send(f'{int(i)*125.59} YEN')


def setup(client):
    client.add_cog(conversions(client))
