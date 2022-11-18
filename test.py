import random

sides = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def throw_dice()->str:
    print((random.choice(sides)))


def roll(dice):
    for i in range(dice):
        throw_dice()

roll(2)