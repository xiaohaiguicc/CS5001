import random as r
import sys
from deck import Deck
from hand import Hand


class GameController:
    """A controller for a simple blackjack game"""
    def __init__(self):
        self.deck = Deck()
        self.dealer_score = r.randint(17, 21) # dealer 的分数在17-21
        self.player_hand = Hand()

    def start_play(self):
        print("The dealer's score is", self.dealer_score)
        self.deal_two()
        self.display_hand()
        self.stay_or_hit(input("Would you like to stay or hit?\n"))

    def deal_two(self):
        # After two times shuffling, get two last cards. 两次洗牌，每次得到洗牌后最后一张牌
        self.player_hand.receive_card(self.deck.deal_one())
        self.player_hand.receive_card(self.deck.deal_one())

    def display_hand(self):
        self.player_hand.display() # 展示现在手上的牌

    def stay_or_hit(self, s_or_h):
        if s_or_h == "hit": # 要不要继续拿牌？
            self.player_hand.receive_card(self.deck.deal_one()) # 再拿一次洗牌后的最后一张
            self.display_hand()
            if self.player_is_bust(): # 如果击败dealer最大分数 21
                self.do_bust()
            else:
                self.stay_or_hit(input("Would you like to stay or hit?\n")) # 没有击败继续问
        elif s_or_h == "stay": # 如果不想继续拿牌
            self.do_stay() #直接现在的牌和dealer的分数比较
        else:
            self.stay_or_hit(input("Would you like to stay or hit?\n"))

    def player_is_bust(self):
        return self.player_hand.score() > 21 # 现在手上的牌的总值，是不是比21大

    def do_stay(self):
        if self.player_hand.score() > self.dealer_score:
            print("You Win!!!")
        elif self.player_hand.score() < self.dealer_score:
            print("You lose.")
        else:
            print("You tied.")
        sys.exit()

    def do_bust(self):
        print("*********************************")
        print("***          BUST!            ***")
        print("*********************************\n")
        sys.exit()