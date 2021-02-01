
import random
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Ace", "King", "Jack", "Queen")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
          "Ten": 10, "King": 10, "Queen": 10, "Jack": 10, "Ace": 11}
playing = True
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + deck_comp
        return "The deck has: " + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 1000
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet? "))
        except ValueError:
            print("Sorry!!! Please enter a number!!")
        else:
            if chips.bet > chips.total:
                print("Your bet cannot exceed 1000")
            else:
                break
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing
    while True:
        ask = input("Would you like to hit or stand? Please enter 'h' or 's':")
        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print("player stands. Dealer is playing")
            playing = False
        else:
            print("Sorry I didn't understand that. Please try again.")
            continue
        break

def show_some(player, dealer):
    print("\n Dealer's hand: ")
    print("< card hidden >")
    print("", dealer.cards[1])
    print("\n player's hand: ", *player.cards, sep="\n ")

def show_all(player, dealer):
    print("\n Dealer's Hand: ", * dealer.cards)
    print("Dealer's Hand = ", dealer.value)
    print("\n Player's Hand: ", *player.cards)
    print("Player's Hand = ", player.value)

def player_bust(player,dealer, chips):
    print("PLAYER BUSTS!")
    chips.lose_bet()

def player_win(player, dealer, chips):
    print("PLAYER WINS!!!")
    chips.win_bet()

def dealer_bust(player, dealer, chips):
    print("DEALER BUSTS!")
    chips.win_bet()

def dealer_win(player, dealer, chips):
    print("DEALER WINS")
    chips.lose_bet()

def push(player, dealer):
    print("It's a push. Player and dealer is a tie. ")

while True:
    print("Welcome to blackjack")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()

    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()

    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_bust(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand, dealer_hand, player_chips)

        elif player_hand.value > dealer_hand.value:
            player_win(player_hand, dealer_hand, player_chips)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)

    print("\n Player's winning stand at", player_chips.total)

    new_game = input("\nWould you like to playagain? enter 'y' or 'n':")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing")
        break