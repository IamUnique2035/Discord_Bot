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

    
#displays a random GIF when _mood is typed.
@client.command(aliases=['Mood', 'feeling', 'Feeling'])
async def mood(ctx):
    feels = [
        'https://tenor.com/view/angry-cat-instant-gif-24474761',
        'https://tenor.com/view/dog-smile-happy-gif-9231579',
        'https://tenor.com/view/dog-puppy-dog-eyes-pout-sad-cute-animals-gif-11172970',
        'https://tenor.com/view/horny-jail-bonk-dog-hit-head-stop-being-horny-gif-17298755',
        'https://tenor.com/view/cat-bed-laying-lazy-dzekas-gif-20013760',
        'https://tenor.com/view/lazy-cat-funny-fat-animals-gif-20933835'  ,
        'https://tenor.com/view/sad-cat-sunakook-tired-exhausted-gif-24687868',
        'https://tenor.com/view/dog-dogs-doggy-angry-thinking-gif-18088194'
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

    
#_fight (@user1) (@user2)
@client.command(aliases=['fight'])
async def Fight(ctx, user1: discord.Member, user2: discord.Member):
    response = (f'{user1.mention} & {user2.mention}, Stop fighting mommy and daddy.',
        f'Go get a room {user1.mention} & {user2.mention}.',
        f'If I wanted to see two monkeys fighting each other I would have gone to the zoo, {user1.mention} & {user2.mention}')
    await ctx.send(f'{random.choice(response)}')

 
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
