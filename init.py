'''
Francisco Pedro do Nascimento
DiceSimulator - Just a program that simulates a dice for RPG play
'''

from DiceSimulator import DiceSimulator

valid_dices = ['D4','D6','D8','D12','D20']

def selectSidesDice():
    index = -1

    while index < 0:
        dice = input('Which dice do you want to roll? ')
        dice = dice.upper()
        try:
            index = valid_dices.index(dice)
        except ValueError:
            print('I\'m sorry is just avaible the options d4, d6, d8, d12 or d20')

    sides = 0
    if index == 0:
        sides = 4
    elif index == 1:
        sides = 6
    elif index == 4:
        sides = 20
    else:
        sides = index * 4

    return sides

def main():
    sides = selectSidesDice()
    print(sides)


main()