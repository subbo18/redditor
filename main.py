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

#creates command prefix, idk what the other shit does
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
async def test(ctx, arg):
    await ctx.send(arg)

#array for retrieving url function
numarr = []

@bot.command()
#lists top ten posts of subreddit
#ctx refers to Commands.context object
async def topten(ctx, sub):
    array = []
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.top(limit=10):
        array.append(submission)
    int = 0
    for i in array:
        int = int+1
        numarr.append(i)
        #url is sends affiliated media (?) doesnt work for galleries or videos
        #if no image it just sends the plain url of the post
        await ctx.send(str(int) + ". " + i.title + " " + i.url)
    
@bot.command()
async def link(ctx, num):
    #removes first ten elements from the previous query
    n = 10
    newlist = numarr[n:]
    #THIS ISNT THE URL FUNCTION, need fix
    await ctx.send(newlist[int(num)-1].url)
        
bot.run(TOKEN)
