# yuma.py
#written by seto yuma#
import os
import datetime
import getpass
import time as t
import interactions as spawn
import random
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
ADMINKGET = getpass.getpass(prompt='\n\tenter admin key:')
# yumaden=commands.Bot(command_prefix='r/', intents=intents)
yumaden=spawn.Client(token=TOKEN)
with open('skull.txt','r') as skullF:
    SKULLYBOI = skullF.read()



'''yumaden class'''
@yumaden.event
async def on_ready():
    print('\n\n\t\tyumaden ascii art\n\n')
    t.sleep(2)
    print(f'\n\t{yumaden.me.name} is online...\n')

'''yumaden commands'''
@yumaden.command(name='mirror',scope=DEV_SERVER_ID)
@spawn.option(name='blurb',description='says it back',required=False)
async def say_something(ctx: spawn.CommandContext, blurb: str):
    """speak bitch"""
    await ctx.send(f"You said '{blurb}'!")

#roll command
@yumaden.command(name='roll',scope=DEV_SERVER_ID)
@spawn.option(name='ask_dice_sides',description='pick and roll -> ( d20, d12, d10, d8, d6, d4 )',required=True)
async def yuma_roll(ctx: spawn.CommandContext, ask_dice_sides: str):
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

    if ask_dice_sides in dice:
        for i in range(dice[ask_dice_sides]):
            sides.append(i)
            # print(dice[ask])
        await ctx.send(f'{ctx.author.name} rolls a: {random.choice(sides)}')
    if ask_dice_sides not in dice:
        import error_lib
        await ctx.send(error_lib.lib["invalid_dice_type"])
    

@yumaden.command(name='tweak',description='yumaden says something out of the box',scope=DEV_SERVER_ID)
async def yuma_tweak(ctx:spawn.CommandContext)->str:
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


'''yumaden/user_interactive embeds'''
@yumaden.command(name='yumahelp',description='an in-depth explanation of yumaden and its commands',scope=DEV_SERVER_ID)
async def yuma_help_embed(ctx:spawn.CommandContext):
    embed=spawn.Embed(
        title='***YUMAHELP***',
        type='rich',
        url='https://www.github.com/setoyuma',
        description='learning embeds',
        color=spawn.Color.blurple()
        )
    embed.set_author(
        name=f'{yumaden.me.name}',
        url='https://github.com/setoyuma',
        icon_url='https://avatars.githubusercontent.com/u/118138305?v=4'
        )
    
    #thumbnail  
    embed.set_thumbnail(
        url='https://avatars.githubusercontent.com/u/118138305?v=4'
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
        name='/roll',
        value='rolls a dice where x is the number of sides. choose a dice "type" by typeing d"x" . x can be 4,6,8,10,12,or 20',
        inline=True
        )
    #tweak
    embed.add_field(
        name='/tweak',
        value='yumaden says something (generally) out of pocket.',
        inline=True
        )



    await ctx.send(embeds=embed)


'''yumaden config functions'''
def runyuma(spawn,admink:str)->bool:
    if admink.capitalize() != ADMINK:
        print('\n\tyumaden startup failed...\n\n\t\tinvalid key:',ADMINKGET)
        t.sleep(3)
        #log admin failures in adminlogin_fail.txt
        os.system('cls')
        os.system('clear')
        return False
    if admink.capitalize() == ADMINK:
        spawn.start()
        return True

if __name__ == '__main__':
    runyuma(yumaden,ADMINKGET)
