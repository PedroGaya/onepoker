from math import ceil
from classes.strategy import Strategy
import numpy as np

def play(self, board):
    card = np.random.choice(self.hand)
    return card

def bet(self, board):
    amount = ceil(self.points / 2)
    if amount >= self.points:
        amount = self.points
    return amount

strategy = Strategy(play, bet, 'RANDOM')