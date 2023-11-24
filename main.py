import discord
import random
from discord.ext import commands

import asyncpraw

#BOT TOKEN, DO NOT SHARE
TOKEN = "bot token"

#schniippppp reddit account info shit
reddit = asyncpraw.Reddit(
    client_id="bla",
    client_secret="bla",
    password = "bla",
    user_agent="bla",
    username = "bla",
)

#creates comman prefix, idk what the other shit does
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='schnip ',intents=intents)

#runs when bot successfully connects
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    #makes sure bot doesnt respond to own mesages
    if message.author == bot.user: 
        return
    #schnip :3
    #1/10 chance of responding with :3
    probs = random.randint(1, 10)
    if message.content == 'schnip':
        if probs == 3:
            await message.channel.send(f':3')
        else:
            await message.channel.send(f'schnip')
    await bot.process_commands(message)

@bot.command()
#lists top ten posts of subreddit
#ctx refers to Commands.context object
async def topten(ctx, sub):
    print(sub)
    async for submission in reddit.subreddit(sub).top(limit=10):
        await ctx.send(submission.title)

bot.run(TOKEN)
