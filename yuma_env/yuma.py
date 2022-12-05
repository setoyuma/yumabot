# yuma.py
#written by seto yuma#
import urllib.request
from PIL import Image as PILimg
import os
import datetime
import getpass
import time as t
import interactions as spawn
import random
import error_lib
from apiMAIN import get_meme,check_image
from dotenv import load_dotenv
load_dotenv()


'''intent setup'''
# intents = d.Intents.default()
# intents.message_content = True
# intents.messages = True
# intents.members = True
# intents.all = True

'''bot vars'''
TOKEN=os.getenv('TKN')
ADMINK=os.getenv('ADMINK')
DEV_SERVER_ID=int(os.getenv('DEV_SERVER_ID'))
ALT_DEV_SERVER_ID=int(os.getenv('ALT_DEV_SERVER_ID'))
STREAM_SERVER_ID=int(os.getenv('STREAM_SERVER_ID'))
PRIV_SERVER_ID=int(os.getenv('PRIV_SERVER_ID'))
server_ids = {
    "dev":DEV_SERVER_ID,
    "alt":ALT_DEV_SERVER_ID,
    "stream":STREAM_SERVER_ID,
    "priv":PRIV_SERVER_ID,
}
adjectives = [
    "fresh",
    "fire",
    "flaming",
    "obscure",
    "THE",
    "40g of",
    "1 millivanilligram of",
    "MF",
    "just a",
    "calculated",
    "retrieved",
    "aquired",
    "2000IQ",
    "big boy",
    "big brain",
]

ADMINKGET = getpass.getpass(prompt='\n\tenter admin key:')
yumaden=spawn.Client(token=TOKEN)
with open('logo_ascii.txt', 'r') as logoF:
    ASCII_LOGO=logoF.read()
with open('skull.txt','r') as skullF:
    SKULLYBOI = skullF.read()


'''yumaden events'''

@yumaden.event
async def on_ready():
    os.system('cls')
    print(f'\n\n\t\t{ASCII_LOGO}\n\n')
    t.sleep(2)
    print(f'\n\t{yumaden.me.name} is online...\n')


'''yumaden commands'''
#meemdex
@yumaden.command(name='memer',scope=server_ids['alt'])
async def yuma_memer(ctx:spawn.CommandContext):
    await ctx.send(
        "hi"
        )

@yumaden.command(
    name='ymeme',
    scope=server_ids['alt'],
    options=[
        spawn.Option(
            name='what_subreddit',
            description='where i pull meem from?',
            type=spawn.OptionType.STRING,
            required=True
    
            ),
        # spawn.Option(
        #     name='how_many_meem',
        #     description='how many meem u need',
        #     type=spawn.OptionType.INTEGER,
        #     required=True
        #     ),
        ]
    )
async def yumaMeme(ctx:spawn.CommandContext,what_subreddit):
    memeEmbed=spawn.Embed(
        title=f'{random.choice(adjectives)} meme',
        type='rich',
        color=spawn.Color.white()
    )
    memeEmbed.set_author(
        name=f'{yumaden.me.name}',
        url='https://github.com/setoyuma',
        icon_url='https://cdn.discordapp.com/avatars/1042644929056358490/aa1e879a74cebcbab3f61a70a81001a7.png?size=256'
    )
    # memeEmbed.set_thumbnail(
    #     url='https://cdn.discordapp.com/avatars/1042644929056358490/aa1e879a74cebcbab3f61a70a81001a7.png?size=256'
    # )
    fetchedMeme = get_meme(what_subreddit,150)[random.randint(0,149)]
    re_meme_attempts=0
    if check_image(fetchedMeme["Url"]):
        memeEmbed.set_image(
            url=f"{fetchedMeme['Url']}",
            width=500,
            height=500,
        )
        await ctx.send(embeds=memeEmbed)
    # else:
    #     await ctx.send("that post wasn't an image.\t{ working on handling text posts}\n***try again :)***\n")

@yumaden.command(name='mirror',scope=server_ids['alt'])
@spawn.option(name='blurb',description='says it back',required=False)
async def say_something(ctx: spawn.CommandContext, blurb: str):
    """speak bitch"""
    await ctx.send(f"You said '{blurb}'!")

