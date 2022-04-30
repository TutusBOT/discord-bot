import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions, MissingPermissions
import time
from keys import TOKEN

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = 't!', intents=intents)

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

@client.command()
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('You need to be in a voice channel to run this command.')

@client.command()
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('I am not in a voice channel.')

@client.command()
async def random(ctx):
    await ctx.send(ctx.author)
    await voice.edit(ctx.author, reason="None", mute=True)

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: nextcord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to kick people!")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: nextcord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has been banned')

@kick.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to ban people!")

client.run(TOKEN)