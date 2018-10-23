class card (object):
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
        suit = suit.upper()
        if suit in ['S', 'H', 'D', 'C']:
            self.suit = suit
        else:
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
        def make13(suit):
            l = []
            for i in range(1, 14):
                l.append(card(i, suit))
            return l
        self.cards = []
        self.cards += make13('S')
        self.cards += make13('H')
        self.cards += make13('D')
        self.cards += make13('C')
    def __str__(self):
        s = ''
        for i in range(4):
            for j in range(13):
                try:
                    s += str(self.cards[13 * i + j])
                except:
                    pass
            s += '\n'
        return s

d = Deck()
print(d)