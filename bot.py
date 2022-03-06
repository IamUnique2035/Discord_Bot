import discord
from discord.ext import commands
from discord.utils import get
import random
import os

client = commands.Bot(command_prefix='_', intents=discord.Intents.all())


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command(aliases=['Help', 'HELP', 'Bot', 'BOT'])
async def bot(ctx):
    await ctx.send(
        f'Hi ,I can do the following: \n convert fahrenheit to celcius by using  _F (value) and celcius to fahrenheit using  _C (value) \n clear messages in bulk(mod only command) using  _clear (value) the standard value is 10 messages \n convert the following currencies:usd,eur and inr to convert use _(currency you would like to convert from)_(currency you would like to convert to) (value)'
        f' ')


@client.command(aliases=['easteregg', 'Easteregg'])
async def easter_egg(ctx):
    await ctx.send(f'Did you think it would be this easy ?')


@client.command()
async def EasterEgg(lol):
    await lol.send(f'Oh, I guess it was that easy.(easter egg 1/1 found)')


@client.command(aliases=['test', 'Test'])
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 1000)}ms')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=[
    'suck dick', 'Suckdick', 'SuckDick', 'suckdick_kritharth', 'suck_dick', 'Suck_dick'])
async def suckdick(ctx):
    await ctx.send(f" ERROR. Can't find {ctx.author.mention}'s dick, object is missing or non-existent.")


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


@client.command()
async def adopted(ctx):
    await ctx.send(f' OH NO THIS CANT BE TRUE')


@client.command(aliases=['gi'])
async def GI(ctx):
    await ctx.send(f'Kevin has no interest in playing Genshin Impact')


@client.command(aliases=['Protest'])
async def protest(ctx):
    await ctx.send(f'I WILL NOT.')


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


@client.command(aliases=['fight'])
async def Fight(ctx, user1, *, user2):
    name1 = get(ctx.guild.members, name=user1)
    name2 = get(ctx.guild.members, name=user2)
    response = (f'{name1.mention} & {name2.mention}, Stop fighting mommy and daddy.',
                f'Go get a room {name1.mention} & {name2.mention}.',
                f'If I wanted to see two monkeys fighting each other I would have gone to the zoo, {name1.mention} & {name2.mention}')
    await ctx.send(f'{random.choice(response)}')


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


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension}.py was loaded')


@client.command(aliases=['Restart'])
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension}.py was reloaded')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension}.py was unloaded')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('_token_here_')