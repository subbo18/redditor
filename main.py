import discord
import random   
from discord.ext import commands
import praw
from urlextract import URLExtract

check_for_async=False
extractor = URLExtract()

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

#gets rid of default help command so i can make custom one
bot.remove_command('help')

#runs when bot successfully connects
@bot.event
async def on_ready():
    print(f'{bot.user} UP AND RUNNING')

#schnip :3
@bot.event
async def on_message(message):
    #makes sure bot doesnt respond to own mesages
    if message.author == bot.user: 
        return
    #1/10 chance of responding with :3
    probs = random.randint(1, 10)
    if message.content == 'schnip':
        print(str(message.author) + " said schnip")
        if probs == 3:
            try:
                await message.channel.send(f':3')
                print("Schnipper said :3")
            except Exception as e:
                await message.channel.send(f'Uh oh! Error: ' + e.args[0])
                print(e.args[0])
        else:
            try:
                await message.channel.send(f'schnip')
                print("Schnipper said schnip")
            except Exception as e:
                await message.channel.send(f'Uh oh! Error: ' + e.args[0])
                print(e.args[0])
    await bot.process_commands(message)

#test command
'''
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

'''

'''
shit that needs to be fixed rn:
    - add command that can toggle nsfw subreddits and confirm with user that they are over 18
    - getpost doesnt work when the post just contains a link. also some formatting issues for the text.
    - add time and server to reports
    - handle post too long
    - GET NEXT TO WORK (PRIORITY) then make previous function
    - fix link and getpost and numarr[] (check line 125) cuz of new get module
    - see if there is ANY faster way to get check if its gallery
'''

#array for link function
numarr = []

#array for current posts that are being sent
postsusing = []

#1000 posts from get function
array = []

#used in next function, will replace probably
cat = ""
subs = ""

#lists ten posts of a category from a subreddit
@bot.command()
#ctx refers to Commands.context object, idk what that does but it has to be there
async def get(ctx, sub, category, num):
    cat = category
    print(cat)
    subs = sub
    print(subs)

    print(str(ctx.author) + " getted " + str(category) + " for " + str(sub))
    
    array = []

    #array for all links in a post
    urlsarr = []

    subreddit = reddit.subreddit(sub)

    if category == "hot":
        subbo = subreddit.hot(limit=1000)
    elif category == "new":
        subbo = subreddit.new(limit=1000)
    elif category == "top":
        subbo = subreddit.top(limit=1000)
    elif category == "rising":
        subbo = subreddit.rising(limit=1000)
    elif category == "controversial":
        subbo = subreddit.controversial(limit=1000)
    else:
        await ctx.send("The only valid categories are: hot, new, top, rising or controversial.")

    for submission in subbo:
        array.append(submission)
        numarr.append(submission)

    x = 0
    for i in array:
        x = x+1
        
        #gets reddit hosted image
        if i.url.endswith(('.jpg', '.png', '.gif')):
            try:
                if int(num) > 0:
                        await ctx.send("**" + str(x ) + ". " + i.title + "** " + i.url)
                        num = int(num)-1
            except Exception as e:
                await ctx.send(f'Uh oh! Error: ' + e.args[0])
                print(e.args[0])

        #gets reddit hosted video
        elif i.is_video:
            video_url = i.media['reddit_video']['fallback_url']
            try:
                if int(num) > 0:
                    await ctx.send("**" + str(x) + ". " + i.title + "** " + video_url )
                    num = int(num) -1
            except Exception as e:
                await ctx.send(f'Uh oh! Error: ' + e.args[0])
                print(e.args[0])

        #gets all images in a gallery
        elif hasattr(i, "is_gallery"):
            #idk how this part works but it does
            ids = [j['media_id'] for j in i.gallery_data['items']]
            url_data = [(i.media_metadata[id]['p'][0]['u'].split("?")[0].replace("preview", "i")) for id in ids]
            galleryarr = " ".join(url_data)
            try:
                if int(num) > 0:
                    await ctx.send(f"**{x}. {i.title}** {galleryarr}")
                    num = int(num)-1
            except Exception as e:
                await ctx.send(f'Uh oh! Error: ' + e.args[0])
                print(e.args[0])

        #gets all non reddit hosted media and websites in post
        else:
            text = i.selftext
            urls = extractor.find_urls(text)
            for url in urls:
                if url.startswith("https"):
                    urlsarr.append(url)
            try:
                if int(num) > 0:
                    await ctx.send("**" + str(x) + ". " + i.title + "** " + ' '.join(urlsarr))
                    num = int(num)-1
                    urlsarr = []
            except Exception as e:
                await ctx.send(f'Uh oh! Error: ' + e.args[0])
                print(e.args[0])

        if x == int(num):
                print("Schnipper successfully executed get " + str(category) + " for " + str(sub))
                #temparr = array[int(num):]
                #array = temparr


