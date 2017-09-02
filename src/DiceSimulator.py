'''
Francisco Pedro do Nascimento
DiceSimulator - Just a program that simulates a dice for RPG play
'''
import random

class DiceSimulator:
    dice_sides = 1

    def __init__(self, sides):
        self.dice_sides = sides
        if sides < 1: self.dice_sides = 1

    def setSides(self, sides):
        self.dice_sides = sides

    def run(self):
        return random.randrange(1, self.dice_sides+1) 