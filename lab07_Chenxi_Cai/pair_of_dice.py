"""Defines the class PairOfDice which has two Die class attributes"""
from die import Die


class PairOfDice:
    """A pair of dice"""
    def __init__(self):
        """constructor"""
        self.die1 = Die()
        self.die2 = Die()

    def roll_dice(self):
        """Roll two dices, return sum"""
        value = self.current_value(self.die1) + self.current_value(self.die2)
        return value

    def current_value(self, die):
        """Assign and return die current value"""
        die.roll()
        return die.current_value
