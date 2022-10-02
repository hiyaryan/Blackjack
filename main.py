# Blackjack
from simple_term_menu import TerminalMenu

from entity.hand import Hand
from entity.dealer import Dealer

# TODO: Create banking system for player/dealer. 

# FIXE: Generalize dealer and player into entities
def play(dealer, player, entities):
    '''
    Game logic
    '''
    print("Welcome to Blackjack!\n\n")

    # Present menu to the player
    select = ""
    while select != 'Quit':
        # If bust the round ends and the opponent wins the round
        bust = False

        # Ensure dealer has enouh cards in deck
        # if len(dealer.deck.deck) == 0:
        #     print("Dealer pulls new deck.\n")
        #     dealer.new_deck()
        dealer.check_deck()
        
        # Player does not stand
        if not bust and not player.stand:
            # Present hands
            print(dealer.view())
            print(player.view())

            # Player turn
            select = menu()

            if select == "Hit":
                player.hit(dealer)
                player.total()

                # Check bust. If bust the table is cleared and reset.
                bust = check_bust(player)
                if bust:
                    new_game(dealer, entities)

            elif select == "Stand":
                player.stay()
                select = ""  # Reset select


         # Ensure dealer has enouh cards in deck
        # if len(dealer.deck.deck) == 0:
        #     print("Dealer pulls new deck.\n")
        #     dealer.new_deck() 
        dealer.check_deck()
            
        # Dealer turn
        if not bust and not dealer.stand:
            # Dealer will always hit if below 17
            if dealer.value < 17:
                dealer.hit(dealer)
                dealer.total()

                # Check bust. If bust the table is cleared and reset.
                bust = check_bust(dealer)
                if bust:
                    new_game(dealer, entities)

            # Dealer will always stand if 17 or above
            else:
                dealer.stay()

        # If the dealer and player are both standing check win.
        if player.stand and dealer.stand:
            try:
                print(f"\t\t{check_win(dealer, player).role} WINS!\n")
            except AttributeError:
                print("\t\tDRAW!\n")
                
            new_game(dealer, entities)

    if select == 'Quit':
        print("\tGoodbye.")


def check_win(dealer, player):
    '''
    Checks the game hand only after each player elects to stand.
    '''
    # Reset stand for both dealer and player
    dealer.stand = False
    player.stand = False

    if dealer.value == player.value:
        return None
        
    if dealer.value > player.value:
        return dealer

    else:
        return player


def check_bust(entity):
    '''
    Checks for the bust hand any time a player hits.
    '''
    if entity.value > 21:
        print(entity.view())
        print(f"\t\t{entity.role} BUST!\n\n")
        return True

    return False


def menu():
    '''
    Displays the menu and returns the selection
    '''
    options = ["[h] Hit", "[s] Stand", "[q] Quit"]
    options_dict = {0: 'Hit', 1: 'Stand', 2: 'Quit'}

    terminal_menu = TerminalMenu(options, title="\n- Blackjack -\n")
    selection = options_dict[terminal_menu.show()]

    return selection


def new_game(dealer, entities):
    '''
    Dealer clears and sets up a new game on the table.
    '''
    dealer.clear_table(entities)
    dealer.setup_table(entities)

    
def initialize():
    '''
    Initialize the game with a dealer and a player.
    '''
    # print("Initializing game...\n")

    dealer = Dealer()
    dealer.new_deck()

    player = Hand("Player")

    entities = [dealer, player]
    dealer.setup_table(entities)

    play(dealer, player, entities)


if __name__ == '__main__':
    initialize()
