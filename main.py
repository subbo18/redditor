from discord.ext import commands
TOKEN = "bot token"

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(command_prefix="/")

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

bot.run(TOKEN)

async def response(message):
    if  message.author == bot.User:
        return
    
    if message.content == "test":
        await message.channel.send(f'{message.author} hasnt showered since kurt cobain died')

    await bot.process_commands(message)

bot.run(TOKEN)
