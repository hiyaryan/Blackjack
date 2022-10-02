# Dealer
# Object that represents the dealer.

from table.deck import Deck
from entity.hand import Hand

class Dealer(Hand):

    def __init__(self):
        '''
        Dealer has a stack of shuffled cards that it can deal. The number
        of decks is decided on initialzation of the dealer. 
        '''
        super().__init__("Dealer")
        self.deck = None

    
    def deal(self, role):
        '''
        Dealer deals a card from their stack of cards.
        '''
        # print(f"\tCard dealed to {role}.")
        return self.deck.remove_top_card()

    
    def new_deck(self):
        '''
        Provides the dealer with a new stack of cards.
        '''
        # print("\tDealer receives a new stack of cards.")
        self.deck = Deck()
        self.deck.shuffle()


    def check_deck(self):
        '''
        Ensure dealer has enouh cards in deck.
        '''
        if len(self.deck.deck) == 0:
            print("Dealer pulls new deck.\n")
            self.new_deck()         

    
    def clear_table(self, entities):
        '''
        Clears the table for all players.
        '''
        for entity in entities:
            entity.clear()

    
    def setup_table(self, entities):
        '''
        Sets up the table by giving all players one card.
        '''
        for entity in entities:
            self.check_deck() # Cards available in deck?
            entity.hit(self)  # Give initial card.
            entity.ready()    # Reset stand value.
            entity.total()    # Calculate hand value. 

    
    def __str__(self):
        return f"Dealer has {self.deck}.\n"
        
