import discord
from discord.ext import commands
import random
import time
from keys import TOKEN

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = 'T!', intents=intents)

@client.event
async def on_ready():
    print('TutuśBOT wylądował')
    print('==================')

# @client.command()
# async def lud(ctx):
#     await ctx.send('Rub mi louda nie żartuj')

# @client.event()
# async def on_member_join(member):
#     channel = client.get_channel(390518200787533836)
#     await channel.send('JD')

# @client.event()
# async def on_member_remove(member):
#     channel = client.get_channel(390518200787533836)
#     await channel.send(';0')

@client.command(pass_context = True)
async def lud(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await ctx.send('rub lud')
        await channel.connect()
        await ctx.send('p!play LOUDA')
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('')

@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('You need to be in a voice channel to run this command.')

@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('I am not in a voice channel.')

client.run(TOKEN)