
import random
face_value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J', 'A']
shapes = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
fulldeck = []
def build_deck():
    for shape in shapes:
        for face in face_value:
            i = face + ' of ' + shape
            fulldeck.append(i)

build_deck()
random.shuffle(fulldeck)
def get_suit(face_card):
    suits = []
    x = fulldeck[0]
    for i in x:
        suits.append(i)
    global suit
    suit = ''.join(suits[5:])
    print(face_card + ' of ' + suit)
    return suit
get_suit('6')
def get_value(suit_card):
    values = []
    y = fulldeck[0]
    for i in y:
        values.append(i)
    global value
    value = ''.join(values[:1])
    print(value + ' of ' + suit_card)
    return value

#get_value('Diamonds')

def same_value(face_card, suit_card):
    card_alpha = (face_card + ' of ' + suit)
    print(card_alpha)
    card_beta = (value + ' of ' + suit_card)
    print(card_beta)
    print(card_alpha == card_beta)

#same_value('2', 'Hearts')
def deal_top_card(top_card):
    for x in top_card:
        print(x)
        break
    del fulldeck[0]
    return x


def get_random_card(card_pickup):
    pickup_deck = []
    for x in card_pickup:
        pickup_deck.append(x)
    y = random.choice(pickup_deck)
    print(y)
    pickup_deck.remove(y)

def shuffle_deck(shuffled_deck):
    random.shuffle(shuffled_deck)
    print(shuffled_deck)

def deal_hand(deal_deck, hand):
    player_hand = []
    i = 0
    while i < hand:
        player_hand.append(deal_top_card(fulldeck))
        i += 1
    print(player_hand)

#deal_top_card(fulldeck)
#print(fulldeck)
#print(len(fulldeck))
#get_random_card(fulldeck)
#shuffle_deck(fulldeck)
deal_hand(fulldeck, 1)



import csv
import matplotlib.pyplot as plt
from scipy import stats
csvfile = list(csv.reader(open('Proteins_and_enzymes_data.csv')))
csv_dic = []
for row in csvfile:
    csv_dic.append(row)
print(csv_dic)
substrate = []
velocity = []
for row in csv_dic:
    substrate.append(row[0])
    velocity.append(row[1])
    #for column in row:
        #print(column)
del velocity[0]
velocity0 = []
for value in velocity:
    value = float(value)
    newvalue = 1.0 / value
    velocity0.append(newvalue)


del substrate[0]
substrate0 = []
for value in substrate:
    value = float(value)
    newvalue = 1.0 / value
    substrate0.append(newvalue)

slope, intercept, r, p, std_err = stats.linregress(substrate0, velocity0)
def myfunc(substrate0):
    return slope * substrate0 + intercept

mymodel = list(map(myfunc, substrate0))
plt.scatter(substrate0, velocity0)
plt.plot(substrate0, mymodel)
plt.show()


