from math import ceil
from classes.strategy import Strategy
from numpy.random import default_rng

rng = default_rng()

def play(self, board):
    card = rng.choice(self.hand)
    return card

def bet(self, board):
    choice = rng.choice(board.legal_actions())
    print('Opponent chose: ', choice)

    if choice == 'BET':
        amount = ceil(self.points / 2)
        board.last_action = 'BET'
        return amount
    elif choice == 'CHECK':
        board.last_action = 'CHECK'
        return 0
    elif choice == 'CALL':
        board.last_action = 'CALL'
        return max(board.bets) - board.bets[self.id - 1]
    elif choice == 'RAISE':
        minimum = max(board.bets) - board.bets[self.id - 1] + 1
        if minimum >= self.points:
            return self.points
        amount = rng.integers(minimum, self.points)
        board.last_action = 'RAISE'
        return amount
    elif choice == 'FOLD':
        board.last_action = 'FOLD'
        board.folded = self.order
        return 0
        
    return 0

strategy = Strategy(play, bet, 'RANDOM')