suits = ['hearts', 'spades', 'diamonds', 'clubs']
values = ['ace', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'jack', 'queen', 'king']

cards = [(suit, value) for suit in suits for value in values]
print(cards)