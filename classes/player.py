from classes.enums import HandState
from classes.board import Board
from strategies.human import play_strategy
from strategies.human import bet_strategy

class Player:
    def __init__(self, play_strategy=play_strategy, bet_strategy=bet_strategy, points=12, order=0):
        self.play_strategy = play_strategy
        self.bet_strategy = bet_strategy
        self.hand = []
        self.points = points
        self.order = order
        self.id = order + 1

    def to_hand(self, *cards):
        for card in cards:
            self.hand.append(card)

    def play(self, board):
        decision = self.play_strategy(self, board)
        self.hand.remove(decision)
        return decision

    def bet(self, board, ante=False):
        decision = self.bet_strategy(self, board) if not ante else board.ante

        self.points -= decision
        board.bets[self.id - 1] += decision

        print(f'P{self.id} bets: ', decision)
        return decision

    def hand_state(self):
        first_card = self.hand[0]
        secnd_card = self.hand[1]

        if first_card >= 8 and secnd_card >= 8:
            return HandState(2)

        if first_card < 8 and secnd_card < 8:
            return HandState(0)

        return HandState(1)
