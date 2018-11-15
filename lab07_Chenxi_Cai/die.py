"""defines the Die class representing a single die"""
import random as rnd


class Die:
    def __init__(self):
        """a single die"""
        self.current_value = 0

    def roll(self):
        """
        sets its current value
        to a random integer
        """
        self.current_value = rnd.randint(1, 6)
