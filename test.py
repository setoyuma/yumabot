import error_lib
import random

ask_dice_num=int(input("dice num: "))
ask_dice_sides=str(input("dice type: "))
userName = 'seto'

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
    for dice_num in range(ask_dice_num):
        
        if ask_dice_sides in dice:

            for dice_sides in range(dice[ask_dice_sides]):

                sides.append(dice_sides)
                continue
            print(f'{userName} rolled: {random.choice(sides)}')
            continue
    if ask_dice_sides not in dice:
        print(error_lib.lib['invalid_dice_type'])
else:
    print(error_lib.lib['invalid_dice_num'])