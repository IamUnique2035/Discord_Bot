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
      # I wanted to display the image along with the title and an explanation. There is probably a better way to do this but it works! (lol)
      await ctx.send (f"{decodeapod['hdurl']}")
      await ctx.send(f"**{decodeapod['title']}**")
      if lmao == None:
        await ctx.send(f'if you want more info type "_NASA info"')
      if lmao == "info":  
        await ctx.send(f"{decodeapod['explanation']}")
        

    #bot that gives a random image a rover took along with the date and which rover took it. sometimes doesn't work since certain rovers didn't take photos on certain days.
    #also I'm terrible at naming variables  
    @commands.command(aliases =['Rover', 'NASA_Rover', 'nasa_rover'])
    async def rover(self, ctx):
     url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'
     tros = '/photos?sol='
     rovers = ["curiosity", "opportunity", "Spirit"]
     lala = random.choice(rovers)
     if lala == "Spirit":
         sol = str(random.randrange(1, 764))
     if lala == "opportunity":
         sol = str(random.randrange(1, 1000))
     if lala == "curiosity":
         sol = str(random.randrange(99, 1000))
     my_secret = '&camera=fhaz&api_key=ur_key'
     r = requests.get(url + lala + tros + sol + my_secret)
     data = r.json()
     await ctx.send(f"{data['photos'][0]['img_src']}")
     await ctx.send(f"taken on {data['photos'][0]['earth_date']} by {data['photos'][0]['rover']['name']} rover")
    
    
    #_weather (place)
    #get API key from https://www.weatherbit.io/
    @commands.command(aliases=['Weather', 'Time', 'time', 'temperature', 'Temperature', 'temp', 'Temp'])
    async def weather(self, ctx, *, place):
     apodurl = 'http://api.weatherapi.com/v1/current.json?key='
     my_secret = ur_key
     end = '&q='
     r = requests.get(apodurl + my_secret + end + place)
     data = r.json()
     await ctx.send(f"\nLocation: **{data['location']['name']}**\nRegion: **{data['location']['region']}**"
                   f"\nCountry: **{data['location']['country']}**\nLatitudes: **{data['location']['lat']}** "
                   f"\nLongitude: **{data['location']['lon']}**\nDate & Time: **{data['location']['localtime']}**"
                   f"\nWeather: **{data['current']['condition']['text']}**\nHumidity: **{data['current']['humidity']}%**"
                   f"\nTemperature: **{data['current']['feelslike_c']}°C**\nWind Speed: **{data['current']['wind_kph']}KPH**")
        
        
    #a simple API that gives out a joke. Warning some of the jokes can be a bit Extreme.
    @commands.command()
    async def joke(self, ctx):
    apodurl = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=political,racist'
    r = requests.get(apodurl)
    data = r.json()
    if data['type'] == 'twopart':
        await ctx.send(f"{data['setup']} \n{data['delivery']}")
    if data['type'] == 'single':
        await ctx.send(f"{data['joke']}")
        
    #an command that selects a random GIF for a given "feeling". Get a key from here https://tenor.com/gifapi 
    @commands.command(aliases=['Tenor', 'GIF', 'gif', 'Gif'])
    async def tenor(self, ctx, *, feeling):
    url = 'https://g.tenor.com/v1/search?q='
    limit = '&limit=50'
    key = 'your_key_here'
    full_url = requests.get(url + feeling + key + limit)
    data = full_url.json()
    results = data['results']
    number = results[random.randrange(1, 50)]
    await ctx.send(f"{number['media'][0]['gif']['url']}")
    
    
    #_search (topic)
    #search nasa's Image library for the topic and chooses a random image along with the title and description.
    @commands.command(aliases=['search', 'Search', 'NASA_Search'])
    async def nasa_search(self, ctx, *, search):
     url = 'https://images-api.nasa.gov/search?q='
     media_type = '&media_type=image'
     r = requests.get(url + search + media_type)
     data = r.json()
     x = random.randrange(0, 100)
     detes = requests.get(data['collection']['items'][x]['href'])
     doots = data['collection']['items'][x]['data'][0]
     true_data = detes.json()
     if true_data[0].endswith('.tif'):
         await ctx.send(true_data[1])
     else:
         await ctx.send(true_data[0])
     await ctx.send(f"**{doots['title']}** taken on **{doots['date_created']}**\n{doots['description']}")
     
     

def setup(client):
    client.add_cog(API(client))

