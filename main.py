import discord
from discord.ext import commands, tasks
import random
import os
import time

# from keep_alive import keep_alive

bot = commands.Bot(command_prefix='.')
bot.remove_command("help")

def permissionCheck(author, rolename):
    for role in author.roles:
        if role.name == rolename:
            return True



# starter_encouragements = [
#   "Cheer up!",
#   "Hang in there.",
#   "You are a great person / bot!",
#   "I love you"
# ]
# sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]       

@bot.command()
async def pm(ctx):
    user = bot.get_user(196351039559958529)
    await ctx.send(user)
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Everytime they say I have aimbot :('))
    print('bot is up')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    response = [
        "It is certain",
        "Outlook good",
        "You may rely on it",
        "Ask again later",
        "Concentrate and ask again",
        "Reply hazy, try again",
        "My reply is no",
        "My sources say no" ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')

@bot.command()
async def load(ctx, extension):
    if(permissionCheck(ctx.author, "admin")):
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"{extension} loaded")
        time.sleep(0.2)
        await ctx.channel.purge(limit = 2)

@bot.command()
async def unload(ctx, extension):
    if(permissionCheck(ctx.author, "admin")):
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f"{extension} unloaded")
        time.sleep(0.2)
        await ctx.channel.purge(limit = 2)

@bot.command()
async def reload(ctx, extension):
    if(permissionCheck(ctx.author, "admin")):
        # await ctx.channel.purge(limit = 1)
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f"{extension} unloaded")
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"{extension} loaded")
        time.sleep(0.2)
        await ctx.channel.purge(limit = 3)

    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'{error}. Check `.help` for more info')

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     if any(word in message.content for word in sad_words):
#         await message.channel.send(f'{random.choice(starter_encouragements)} {message.author.mention}')
#     else:
#         pass


# keep_alive()
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('your token here')
