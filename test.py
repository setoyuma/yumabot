import random
ask = input('\n\twhat are you rolling <d20, d12, d10, d8, d6, d4>:  ')

def setSides(ask:str):


    sides=[]
    dice = {
        'd20':20,
        'd12':12,
        'd10':10,
        'd8':8,
        'd6':6,
        'd4':4,
    }

    if ask in dice:
        for i in range(dice[ask]):
            sides.append(i)
        # print(dice[ask])
        print(f'USER.NAME Rolled: {random.choice(sides)}')
    if ask not in dice:
        print('ERROR#600:invalid_dice_type')

setSides(ask)

