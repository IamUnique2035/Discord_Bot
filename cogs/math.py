import discord
from discord.ext import commands


class math(commands.Cog):

    def __int__(self, client):
        self.client = client

    @commands.command(aliases=['Square'])
    async def square(self, ctx, *, number_to_be_squared):
      x = int(number_to_be_squared)
      answer = (x ** 2)
      await ctx.send(f'square= {answer}')

    @commands.command(aliases=['Cube'])
    async def cube(self, ctx, *, number_to_be_cubed):
     w = int(number_to_be_cubed)
     answer = (w ** 3)
     await ctx.send(f'Cube = {answer}')

    @commands.command(aliases=['Sum', 'add', 'Add', 'addition', 'Addition'])
    async def sum(self, ctx, pow, *, kech):
     await ctx.send(f'answer = {float(pow) + float(kech)}')

    @commands.command(
    aliases=['Minus', 'min', 'Min', 'subtract', 'Subtract', 'sub', 'Sub'])
    async def minus(self, ctx, wop, *, hcek):
     await ctx.send(f'answer = {float(wop) - float(hcek)}')

    @commands.command(aliases=['Multiply', 'mul', 'Mul', 'product', 'Product'])
    async def multiply(self,ctx, input_number, *, input_number_to_multiply_with):
     await ctx.send(
        f'answer = {float(input_number) * float(input_number_to_multiply_with)}')

  
    @commands.command(aliases=['Division', 'Div', 'div', 'quotient', 'Quotient'])
    async def division(self, ctx, dividend, *, divisor):
     await ctx.send(f'answer = {float(dividend) / float(divisor)}')


def setup(client):
