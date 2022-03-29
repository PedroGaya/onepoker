from classes.enums import HandState, GameState

class Board:
    def __init__(self, points, ante):
        self.game_state = GameState.PLAY
        self.p1_hand = HandState.UP_DOWN
        self.p2_hand = HandState.UP_DOWN
        self.ante = ante
        self.bets = [0, 0]

    def update(self, new_state):
        pass