#for next function, same thing as get function
#but uses postusing[] instead of array[]
#because array[] is 1000 elements long
#and postusing[] is probably not 1000 elements long
async def nextget(ctx):
    x=0
    for i in postsusing:
            x = x+1
            
            if i.url.endswith(('.jpg', '.png', '.gif')):
                try:
                    if int(num) > 0:
                        await ctx.send("**" + str(x ) + ". " + i.title + "** " + i.url)
                        num = int(num)-1
                except Exception as e:
                    await ctx.send(f'Uh oh! Error: ' + e.args[0])
                    print(e.args[0])

            elif i.is_video:
                video_url = i.media['reddit_video']['fallback_url']
                try:
                    if int(num) > 0:
                        await ctx.send("**" + str(x) + ". " + i.title + "** " + video_url )
                        num = int(num) -1
                except Exception as e:
                    await ctx.send(f'Uh oh! Error: ' + e.args[0])
                    print(e.args[0])

            elif hasattr(i, "is_gallery"):
                #idk how this part works but it does
                ids = [j['media_id'] for j in i.gallery_data['items']]
                url_data = [(i.media_metadata[id]['p'][0]['u'].split("?")[0].replace("preview", "i")) for id in ids]
                galleryarr = " ".join(url_data)
                try:
                    if int(num) > 0:
                        await ctx.send(f"**{x}. {i.title}** {galleryarr}")
                        num = int(num)-1
                except Exception as e:
                    await ctx.send(f'Uh oh! Error: ' + e.args[0])
                    print(e.args[0])

            else:
                text = i.selftext
                urls = extractor.find_urls(text)
                for url in urls:
                    if url.startswith("https"):
                        urlsarr.append(url)
                try:
                    if int(num) > 0:
                        await ctx.send("**" + str(x) + ". " + i.title + "** " + ' '.join(urlsarr))
                        num = int(num)-1
                        urlsarr = []
                except Exception as e:
                    await ctx.send(f'Uh oh! Error: ' + e.args[0])
                    print(e.args[0])
            if x == int(num):
                    print("Schnipper successfully executed next " + str(cat) + " for " + str(subs))

#gets next amount of posts after a user has used the get function
@bot.command()
async def next(ctx, num):
    postsusing.clear
    for x in range(int(num)):
        postsusing.append(array.pop(0))
        nextget()
    
#links to a post after using get or next or prev
@bot.command()
async def link(ctx, num):
    n = -10
    newlist = numarr[n:]
    print(str(ctx.author) + " used link for " + str(newlist[int(num)-1].title))
    try:
        await ctx.send("https://www.reddit.com/" + newlist[int(num)-1].id)
        print("Schnipper successfully executed link for " + str(newlist[int(num)-1].title))
    except requests.Timeout as e:
                print("Schnipper timed out")

#sends body text of a post after using get or next or prev
@bot.command()
async def getpost(ctx, num):
    n = -10
    newlist = numarr[n:]
    print(str(ctx.author) + " used getpost for " + str(newlist[int(num)-1].title))
    text = newlist[int(num)-1].selftext
    title = str(newlist[int(num)-1].title)
    author = str(newlist[int(num)-1].author)
    try:
        if len(text) == 0:
            await ctx.send("**" + title + "** posted by **" + author + "** has no body text.")
            print("Post has no body text.")
        else:
            await ctx.send("**" + title + "** posted by **" + author + ":** ```" + text + "```")
            print("Schnipper successfully executed getpost for " + str(newlist[int(num)-1].title))
    except requests.Timeout as e:
                print("Schnipper timed out")
    except Exception as e:
        errnum = e.args[0]
        if e.code == 50006:
             await ctx.send("Post has no body text.")
             #need send media
             print("Post has no body text, sending media instead. (" + errnum + ")")
        elif e.code == 50035:
             # need fix
             await ctx.send("Post body text is too long to send on discord.")
             print("Post body text is too long to send on discord. (" + errnum + ")")

#sends list of commands
@bot.command()
async def commandlist(ctx):
    print(str(ctx.author) + " used commandlist")
    try:
        await ctx.channel.send(f'Here is a list of commands:')
        await ctx.channel.send(f'**getten** - gets ten posts of a subreddit from a specific category. The format for using this command is "schnip getten *subreddit* *category*." For example, using "schnip getten terraria top" means you are looking for the top posts in r/terraria.')
        await ctx.channel.send(f'**link** - gets link for a specific post, after you\'ve used a getten command. For example, after you\'ve got your top ten posts from r/terraria, using "schnip link 8" will give you the link for the 8th top post in r/terraria.')
        await ctx.channel.send(f'**getpost** - gets the body text for a specific post, after you\'ve used a getten command. For example, after you\'ve got your top ten posts from r/terraria, using "schnip getpost 8" will give you body text the 8th top post in r/terraria.')
        await ctx.channel.send(f'**help** - a guide to how Schnipper works.')
        print("Schnipper successfully executed commandlist")
    except requests.Timeout as err:
                print("Schnipper timed out")

