# yuma.py
#written by seto yuma#
import os
import datetime
import getpass
import time as t
import discord as d
from discord import app_commands
from discord.ext import commands
import random

from dotenv import load_dotenv
load_dotenv()

'''intent setup'''
intents = d.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True
# intents.all = True

'''bot vars'''
TOKEN=os.getenv('DISCORD_TOKEN')
ADMINK=os.getenv('ADMINK')
ADMINKGET = getpass.getpass(prompt='\n\tenter admin key:')
yumabot=commands.Bot(command_prefix='r/', intents=intents)
# yumabot=d.Client(intents=intents)
# TREE=app_commands.CommandTree(yumabot)
with open('skull.txt','r') as skullF:
    SKULLYBOI = skullF.read()
    
'''yumabot events'''
@yumabot.event
async def on_ready():
    # await TREE.sync()
    print('\n\n\t\tyumabot ascii art\n\n')
    t.sleep(2)
    print(f'\n\t{yumabot.user.name} is online...\n')

'''yumabot commands'''
'''
test slash command:

@TREE.command(name='speak',description='yumabot talk')
async def yuma_speak(interaction):
    await interaction.response.send_message('what bozo')'''

@yumabot.command(name='tweak',help='yumabot says something out of the box')
async def yuma_tweak(ctx)->str:
    scuffed_responses = [
        'AHHHHHHHHHHHH AHHHHH AHHHHHHHHAHAHAHHHH',
        'bitch',
        'you think they want you drinkin coconut water?',
        'so where do gummy bears come from???',
        'if i cant smell it, must taste neutral',
        'someone hit the lights',
        '(/-_-)/',
        'we tweakin???',
        'HOLY FUCK ITS ROBERT',
        "i'd fry you in bell ball.",
        'ok.',
        f'{SKULLYBOI}'
    ]

    response = random.choice(scuffed_responses)
    await ctx.send(response)
    return response

# dice roll commands
def throw_dice(side_query)->str:
    sides = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    return(str(random.choice(sides)))

@yumabot.command(name='roll',help='rolls a 20 sided die')
async def yuma_d20(ctx)->None:    

    querey_dice = int(input('# of dice (max 2):'))        
    dice = querey_dice     

    for i in range(dice):
        await ctx.send(f'{ctx.message.author.name}Roll #{i}: {throw_dice(dice)}\t|| ')


'''yumabot/user_interactive embeds'''
@yumabot.command(name='yumahelp',help='a more comprehensive explanation of yumabot and its commands')
async def yuma_help_embed(ctx):
    embed=d.Embed(
        title='***YUMAHELP***',
        type='rich',
        url='https://www.github.com/setoyuma',
        description='learning embeds',
        color=d.Color.blurple()
        )
    embed.set_author(name=f'{yumabot.user.name}',url='https://github.com/setoyuma',icon_url='https://avatars.githubusercontent.com/u/118138305?v=4')
    
    #thumbnail
    embed.set_thumbnail(url='https://avatars.githubusercontent.com/u/118138305?v=4')

    #fields
    embed.add_field(
        name='***commands***',
        value='*---*',
        inline=False
    )

    embed.add_field(
        name='format:\n<command>',
        value='<description of command>',
        inline=False
        )
    
    embed_line_break = embed.add_field(name='_',value='_',inline=False)

    embed.add_field(
        name='r/d20',
        value='rolls a 20 sided die',
        inline=True
        )

    embed.add_field(
        name='r/tweak',
        value='yumabot says something (generally)out of pocket.',
        inline=True
        )



    await ctx.send(embed=embed)


'''yumabot config functions'''
def runyuma(spawn,admink:str)->bool:
    if admink.capitalize() != ADMINK:
        print('\n\tyumabot startup failed...\n\n\t\tinvalid key:',ADMINKGET)
        t.sleep(3)
        #log admin failures in adminlogin_fail.txt
        os.system('clear')
        return False
    if admink.capitalize() == ADMINK:
        spawn.run(TOKEN)
        return True

if __name__ == '__main__':
    runyuma(yumabot,ADMINKGET)
