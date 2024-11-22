import discord
from discord import app_commands
from random import randint

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Bot is ready!")
    try:
        await tree.sync(guild=None)  # None means global sync
        print("Synced globally")
    except Exception as e:
        print(e)

# Command: rook
@tree.command(name="rook", description="Says hi")
async def rook(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hiyas!')

# Command: Ear
@tree.command(name="earwiggle", description="wiggles ears")
async def earwiggle(interaction: discord.Interaction):
    await interaction.response.send_message(f'*wiggles ears*')

# Command: Beer
@tree.command(name="beerme", description="Passes you a beer")
async def beerme(interaction: discord.Interaction):
    await interaction.response.send_message(f"""*slides you a beer*
Cheers {interaction.user.display_name}! 🍻
""")

# Command: Beer
@tree.command(name="beerdjorick", description="Passes Djorick a beer")
async def beerdjorick(interaction: discord.Interaction):
    await interaction.response.send_message(f"""*slides Djorick a beer*
Have a cold one, Mr. Bairon! 🍻
""")

# Command: Cheers
@tree.command(name="cheers", description="Passes you a beer")
async def cheers(interaction: discord.Interaction):
    await interaction.response.send_message(f"""*slides you a beer*
Cheers {interaction.user.display_name}! 🍻
""")

# Command: News
@tree.command(name="news", description="Links to the news channel")
async def news(interaction: discord.Interaction):
    await interaction.response.send_message(f"""*tosses newspaper* 🗞️
[Lodestone News](<https://discord.com/channels/869999933934145578/870028217375940670>)
""")

# Command: watermelon
@tree.command(name="watermelon", description="Watermelon")
async def watermelon(interaction: discord.Interaction):
    await interaction.response.send_message(f'*Where the hell is it?*')

# Command: gunblade
@tree.command(name="gunblade", description="Gunblade")
async def gunblade(interaction: discord.Interaction):
    await interaction.response.send_message(f'*Polishes a gunblade and hands it over* 💥')

# Command: treesave
@tree.command(name="treesave", description="Saves a kitty")
async def treesave(interaction: discord.Interaction):
    await interaction.response.send_message(f'*Helps a miqo get out of a tree*')

# Command: smiles
@tree.command(name="smiles", description="Smiles")
async def smiles(interaction: discord.Interaction):
    await interaction.response.send_message(f"""*Gives everyone a smile* 
Rook is on the job!
""")

# Command: rock
@tree.command(name="rock", description="Feed Tiny Kitty")
async def rock(interaction: discord.Interaction):
    await interaction.response.send_message(f'*Gives Tiny Kitty a rock to snack on* 🪨')

# Command: heal
@tree.command(name="heal", description="Heals")
async def heal(interaction: discord.Interaction):
    await interaction.response.send_message(f'*Gets out the dinosaur band-aids* 🩹')

# Command: morb
@tree.command(name="morbol", description="Releases some morbols")
async def morbol(interaction: discord.Interaction):
    await interaction.response.send_message(f'*{randint(1,100)} morbols released from the FC chest*')

# Command: incin
@tree.command(name="incinerate", description="Incinerates some morbols")
async def incinerate(interaction: discord.Interaction):
    await interaction.response.send_message(f'*{randint(2,100)} morbols incinerated* :fire:')

# Command: burn
@tree.command(name="burn", description="Incinerates some morbols")
async def burn(interaction: discord.Interaction):
    await interaction.response.send_message(f'*{randint(2,100)} morbols incinerated* :fire:')

# Command: nap
@tree.command(name="nap", description="Naps")
async def nap(interaction: discord.Interaction):
    await interaction.response.send_message(f':sleeping: zzz...')

# Command: evolve
#@tree.command(name="evolve", description="Evolve")
#async def nap(interaction: discord.Interaction):
#    await interaction.response.send_message(f"""*...? Rook is evolving!* 
#...
#...
#...!
#Rook forgot ! commands.
#Rook learned / commands!
#""")

client.run('BOT_TOKEN')
