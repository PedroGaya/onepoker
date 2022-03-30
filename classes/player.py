from classes.enums import HandState
from strategies.random import strategy as random_strategy
class Player:
    def __init__(self, strategy, points=12, order=0, id=-1):
        self.strategy = strategy
        self.hand = []
        self.points = points
        self.order = order
        self.id = id

    def to_hand(self, *cards):
        for card in cards:
            self.hand.append(card)

    def play(self, board):
        decision = self.strategy.play(self, board)
        self.hand.remove(decision)
        return decision

    def bet(self, board, ante=False):
        print(f'P{self.id} points before decision:', self.points)

        decision = self.strategy.bet(self, board) if not ante else board.ante

        print(f'P{self.id} points before bets:', self.points)

        self.points = self.points - decision
        board.bets[self.id - 1] += decision

        print(f'P{self.id} bets: ', decision)
        print(board.bets)
        print(f'P{self.id} points after bets:', self.points)

        return decision

    def hand_state(self):
        first_card = self.hand[0]
        secnd_card = self.hand[1]

        if first_card >= 8 and secnd_card >= 8:
            return HandState(2)

        if first_card < 8 and secnd_card < 8:
            return HandState(0)

        return HandState(1)
