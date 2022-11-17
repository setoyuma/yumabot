import os
import discord as d
from discord.ext import commands
import random

from dotenv import load_dotenv
load_dotenv()

#intent setup
intents = d.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True
# intents.all = True

TOKEN = os.getenv('DISCORD_TOKEN')
yumabot = commands.Bot(command_prefix='r/', intents=intents)

@yumabot.event
async def on_ready():
    print(f'\n\t{yumabot.user.name} is online...\n')

@yumabot.command(name='tweak',help='yumabot says something out of the box')
async def yuma_tweak(ctx):
    scuffed_responses = [
        'AHHHHHHHHHHHH AHHHHH AHHHHHHHHAHAHAHHHH',
        'bitch',
        'you think they want you drinkin coconut water?',
        'so where do gummy bears come from???',
        'if i cant smell it, must taste neutral',
        'someone hit the lights'
    ]

    response = random.choice(scuffed_responses)
    await ctx.send(response)

@yumabot.command(name='d20',help='rolls a 20 sided die')
async def yuma_d20(ctx):
    sides = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    player_roll = random.choice(sides)
    await ctx.send(f'\t{ctx.message.author.name} Rolled {str(player_roll)}\n')

if __name__ == '__main__':
    yumabot.run(TOKEN)
