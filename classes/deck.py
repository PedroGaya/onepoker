import numpy as np

class Deck():
    @classmethod
    def __asSymbol(self, val):
        if val <= 10:
            return str(val)
        else:
            if val == 11:
                return 'J'
            if val == 12:
                return 'Q'
            if val == 13:
                return 'K'
            if val == 14:
                return 'A'
        return 'Error: invalid argument.'
        
    @classmethod
    def new(self, symbols=False):
        hearts = np.array(range(2, 15), dtype=np.short)
        spades = np.array(range(2, 15), dtype=np.short)
        clubs = np.array(range(2, 15), dtype=np.short)
        diamonds = np.array(range(2, 15), dtype=np.short)
        deck = np.concatenate([hearts, spades, clubs, diamonds])

        if symbols:
            symbolified = np.array(list(map(self.__asSymbol, deck)))
            self.state = symbolified
            return symbolified
        else:
            self.state = deck
            return deck

    def draw(self):
        deck = self.state.copy()
        card = deck[-1]
        self.set(deck[:-1])
        return card
    
    def shuffle(self):
        deck = self.state.copy()
        rng = np.random.default_rng()
        rng.shuffle(deck)
        self.state = deck
        return deck
    
    def symbolify(self):
        deck = self.state.copy()
        symbolified = np.array(list(map(self.__asSymbol, deck)))
        self.set(symbolified)
    
    def set(self, new_deck):
        self.state = new_deck
        return self.state
            
    def __init__(self, symbols=False, empty=False):
        if empty:
            self.state.set(np.array([]))

        self.set(self.new(symbols=symbols))