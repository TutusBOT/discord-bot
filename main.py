from cgi import test
import nextcord
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions, MissingPermissions
from nextcord.abc import GuildChannel
from keys import TOKEN
import random
import os
import wavelink

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print('TutuśBOT wylądował')
    print('==================')
    bot.loop.create_task(node_connect())

testServerId = 390518200787533834

@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f'Node {node.identifier} is ready')

async def node_connect():
    await bot.wait_until_ready()
    await wavelink.NodePool.create_node(bot=bot, host='lavalinkinc.ml', port=443, password="incognito", https=True)

@bot.slash_command(guild_ids=[testServerId], description='Play a song!')
async def play(interaction: Interaction, channel: GuildChannel = SlashOption(channel_types=[ChannelType.voice], description='Voice channel to join'), search: str = SlashOption(description='Song to play')):
    await interaction.response.send_message('sth')
    search = await wavelink.YouTubeTrack.search(query=search, return_first=True)
    if not interaction.guild.voice_client:
        vc: wavelink.Player = await channel.connect(cls=wavelink.Player)
    elif not getattr(interaction.author.voice, 'channel', None):
        return await interaction.send('First join a voice channel')
    else:
        vc: wavelink.Player = interaction.guild.voice_client
    if vc.queue.is_empty and not vc.is_playing():
        await vc.play(search)
        await interaction.send(f'Now playing: {search.title}')
    else:
        vc.queue.put_wait(search)
        await interaction.send(f'Added {search.title} to the queue.')
    if vc.loop: return
    setattr(vc, 'loop', False)


@bot.slash_command(name='random', description='Generates a random number within a range of 1 and given number', guild_ids=[testServerId])
async def randomnumber(interaction: Interaction, range:int):
    await interaction.response.send_message(f'Random number between 1 and {range} is: {random.randrange(1,range)}')
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(390518200787533836)
    await channel.send('JD')



bot.run(TOKEN)
# @bot.command()
# async def lud(ctx):
#     await ctx.send('Rub mi louda nie żartuj')

# @bot.event()
# async def on_member_join(member):
#     channel = bot.get_channel(390518200787533836)
#     await channel.send('JD')

# @bot.event()
# async def on_member_remove(member):
#     channel = bot.get_channel(390518200787533836)
#     await channel.send(';0')

# @bot.command(pass_context = True)
# async def lud(ctx):
#     if(ctx.author.voice):
#         channel = ctx.message.author.voice.channel
#         await ctx.send('rub lud')
#         await channel.connect()
#         await ctx.send('p!play LOUDA')
#         time.sleep(3)
#         await ctx.guild.voice_client.disconnect()
#     else:
#         await ctx.send('')

# @bot.command()
# async def join(ctx):
#     if(ctx.author.voice):
#         channel = ctx.message.author.voice.channel
#         await channel.connect()
#     else:
#         await ctx.send('You need to be in a voice channel to run this command.')

# @bot.command()
# async def leave(ctx):
#     if(ctx.voice_client):
#         await ctx.guild.voice_client.disconnect()
#     else:
#         await ctx.send('I am not in a voice channel.')

# @bot.command()
# async def random(ctx):
#     await ctx.send(ctx.author)
#     await voice.edit(ctx.author, reason="None", mute=True)

# @bot.command()
# @has_permissions(kick_members=True)
# async def kick(ctx, member: nextcord.Member, *, reason=None):
#     await member.kick(reason=reason)
#     await ctx.send(f'User {member} has been kicked')

# @kick.error
# async def kick_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send("You don't have permission to kick people!")

# @bot.command()
# @has_permissions(ban_members=True)
# async def ban(ctx, member: nextcord.Member, *, reason=None):
#     await member.ban(reason=reason)
#     await ctx.send(f'User {member} has been banned')

# @kick.error
# async def ban_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send("You don't have permission to ban people!")

