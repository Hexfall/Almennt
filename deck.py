import random
class Card (object):
    def __init__(self, rank = 0, suit = ""):
        if type(rank) == str:
            rank = rank.upper()
            if rank == 'A':
                self.rank = 1
            elif rank == 'J':
                self.rank = 11
            elif rank == 'Q':
                self.rank = 12
            elif rank == 'K':
                self.rank = 13
            else:
                self.rank = 0
        else:
            if rank < 1 or rank > 13:
                self.rank = 0
            else:
                self.rank = rank
        try:
            suit = suit.upper()
            if suit in ['S', 'H', 'D', 'C']:
                self.suit = suit
            else:
                self.suit = ""
        except:
            self.suit = ""
    def __str__(self):
        if self.rank == 0 or self.suit == "":
            return "blk"
        printRank = self.rank
        if printRank == 13:
            printRank = 'K'
        elif printRank == 12:
            printRank = 'Q'
        elif printRank == 11:
            printRank = 'J'
        elif printRank == 1:
            printRank = 'A'
        return "{:>2}{:1}".format(printRank, self.suit)
    def is_blank(self):
        if str(self) == 'blk':
            return True
        return False

class Deck (object):
    def __init__(self):
        self.cards = [Card(i, j) for i in range(1, 14) for j in ['S', 'H', 'D', 'C']]
    def __str__(self):
        return "\n".join([" ".join([str(self.cards[i * int(len(self.cards)/4) + j]) for j in range(int(len(self.cards)/4))]) for i in range(4)])
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        return self.cards.pop(0)

class PlayingHand (object):
    def __init__(self):
        self.hand = [Card() for i in range(13)]
    def __str__(self):
        return " ".join([str(i) for i in self.hand])
    def add_card(self, newCard):
        for i in range(len(self.hand)):
            if self.hand[i].is_blank():
                self.hand[i] = newCard
                break
    NUMBER_CARDS = 13

def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5,'s')
    print(card2)
    card3 = Card('Q','D')
    print(card3)
    card4 = Card('x', 7)
    print(card4)
def print_4_hands(hand1, hand2, hand3, hand4):
    ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)
def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands '''
    for i in range(PlayingHand.NUMBER_CARDS):
        hand1.add_card(deck.deal())
        hand2.add_card(deck.deal())
        hand3.add_card(deck.deal())
        hand4.add_card(deck.deal())
def test_hands(deck):
    hand1 = PlayingHand()
    hand2 = PlayingHand()
    hand3 = PlayingHand()
    hand4 = PlayingHand()
    print("The 4 hands:")
    print_4_hands(hand1, hand2, hand3, hand4)
    deal_4_hands(deck, hand1, hand2, hand3, hand4)
    print("The 4 hands after dealing:")
    print_4_hands(hand1, hand2, hand3, hand4)
# The main program starts here
random.seed(10)
test_cards()
deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)
test_hands(deck)
print("The deck after dealing:")
print(deck)