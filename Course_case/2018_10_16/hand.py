class Hand:
    """A blackjack hand"""
    def __init__(self):
        self.number_of_aces = 0
        self.cards = []

    def receive_card(self, card):
        if card.value == "ace":
            self.number_of_aces += 1 # 计算ace牌的个数
        self.cards.append(card) # list of card object, 保存牌

    def score(self):
        s = sum([c.num_value() for c in self.cards])
        if s > 21:
            s = s - self.number_of_aces * 10
        return s # 计算牌的分数

    def display(self):
        print("Player hand:")
        for c in self.cards:
            print("\tThe", c.value, "of", c.suit) # 展示手上的牌