#a guide to Schnipper
@bot.command()
async def help(ctx):
    print(str(ctx.author) + " used help")
    try:
        await ctx.channel.send(f'Hello! My name is Schnipper, and I am a bot that browses Reddit! Use "schnip commandlist" to know my list of commands.')
        await ctx.channel.send(f'If you aren\'t familiar Reddit or how it works, here is a quick guide:')
        await ctx.channel.send(f'**Introduction:** ```"It is a social platform where users submit posts that other users \'upvote\' or \'downvote\' based on if they like it. If a post gets lots of upvotes it moves up the Reddit rankings so that more people can see it. If it gets downvotes it quickly falls and disappears from most people\'s view."```   - from Brandwatch')
        await ctx.channel.send(f'**Here is a great video that explains how Reddit works:** https://www.youtube.com/watch?v=c9wokyF6dLA&pp=ygUOV2hhdCBpcyByZWRkaXQ%3D')
        await ctx.channel.send(f'.')
        await ctx.channel.send(f'**Subreddits:** Subreddits or “subs” are communities here on Reddit that you can join and engage with. There are thousands of subreddits on here, communities for pretty much every topic you can think of. Every sub on here has a “rule book” of sorts and you must abide by all of the rules of a sub or you risk getting a ban. You can find sub rules in the “about” section of a sub, community info/the sidebar or sometimes pinned to the homepage of a sub and if you use the app when you make a post the rules are in the post feature.')
        await ctx.channel.send(f'.')
        await ctx.channel.send(f'**Sorting:** **Hot** shows you posts that are popular and trending right now. **New** shows you posts that are just posted. **Top** shows you posts that have the most upvotes in a certain time period. **Controversial** shows you posts that have a lot of different opinions. RISING shows you posts that are getting more votes quickly and might end up being "Hot" soon.')
        await ctx.channel.send(f'.')
        await ctx.channel.send(f'''**Some common Reddit terms:**

    **Upvote** - A term equivalent to the like button on other platforms. This increases the Karma of the Redditor being upvoted. Each post has one upvote by default.

    **Post** - A media poost that you're bringing to reddit, whether it's yours or something found elsewhere on the Internet.

    **OC** - Original Coontent, AKA content of your own making.

    **Crosspost** - A link to yours or someone else's post from one subreddit to another.
                            
    **Multipost** - Where you make the same post in two or more different subreddits at the same time.
                            
    **Repost** - Where you take an old post (yours or someone else's) and post it again in the same subreddit.
                            
    **Downvote** - A term equivalent to dislike on other social networks.

    **Upvote** - A term equivalent to like on other social networks.

    **Community** - A subreddit.
                            
    **Awards** - These are community given awards which show on your post. The original ones are Silver, Gold and Platinum - each of them cost more but give the user more perks. Silver does nothing, like many of the other awards that have been recently deployed. These tend to cost 100 coins or less and come in loot boxes that appear in the mobile app sometimes for free! Some of the other awards, Gold and Platinum give the user a certain duration of Reddit Premium and some coins. There are also sub specific awards which usually give the subreddit moderators some coins tom give out to posts on that sub.''')

        await ctx.channel.send(f'''**Karma** - A approximation of the upvotes you get on posts and comments minus the downvotes. How many awards you get and the how many awards you are given and their type affect this score as well.

    **Trophies** - Trophies are displayed on your profile and are awarded for various tasks. For example you get a trophy when you verify your email and you also get a trophy for every year you are on Reddit. This is different from an award in the sense that is not awarded by your fellow Redditors.

    **Cakeday** - This is basically like a birthday for your Reddit account and happens every year on the day you created your account - just like a real birthday. You even get a little slice of cake next to your name for the day!

    **OP** - Original Poster. Refers to the person that posted the post you are commenting on.

    **NSFW** - Not Safe For Work content. You must be 18+ to view this content.

    **Snoo** - The Reddit alien mascot every user has.

    **Redditor** - A Reddit user.

    **Flair** - A subreddit-specific tag that is shown next to your name on that sub. Or it can be the tag of a post.

    **Mod** - Subreddit\'s each have their own moderators to keep the content on that sub within the rules and keep order. These people are all volunteers and exist on every single subreddit.

    **Admin** - Workers paid by Reddit who control the website and it\'s apps. You will see these people have a little Red Snoo logo next to their name They can do everything a mod can do but on a site wide scale.''')

        await ctx.channel.send(f'''**Shadowban** - A ban the Reddit Admins or the automatic spam filter give. You can continue to do everything you would usually do but nobody will see it.

    **Suspended** - A ban from Reddit (side wide) given by the Admins that lasts for a set number of days/permanently and the user will get a notification about this if they get suspended.

    **“/s”** - Used at the end of a sentence when sarcasm is attempted.

    **Throwaway account** - an alternate account that is not primarily used by the user.

    **TIL** - “Today I Learned”```''')
        await ctx.channel.send(f'.')
        await ctx.channel.send(f'''__**Here you can see the most popular communities of Reddit:**__ https://www.reddit.com/best/communities/1/''')
        print("Schnipper successfully executed help")
    except requests.Timeout as err:
                print("Schnipper timed out")

bot.run(TOKEN)
