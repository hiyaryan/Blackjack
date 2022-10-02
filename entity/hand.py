# Hand
# Object that represents the players hand.
class Hand():

    def __init__(self, role):
        '''
        The hand is a list of cards available to the player or dealer.
        The role describes if the player is a player or dealer. Stand
        indicates whether the player can be dealt cards.
        '''
        # if role == "Dealer":
        #     print(f"{role} opens the table.")
        # else:
        #     print(f"{role} sits at the table.")
        
        self.hand = []
        self.value = 0
        self.role = role
        self.stand = False

    
    def hit(self, dealer):
        '''
        Receive another card. 
        '''        
        if len(self.hand) != 0:
            print(f"\t{self.role} hits.\n")
            
        self.hand.append(dealer.deal(self.role))

    
    def stay(self):
        '''
        Player stands and will stop receiving cards.
        '''
        print(f"\t{self.role} stands.\n")
            
        self.stand = True

    
    def ready(self):
        '''
        Player is ready and can receive cards.
        '''
        self.stand = False

    
    def total(self):
        '''
        Calculates the value of the hand.
        '''
        total = 0
        # for card in self.hand:
        #     if total > 21:
        #         # This only works if the current card added to the value of
        #         # the hand making it greater than 21 is an Ace.
                
        #         if card.value == 14:
        #             card.value = 1
                    
        #             self.total() # retotal
        #             return

        #     # All other cards simply add value to total.
        #     else:
        #         total += card.value

        for card in self.hand:
            total += card.value        

        if total > 21:
            # This only works if the current card added to the value of
            # the hand making it greater than 21 is an Ace.
            for card in self.hand:
                if card.rank == "Ace" and card.value == 14:
                    card.value = 1
                    
                    self.total() # retotal
                    return

        self.value = total

    
    def clear(self):
        '''
        Clears the hand of cards. Called for every bust or win.
        '''
        self.hand = []

    
    def view(self):
        '''
        Presents the hand. 
        '''

        # Concatenating string representation of Card objects.
        index = ""
        for card in self.hand:
            index += f"\t{card}\n"

        return f"୭ {self.role} Hand\n\n{index}\n\t ✧ {self.value} ✧\n\n"

    
    def __str__(self):
        return f"{self.role} has {len(self.hand)} in hand."