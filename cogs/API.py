import discord
import random
import requests
from discord.ext import commands
import urllib.request
import json


class API(commands.Cog):

    def __int__(self, client):
        self.client = client
        
    #NASA API ( if you type _NASA it gives you nasa's image of the day) apply for a developer key at https://api.nasa.gov/)
    @commands.command(aliases=['NASA','Nasa'])
    async def nasa(self, ctx, *, lmao=None):
      apodurl = 'https://api.nasa.gov/planetary/apod?'
      mykey = 'api_key=ur_key'
      apodurlobj = urllib.request.urlopen(apodurl + mykey)
      apodread = apodurlobj.read()
      decodeapod = json.loads(apodread.decode('utf-8'))
      await ctx.send (f"{decodeapod['hdurl']}")
      await ctx.send(f"**{decodeapod['title']}**")
      if lmao == None:
        await ctx.send(f'if you want more info type "_NASA info"')
      if lmao == "info":  
        await ctx.send(f"{decodeapod['explanation']}")
        

    #bot that gives a random image a rover took along with the date and which rover took it. sometimes doesn't work since certain rovers didn't take photos on certain days.
    #also I'm terrible at naming variables  
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
      mykey = '&camera=fhaz&api_key=ur_key'
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



def setup(client):
    client.add_cog(API(client))

