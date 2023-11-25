import discord
import random
from discord.ext import commands

import asyncpraw

#BOT TOKEN, DO NOT SHARE
TOKEN = "bot token"

#schniippppp reddit account info, DO NOT SHARE
reddit = asyncpraw.Reddit(
    client_id="bla",
    client_secret="bla",
    password = "bla",
    user_agent="bla",
    username = "bla",
)

#creates command prefix, idk what the intents does
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='schnip ',intents=intents)

#runs when bot successfully connects
@bot.event
async def on_ready():
    print(f'{bot.user} UP AND RUNNING')

@bot.event
async def on_message(message):
    #makes sure bot doesnt respond to own mesages
    if message.author == bot.user: 
        return
    #schnip :3
    #1/10 chance of responding with :3
    probs = random.randint(1, 10)
    if message.content == 'schnip':
        print(str(message.author) + " said schnip")
        if probs == 3:
            await message.channel.send(f':3')
            print("Schnipper said :3")
        else:
            await message.channel.send(f'schnip')
            print("Schnipper said schnip")
    await bot.process_commands(message)

#test command
'''
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
'''

#array for link function
numarr = []

#lists top ten posts of subreddit
@bot.command()
#ctx refers to Commands.context object, idk what that does but it has to be there
async def topten(ctx, sub):

    print(str(ctx.author) + " used topten for " + str(sub))
    
    #array for the ten posts
    array = []

    subreddit = reddit.subreddit(sub)

    for submission in subreddit.top(limit=10):
        array.append(submission)
        numarr.append(submission)

    int = 0
    for i in array:
        int = int+1
        
        if i.url.endswith(('.jpg', '.png', '.gif')):
            await ctx.send("**" + str(int) + ". " + i.title + "** " + i.url)

        elif i.is_video:
            video_url = i.media['reddit_video']['fallback_url']
            await ctx.send("**" + str(int) + ". " + i.title + "** " + video_url )

        elif hasattr(i, "is_gallery"):
            #idk how this part works but it does
            ids = [j['media_id'] for j in i.gallery_data['items']]
            url_data = [(i.media_metadata[id]['p'][0]['u'].split("?")[0].replace("preview", "i")) for id in ids]
            galleryarr = " ".join(url_data)
            await ctx.send(f"**{int}. {i.title}** {galleryarr}")

        else:
            await ctx.send("**" + str(int) + ". " + i.title + "**")

#lists hot ten posts of subreddit
@bot.command()
async def hotten(ctx, sub):
    print(str(ctx.author) + " used hotten for " + str(sub))
    array = []
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=10):
        array.append(submission)
        numarr.append(submission)
    int = 0
    for i in array:
        int = int+1
        if i.url.endswith(('.jpg', '.png', '.gif')):
            await ctx.send("**" + str(int) + ". " + i.title + "** " + i.url)
        elif i.is_video:
            video_url = i.media['reddit_video']['fallback_url']
            await ctx.send("**" + str(int) + ". " + i.title + "** " + video_url )
        elif hasattr(i, "is_gallery"):
            ids = [j['media_id'] for j in i.gallery_data['items']]
            url_data = [(i.media_metadata[id]['p'][0]['u'].split("?")[0].replace("preview", "i")) for id in ids]
            galleryarr = " ".join(url_data)
            await ctx.send(f"**{int}. {i.title}** {galleryarr}")
        else:
            await ctx.send("**" + str(int) + ". " + i.title + "**")

#lists gilded ten posts of subreddit
@bot.command()
async def gildedten(ctx, sub):
    print(str(ctx.author) + " used gildedten for " + str(sub))
    array = []
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.gilded(limit=10):
        array.append(submission)
        numarr.append(submission)
    int = 0
    for i in array:
        int = int+1
        if i.url.endswith(('.jpg', '.png', '.gif')):
            await ctx.send("**" + str(int) + ". " + i.title + "** " + i.url)
        elif i.is_video:
            video_url = i.media['reddit_video']['fallback_url']
            await ctx.send("**" + str(int) + ". " + i.title + "** " + video_url )
        elif hasattr(i, "is_gallery"):
            ids = [j['media_id'] for j in i.gallery_data['items']]
            url_data = [(i.media_metadata[id]['p'][0]['u'].split("?")[0].replace("preview", "i")) for id in ids]
            galleryarr = " ".join(url_data)
            await ctx.send(f"**{int}. {i.title}** {galleryarr}")
        else:
            await ctx.send("**" + str(int) + ". " + i.title + "**")

