from table.card import Card
from table.deck import Deck
from entity.hand import Hand
from entity.dealer import Dealer

# Card object tests
# ----------------------------------------
seven_of_diamonds = Card("Seven", "Diamonds")
print(seven_of_diamonds)

queen_of_hearts = Card("Queen", "Hearts")
print(queen_of_hearts)
# ----------------------------------------

# Deck object tests
# ----------------------------------------
new_deck = Deck()
print(new_deck)

print()

for card in new_deck.deck:
    print(card)
    
new_deck.shuffle()
print(f"Shuffle 1: {new_deck.deck[-1]}")

new_deck.shuffle()
print(f"Shuffle 2: {new_deck.deck[-1]}")

new_deck.shuffle()
print(f"Shuffle 3: {new_deck.deck[-1]}")

for card in new_deck.deck:
    print(card)
    
print()

# Removed number_of_decks since dealer can simply create a new deck.
# new_deck_two = Deck(number_of_decks=2) 
# print(new_deck_two)

print()
# ----------------------------------------

# Hand object tests
# ----------------------------------------
player = Hand("Player")

player.hand.append(seven_of_diamonds)
player.hand.append(queen_of_hearts)

print(player)
print(player.view())

# player.hit(Card("Two", "Hearts"))
print(player)

player.stay()
print(player)


# Dealer object tests
# ----------------------------------------
dealer = Dealer()
dealer.new_deck()
print(dealer)

player.hit(dealer)
print(player)

print(dealer)
dealer.new_deck()

print(dealer)