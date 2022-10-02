# Card
# Object that represents a single card.

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}

symbols = {'Clubs': '♣', 'Spades': '♠', 'Hearts': '♥', 'Diamonds': '♦'}


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        self.symbol = symbols[suit]

    
    def __str__(self):
        return f"{self.value}{self.symbol} {self.rank} of {self.suit} {self.value}{self.symbol}"