#lists controversial ten posts of subreddit
@bot.command()
async def controversialten(ctx, sub):
    print(str(ctx.author) + " used controversialten for " + str(sub))
    array = []
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.controversial(limit=10):
        array.append(submission)
        numarr.append(submission)
    int = 0
    for i in array:
        int = int+1
        if i.url.endswith(('.jpg', '.png', '.gif')):
            await ctx.send("**" + str(int) + ". " + i.title + "** " + i.url)
        elif i.is_video:
            video_url = i.media['reddit_video']['fallback_url']
            await ctx.send("**" + str(int) + ". " + i.title + "** " + video_url )
        elif hasattr(i, "is_gallery"):
            ids = [j['media_id'] for j in i.gallery_data['items']]
            url_data = [(i.media_metadata[id]['p'][0]['u'].split("?")[0].replace("preview", "i")) for id in ids]
            galleryarr = " ".join(url_data)
            await ctx.send(f"**{int}. {i.title}** {galleryarr}")
        else:
            await ctx.send("**" + str(int) + ". " + i.title + "**")

#lists new ten posts of subreddit
@bot.command()
async def newten(ctx, sub):
    print(str(ctx.author) + " used newten for " + str(sub))
    array = []
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.new(limit=10):
        array.append(submission)
        numarr.append(submission)
    int = 0
    for i in array:
        int = int+1
        if i.url.endswith(('.jpg', '.png', '.gif')):
            await ctx.send("**" + str(int) + ". " + i.title + "** " + i.url)
        elif i.is_video:
            video_url = i.media['reddit_video']['fallback_url']
            await ctx.send("**" + str(int) + ". " + i.title + "** " + video_url )
        elif hasattr(i, "is_gallery"):
            ids = [j['media_id'] for j in i.gallery_data['items']]
            url_data = [(i.media_metadata[id]['p'][0]['u'].split("?")[0].replace("preview", "i")) for id in ids]
            galleryarr = " ".join(url_data)
            await ctx.send(f"**{int}. {i.title}** {galleryarr}")
        else:
            await ctx.send("**" + str(int) + ". " + i.title + "**")

#lists rising ten posts of subreddit
@bot.command()
async def risingten(ctx, sub):
    print(str(ctx.author) + " used risingten for " + str(sub))
    array = []
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.rising(limit=10):
        array.append(submission)
        numarr.append(submission)
    int = 0
    for i in array:
        int = int+1
        if i.url.endswith(('.jpg', '.png', '.gif')):
            await ctx.send("**" + str(int) + ". " + i.title + "** " + i.url)
        elif i.is_video:
            video_url = i.media['reddit_video']['fallback_url']
            await ctx.send("**" + str(int) + ". " + i.title + "** " + video_url )
        elif hasattr(i, "is_gallery"):
            ids = [j['media_id'] for j in i.gallery_data['items']]
            url_data = [(i.media_metadata[id]['p'][0]['u'].split("?")[0].replace("preview", "i")) for id in ids]
            galleryarr = " ".join(url_data)
            await ctx.send(f"**{int}. {i.title}** {galleryarr}")
        else:
            await ctx.send("**" + str(int) + ". " + i.title + "**")
    
@bot.command()
async def link(ctx, num):
    n = -10
    newlist = numarr[n:]
    print(str(ctx.author) + " used link for " + str(newlist[int(num)-1].title))
    await ctx.send("https://www.reddit.com/" + newlist[int(num)-1].id)
  
bot.run(TOKEN)
