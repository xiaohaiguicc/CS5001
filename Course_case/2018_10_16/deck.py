import random as r
from card import Card


class Deck:
    """A standard deck of playing cards"""
    def __init__(self):
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        values = ['ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'jack', 'queen', 'king']
        self.cards = self.shuffle([Card(suit, value) # 洗牌后的所有牌的组合
                                   for suit in suits
                                   for value in values]) # two for loops means set A * B, all possible combinations between suits and values
                                                         # ex: [('hearts', 'ace'), ('hearts', '2'), ('hearts', '3'), ('hearts', '4'),....]

    def shuffle(self, cards): #洗牌
        list_range = range(0, len(cards))
        for i in list_range:
            j = r.randint(list_range[0], list_range[-1])
            cards[i], cards[j] = cards[j], cards[i]
        return cards

    def deal_one(self):
        return self.cards.pop() # return the last card 返回洗牌后最后一张牌