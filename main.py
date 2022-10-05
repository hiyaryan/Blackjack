# Blackjack
from simple_term_menu import TerminalMenu

from entity.hand import Hand
from entity.dealer import Dealer

# FIXE: Generalize dealer and player into entities
def play(dealer, player, entities):
    '''
    Game logic
    '''
    print("Welcome to Blackjack!\n\n")

    # Present menu to the player
    select = ""
    place_bet = True
    while select != 'Quit':
        # If bust the round ends and the opponent wins the round
        bust = False

        # Ensure dealer has enouh cards in deck
        dealer.check_deck()
        
        # Player does not stand
        if not bust and not player.stand:
            # Present hands
            print(dealer.view())
            print(player.view())

            # Place bet on first loop.
            if place_bet:

                # While loop opens Bet menu and only advances if bet is made.
                print(f"{player.role} place your bet.\n")
                while select != "Quit" and not player.account.subtract_tokens('B'):
                    select = player.account.menu()

                # Quits the entire game by breaking out of the loop.
                if select == "Quit":
                    break
                    
                # Dealer always matches the bet.
                dealer.account.subtract_tokens('B', tokens=player.account.bet)

                #Bets have been placed, do not ask again until new game.
                place_bet = False
            
            # Player turn
            select = menu()

            while select == "Bank":
                player.account.menu()
                select = menu()

            if select == "Hit":
                player.hit(dealer)
                player.total()

                # Check bust. If bust the table is cleared and reset.
                bust = check_bust(player)
                if bust:
                    place_bet = new_game(dealer, entities)

            elif select == "Stand":
                player.stay()
                select = ""  # Reset select

            elif select == "Quit":
                break

        # Ensure dealer has enouh cards in deck.
        dealer.check_deck()
            
        # Dealer turn
        if not bust and not dealer.stand:
            # Dealer will always hit if below 17.
            if dealer.value < 17:
                dealer.hit(dealer)
                dealer.total()

                # Check bust. If bust the table is cleared and reset.
                bust = check_bust(dealer)
                if bust:
                    place_bet = new_game(dealer, entities)

            # Dealer will always stand if 17 or above.
            else:
                dealer.stay()

        # If the dealer and player are both standing check win.
        if player.stand and dealer.stand:
            try:
                print(f"\t{check_win(dealer, player).role} WINS!\n")
            except AttributeError:
                print("\tDRAW!\n")
                
            place_bet = new_game(dealer, entities)

    if select == 'Quit':
        print("\n\tGoodbye.\n")


def check_win(dealer, player):
    '''
    Checks the game hand only after each player elects to stand. Awards winner
    with tokens bet on the table hands.
    '''
    # Reset stand for both dealer and player
    dealer.stand = False
    player.stand = False

    if dealer.value == player.value:
        return None
        
    if dealer.value > player.value:
        return dealer

    else:
        # TODO: Add mechanism to add tokens that were bet to Account.
        player.account.add_tokens("W", tokens=dealer.account.bet)
        return player


def check_bust(entity):
    '''
    Checks for the bust hand any time a player hits.
    '''
    if entity.value > 21:
        print(entity.view())
        print(f"\t{entity.role} BUST!\n\n")
        return True

    return False


def menu():
    '''
    Displays the menu and returns the selection
    '''
    options = ["[h] Hit", "[s] Stand", "[b] Bank", "[q] Quit"]
    options_dict = {0: 'Hit', 1: 'Stand', 2: "Bank", 3: 'Quit'}

    terminal_menu = TerminalMenu(options, title="\n- Blackjack -\n")
    selection = options_dict[terminal_menu.show()]

    return selection


def new_game(dealer, entities):
    '''
    Dealer clears and sets up a new game on the table.
    '''
    dealer.clear_table(entities)
    dealer.setup_table(entities)

    return True

    
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
