import discord
from discord.ext import commands

# Create a bot instance with command prefix '!'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('Bot is ready to use!')

# Command: Ping
@bot.command()
async def ping(ctx):
    """Responds with the bot's latency"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! 🏓 Score: {latency}')

# Command: Hello
@bot.command()
async def hello(ctx):
    """Sends a hello message"""
    await ctx.send(f'Hello {ctx.author.display_name}! 👋')

# Command: Rook
@bot.command()
async def rook(ctx):
    """Responds with the bot's commands"""
    await ctx.send(f"""Hiyas!
* !commands - command list
""")

# Command: Commands
@bot.command()
async def commands(ctx):
    """Responds with the bot's commands"""
    await ctx.send(f"""Sure!
* !ping - test ping
* !news - lodestone news
* !fr - fashion report
* !hello - greeting
* !beerme
* !cheers
* !earwiggle
* !watermelon
""")

# Command: Fashion
@bot.command()
async def fr(ctx):
    """Sends an fr message"""
    await ctx.send(f'Right away {ctx.author.display_name}!')

# Command: Ear
@bot.command()
async def earwiggle(ctx):
    """Sends an ear message"""
    await ctx.send(f'*wiggles ears*')

# Command: Ears
@bot.command()
async def earwiggles(ctx):
    """Sends an ear message"""
    await ctx.send(f'*wiggles ears*')

# Command: Beer
@bot.command()
async def beerme(ctx):
    """Sends a beer message"""
    await ctx.send(f"""*slides you a beer*
Cheers {ctx.author.display_name}! 🍻
""")

# Command: Cheers
@bot.command()
async def cheers(ctx):
    """Sends a beer message"""
    await ctx.send(f"""*slides you a beer*
Cheers {ctx.author.display_name}! 🍻
""")

# Command: News
@bot.command()
async def news(ctx):
    """Sends the news"""
    await ctx.send(f"""*tosses newspaper* 🗞️
<https://discord.com/channels/869999933934145578/870028217375940670>
""")

# Command: watermelon
@bot.command()
async def watermelon(ctx):
    """Sends a wm message"""
    await ctx.send(f'*Where the hell is it?*')

# Command: gunblade
@bot.command()
async def gunblade(ctx):
    """Sends a wm message"""
    await ctx.send(f'*Polishes a gunblade and hands it over* 💥')

# Command: treesave
@bot.command()
async def treesave(ctx):
    """Sends a wm message"""
    await ctx.send(f'*Helps a miqo get out of a tree*')

# Command: tree
@bot.command()
async def tree(ctx):
    """Sends a wm message"""
    await ctx.send(f'*Helps a miqo get out of a tree*')

# Command: smiles
@bot.command()
async def smiles(ctx):
    """Sends a wm message"""
    await ctx.send(f"""*Gives everyone a smile* 
Rook is on the job!
""")

# Command: rock
@bot.command()
async def rock(ctx):
    """Sends a wm message"""
    await ctx.send(f'*Gives Tiny Kitty a rock to snack on* 🪨')

# Command: effort
@bot.command()
async def effort(ctx):
    """Sends a wm message"""
    await ctx.send(f"""*Rook gives maximum effort!*
HNNNGGAAAHHH!
""")

# Command: healer
@bot.command()
async def healer(ctx):
    """Sends a wm message"""
    await ctx.send(f'*Rook gets out the dinosaur band-aids*')

# Run the bot
bot.run('BOT_TOKEN')
