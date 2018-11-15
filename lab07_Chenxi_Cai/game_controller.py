"""manage the rolling, scoring, and user interaction"""

import sys
from pair_of_dice import PairOfDice


class GameController:
    """"A controller for street craps game"""
    def __init__(self):
        self.dice = PairOfDice()
        self.first_value = 0

    def start_play(self):
        """Whole game process"""
        self.first_value = self.roll()
        self.first_rule(self.first_value)
        self.second_rule()

    def roll(self):
        """return rolled values"""
        input("Press enter to roll the dice...\n")
        value = self.dice.roll_dice()
        return value

    def first_rule(self, first_value):
        """Rule for first rolling value"""
        win_list = [7, 11]
        lose_list = [2, 3, 12]
        if first_value in win_list:
            print("You rolled {}. You win!".format(first_value))
            sys.exit()
        elif first_value in lose_list:
            print("You rolled {}. You lose.".format(first_value))
            sys.exit()
        else:
            print("Your point is", first_value)

    def second_rule(self):
        """Rules for later roll"""
        value = self.roll()
        while(value != self.first_value and value != 7):
            print("You rolled", value)
            value = self.roll()
        if value == self.first_value:
            print("You rolled {}. You win!".format(value))
        elif value == 7:
            print("You rolled 7. You lose.")
        sys.exit()
