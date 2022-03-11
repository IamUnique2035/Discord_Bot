import discord
from discord.ext import commands
from discord.utils import get
import json
import urllib.request
import random
import os
import requests

client = commands.Bot(command_prefix='_', intents=discord.Intents.all())


@client.event
async def on_ready():
    print('Bot is ready.')

#NASA API ( if you type _NASA it gives you nasa's image of the day) apply for a developer key at https://api.nasa.gov/)
@client.command(aliases=['NASA','Nasa'])
async def nasa(ctx, *, lmao=None):
    apodurl = 'https://api.nasa.gov/planetary/apod?'
    mykey = 'api_key=ur_API_key'
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
@client.command()
async def rover(ctx):
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
    mykey = '&camera=fhaz&api_key=ur_API_key'
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
    
    
@client.command(aliases=['Help', 'HELP', 'Bot', 'BOT'])
async def bot(ctx):
    await ctx.send(
        f'Hi ,I can do the following: \n convert fahrenheit to celcius by using  _F (value) and celcius to fahrenheit using  _C (value) \n clear messages in bulk(mod only command) using  _clear (value) the standard value is 10 messages \n convert the following currencies:usd,eur and inr to convert use _(currency you would like to convert from)_(currency you would like to convert to) (value)'
        f' ')

#dumb easter egg command lol
@client.command(aliases=['easteregg', 'Easteregg'])
async def easter_egg(ctx):
    await ctx.send(f'Did you think it would be this easy ?')

#part 2 of dumb easter egg command
@client.command()
async def EasterEgg(lol):
    await lol.send(f'Oh, I guess it was that easy.(easter egg 1/1 found)')

# _ping tester
@client.command(aliases=['test', 'Test'])
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 1000)}ms')

#_clear (number of messages,if left blank amount =10)
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

#dumb command lol
@client.command(aliases=[
    'suck dick', 'Suckdick', 'SuckDick', 'suck_dick', 'Suck_dick'])
async def suckdick(ctx):
    await ctx.send(f" ERROR. Can't find {ctx.author.mention}'s dick, object is missing or non-existent.")

#if bot's nickname is changed to anything that includes the word porn it sets it back to original name or kevin Jr(you can change this to anything you want)
@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("porn") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="Kevin Jr")


                
@client.command(aliases=['mad', 'Mad', 'Angry', 'Angy', 'angy'])
async def angry(ctx):
    await ctx.send(f'https://tenor.com/view/angry-cat-instant-gif-24474761')


@client.command(aliases=['Mood', 'feeling', 'Feeling'])
async def mood(ctx):
    feels = [
        'https://tenor.com/view/angry-cat-instant-gif-24474761',
        'https://tenor.com/view/dog-smile-happy-gif-9231579',
        'https://tenor.com/view/dog-puppy-dog-eyes-pout-sad-cute-animals-gif-11172970',
        'https://tenor.com/view/horny-jail-bonk-dog-hit-head-stop-being-horny-gif-17298755',
        'https://tenor.com/view/cat-bed-laying-lazy-dzekas-gif-20013760',
        'https://tenor.com/view/lazy-cat-funny-fat-animals-gif-20933835'
    ]
    await ctx.send(f'{random.choice(feels)}')

#_8ball (question you would like to ask it)
@client.command(aliases=['8ball', '8Ball'])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Outlook not so good.", "Very doubtful."
    ]
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')


@client.command(aliases=['Created'])
async def created(ctx):
    await ctx.send(f'I was created on 13th ‎December ‎2020')


@client.command(aliases=['Horny', 'Bonk', 'bonk'])
async def horny(ctx):
    await ctx.send(f'https://tenor.com/view/horny-jail-bonk-dog-hit-head-stop-being-horny-gif-17298755')

#_fight (user1) (user2)
@client.command(aliases=['fight'])
async def Fight(ctx, user1, *, user2):
    name1 = get(ctx.guild.members, name=user1)
    name2 = get(ctx.guild.members, name=user2)
    response = (f'{name1.mention} & {name2.mention}, Stop fighting mommy and daddy.',
                f'Go get a room {name1.mention} & {name2.mention}.',
                f'If I wanted to see two monkeys fighting each other I would have gone to the zoo, {name1.mention} & {name2.mention}')
    await ctx.send(f'{random.choice(response)}')

#_nickname (@user1) (new nickname)
@client.command(pass_content=True,
                aliases=['Nickname', 'nickname', 'Changenick'])
@commands.has_permissions(manage_nicknames=True)
async def changenick(ctx,
                     member: discord.Member,
                     nick,
                     *,
                     nicky='',
                     nickyy=''):
    joint = "% s % s % s" % (nick, nicky, nickyy)
    await member.edit(nick=joint)
    await ctx.send(f'Nickname was changed for {member.mention}')
 
#sets a status for your bot. Just change (name=f'____') to anything you want.
@client.event
async def on_ready():
    #playing,watching,streaming and listening are possible statuses
    await client.change_presence(activity=discord.Game(name=f"Your Mum")
                                 
#_load (cog to be loaded) 
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension}.py was loaded')

#_restart (cog to be reloaded)
@client.command(aliases=['Restart'])
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension}.py was reloaded')

#unload (cog to be unloaded)
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension}.py was unloaded')

#looks for the cog file. create a file named cogs at the same level of this file and create this programme's cogs in it.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('your__token_here_')
