'''
Francisco Pedro do Nascimento
DiceSimulator - Just a program that simulates a dice for RPG play
'''

from DiceSimulator import DiceSimulator

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.valid_dices = ["D4","D6","D8","D12","D20", "EXIT", "QUIT"]

    def selectSidesDice(self):
        index = -1

        while index < 0:
            dice = raw_input('Which dice do you want to roll? ')
            dice = dice.upper()
            if dice in self.valid_dices: index = self.valid_dices.index(dice)
            else: print('I\'m sorry is just avaible the options d4, d6, d8, d12 or d20')

        sides = 0
        if index > 4:
            exit()
        elif index == 0:
            sides = 4
        elif index == 1:
            sides = 6
        elif index == 4:
            sides = 20
        else:
            sides = index * 4

        return sides

    def run(self):
        simulator = DiceSimulator(1)
        while True:
            sides = self.selectSidesDice()
            simulator.setSides(sides)
            print(str(simulator.run()))

            roll_again = 'S'
            while roll_again.upper() == 'S':
                roll_again = raw_input('Do you want to rol again? [S/n]')
                if roll_again.upper() == 'S':
                    print(str(simulator.run()))

if __name__ == "__main__":
    Menu().run()
