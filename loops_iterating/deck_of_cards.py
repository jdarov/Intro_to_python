suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = [f'{rank} of {suit}\n' for suit in suits for rank in ranks]

print("".join(deck))
print(deck)
