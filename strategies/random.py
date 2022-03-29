from math import ceil
from classes.enums import GameState
import numpy as np

def play_strategy(self, board):
    card = np.random.choice(self.hand)
    return card

def bet_strategy(self, board):
    amount = ceil(self.points / 2)
    if amount >= self.points:
        amount = self.points
    return amount