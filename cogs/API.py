import discord
import random
import requests
from discord.ext import commands
import urllib.request
import json


class API(commands.Cog):

    def __int__(self, client):
        self.client = client

      
    @commands.command(aliases =['Rover','NASA_Rover','nasa_rover'])
    async def rover(self, ctx):
      apodurl = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'
      tros = '/photos?sol='
      rovers = ["curiosity", "opportunity", "Spirit"]
      lala = random.choice(rovers)
      if lala == "Spirit":
        sol = str(random.randrange(1, 764))
      if lala == "opportunity":
        sol = str(random.randrange(1, 1000))
      if lala == "curiosity":
        sol = str(random.randrange(99, 1000))
      mykey = '&camera=fhaz&api_key=0yyWN7evu88eM3E8erJ2T7BZNWmFjm2Tn2tmo0HD'
      r = requests.get(apodurl + lala + tros + sol + mykey)
      data = r.json()
      neo = data['photos']
      troup = neo[0]
      rover = troup['rover']
      name = rover['name']
      oofd = troup['img_src']
      date = troup['earth_date']
      await ctx.send(f'{oofd}')
      await ctx.send(f'taken on {date} by {name} rover')

      
    @commands.command(aliases=['NASA','Nasa'])
    async def nasa(self, ctx, *, lmao=None):
      apodurl = 'https://api.nasa.gov/planetary/apod?'
      mykey = 'api_key=0yyWN7evu88eM3E8erJ2T7BZNWmFjm2Tn2tmo0HD'
      apodurlobj = urllib.request.urlopen(apodurl + mykey)
      apodread = apodurlobj.read()
      decodeapod = json.loads(apodread.decode('utf-8'))
      await ctx.send (f"{decodeapod['hdurl']}")
      await ctx.send(f"**{decodeapod['title']}**")
      if lmao == None:
        await ctx.send(f'if you want more info type "_NASA info"')
      if lmao == "info":  
        await ctx.send(f"{decodeapod['explanation']}")

