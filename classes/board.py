from classes.enums import HandState, GameState, BetActions
import numpy as np

class Board:
    def __init__(self, points, ante):
        self.game_state = GameState.PLAY
        self.p1_hand = HandState.UP_DOWN
        self.p2_hand = HandState.UP_DOWN
        self.last_action = None
        self.ante = ante
        self.bets = [0, 0]
        self.folded = -1

    def legal_actions(self):
        possible_actions = [e.name for e in BetActions]
        if self.last_action == None:
            return ['BET', 'CHECK']
        elif self.last_action == 'BET':
            possible_actions.remove('BET')
            possible_actions.remove('CHECK')
            return possible_actions
        elif self.last_action == 'CHECK':
            possible_actions.remove('CALL')
            possible_actions.remove('RAISE')
            return possible_actions
        elif self.last_action == 'CALL':
            return ['NONE']
        elif self.last_action == 'RAISE':
            possible_actions.remove('BET')
            possible_actions.remove('CHECK')
            return possible_actions
        elif self.last_action == 'FOLD':
            return ['NONE']
