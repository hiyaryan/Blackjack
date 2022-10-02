# Deck
# Object that represents a collection of 52 cards.
from table.card import Card
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:

    def __init__(self):
        '''
        Constructs this deck by creating a list of 52 unique cards based on 
        the suits and ranks.
        '''
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(rank, suit))

    
    def shuffle(self):
        '''
        Shuffles this deck using the shuffle method in the random library.
        '''
        random.shuffle(self.deck)

    
    def remove_top_card(self):
        '''
        Pops the first card off the deck removing in from the stack.
        '''
        return self.deck.pop()


    def deck_len(self):
        '''
        Returns the length of the deck.
        '''
        
    
    
    def __str__(self):
        '''
        Prints the number of decks representing this object.
        '''
        return f"{len(self.deck)} cards in the deck"
