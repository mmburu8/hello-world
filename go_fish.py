import random
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
shapes = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
fulldeck = []
def build_deck():
    for shape in shapes:
        for value in values:
            deckstar = value + ' of ' + shape
            fulldeck.append(deckstar)
build_deck()
#random.shuffle(fulldeck)
x = random.choice(fulldeck)
fulldeck.remove(x)
y = random.choice(fulldeck)
def get_suit(card):
    suit = card[:1]
    return suit

def get_value(card):
    value = card[5:]
    print(value)
    return value
m = get_value(x)
n = get_value(y)

def same_value(card_1, card_2):
    value_comparison = card_1 == card_2
    print(value_comparison)
same_value(m, n)
r = get_suit(x)
s = get_suit(y)
def same_suit(card_3, card_4):
    suit_comparison = card_3 == card_4
    print(suit_comparison)
same_suit(r, s)
def top_card(deck):
    topcard = deck[0]
    deck.remove(topcard)
print(fulldeck)
top_card(fulldeck)

def get_random_card(deck):
    c = random.choice(deck)
    deck.remove(c)
    return c

def shuffle_deck(deck):
    random.shuffle(deck)
hand_deck = []
def deal_hand(deck, size_of_hand):
    for x in range(size_of_hand):
        x = get_random_card(fulldeck)
        deck.append(x)
    print(deck)


deal_hand(hand_deck, 7)



shuffle_deck(fulldeck)
get_random_card(fulldeck)
print(fulldeck)
*********************************************
from itertools import combinations
import random
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
shapes = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
fulldeck = []
def build_deck():
    for shape in shapes:
        for value in values:
            deckstar = value + ' of ' + shape
            fulldeck.append(deckstar)
build_deck()
#random.shuffle(fulldeck)
x = random.choice(fulldeck)
fulldeck.remove(x)
y = random.choice(fulldeck)
gsfhd = []
def get_suit(deck):
    for y in deck:
        suit = y[:1]
        gsfhd.append(suit)
    print(gsfhd)
gvfhd = []
def get_value(deck):
    for i in deck:
        value = i[5:]
        gvfhd.append(value)
    print(gvfhd)
#m = get_value(x)
#n = get_value(y)

def same_value(deck):
    comb = combinations(deck, 2)
    for i in list(comb):
        value_comparison = i[0] == i[1]
        print(value_comparison)

def same_suit(deck):
    comb = combinations(deck, 2)
    for i in list(comb):
        suit_comparison = i[0] == i[1]
        print(suit_comparison)

def top_card(deck):
    topcard = deck[0]
    deck.remove(topcard)
print(fulldeck)
top_card(fulldeck)

def get_random_card(deck):
    c = random.choice(deck)
    deck.remove(c)
    return c

def shuffle_deck(deck):
    random.shuffle(deck)
hand_deck = []
def deal_hand(deck, size_of_hand):
    for x in range(size_of_hand):
        x = get_random_card(fulldeck)
        deck.append(x)
    return deck


deal_hand(hand_deck, 7)



shuffle_deck(fulldeck)
get_random_card(fulldeck)
print(hand_deck)
get_value(hand_deck)
get_suit(hand_deck)
#same_value(gvfhd)
same_suit(gsfhd)