#roll command
@yumaden.command(
    name='yroll',
    scope=server_ids['alt'],
    options=[
        spawn.Option(
            name='ask_dice_num',
            description='how many dice -> ( 1 or 2 )',
            type=spawn.OptionType.INTEGER,
            required=True
            ),
        spawn.Option(
            name='ask_dice_sides',
            description='pick and roll -> ( d20, d12, d10, d8, d6, d4 )',
            type=spawn.OptionType.STRING,
            required=True
            ),
        ]
    )
async def yuRoll(ctx: spawn.CommandContext,ask_dice_num,ask_dice_sides):
    """\n\twhat are you rolling -> ( d20, d12, d10, d8, d6, d4 )  """
    sides = []
    dice = {
        'd20':20,
        'd12':12,
        'd10':10,
        'd8':8,
        'd6':6,
        'd4':4,
    }

    if ask_dice_num > 0 and ask_dice_num < 3:
        
        if ask_dice_sides in dice:

            for dice_sides in range(dice[ask_dice_sides]):

                sides.append(dice_sides)
                continue

            if int(ask_dice_num) == 1:
                await ctx.send(f'{ctx.author.name} rolled a: {random.choice(sides)}')

            elif int(ask_dice_num) == 2:
                await ctx.send(f'{ctx.author.name} rolled a: {random.choice(sides)}  --|--  {random.choice(sides)}')

        if ask_dice_sides not in dice:
            await ctx.send(error_lib.lib['invalid_dice_type'])
    else:
        await ctx.send(error_lib.lib['invalid_dice_num'])
    

@yumaden.command(name='yc',description='yumaden says something out of the box',scope=server_ids['alt'])
async def yuComment(ctx:spawn.CommandContext)->str:
    scuffed_responses = [
        'AHHHHHHHHHHHH AHHHHH AHHHHHHHHAHAHAHHHH',
        'bitch',
        'you think they want you drinkin coconut water?',
        'so where do gummy bears come from???',
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


'''yumaden/user_interactive embeds'''
@yumaden.command(name='yhelp',description='an in-depth explanation of yumaden and its commands',scope=server_ids['alt'])
async def yuHelp(ctx:spawn.CommandContext):
    embed=spawn.Embed(
        title='***YUMAHELP***',
        type='rich',
        url='https://www.github.com/setoyuma',
        description='description of yumabot and its functions',
        color=spawn.Color.white()
        )
    embed.set_author(
        name=f'{yumaden.me.name}',
        url='https://github.com/setoyuma',
        icon_url='https://cdn.discordapp.com/avatars/1042644929056358490/aa1e879a74cebcbab3f61a70a81001a7.png?size=256'
        )
    
    #thumbnail  
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/avatars/1042644929056358490/aa1e879a74cebcbab3f61a70a81001a7.png?size=256'
        )

    #fields
    ###
    #header
    embed.add_field(
        name='***commands***',
        value='*---*',
        inline=False
    )

    ###
    #bot overview section (in progress)
    ###
    '''embed.add_field(
        name='format:\n<command>',
        value='<description of command>',
        inline=False
        )'''
    
    embed_line_break = embed.add_field(name='_',value='_',inline=False)

    #roll
    embed.add_field(
        name='/yroll',
        value='/yroll (yumaRoll) will tell yumaBot to roll *n* number of dice and  the number of sides can be chosed by typing d"*x*" where x can be 4,6,8,10,12,or 20',
        inline=True
        )
    #tweak
    embed.add_field(
        name='/yc',
        value='/yc (yumaComment) causes yumaden to something (generally) out of pocket.',
        inline=True
        )
    #meem
    embed.add_field(
        name='/ymeme',
        value='/ymeme (yumaMeme) causes yumaBot to generate a pool of 150 memes and randomply picks one to give u from a subreddit you choose.\n\t(command wont work if you dont specify a subreddit) ',
        inline=True
        )

    await ctx.send(embeds=embed)


'''yumaden config functions'''
def runyuma(spawn,admink:str)->bool:
    if admink.capitalize() != ADMINK:
        print('\n\tyumaden startup failed...\n\n\t\tinvalid key:')
        t.sleep(3)
        #log admin failures in adminlogin_fail.txt
        os.system('cls')
        return False
    if admink.capitalize() == ADMINK:
        spawn.start()
        return True

if __name__ == '__main__':
    runyuma(yumaden,ADMINKGET)
