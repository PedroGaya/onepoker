from classes.strategy import Strategy
from classes.enums import BetActions

def play(self, board):
    print('Your hand: ', self.hand)
    if (self.order == 0):
        print('Opponent hand: ', board.p2_hand)
    else:
        print('Opponent hand: ', board.p1_hand)

    card = int(input('Choose a card:\n'))

    while card not in self.hand:
        card = int(input('Please choose a valid card.\n'))
    return card

def bet(self, board):
    print('Your options: ')
    for e in board.legal_actions():
        print(e)

    choice = input('Choose an action (type it AS IS):\n').upper()

    while choice not in board.legal_actions():
        choice = input('Illegal, do it right this time:\n').upper()
    
    if choice == 'BET':
        amount = int(input('Amount:\n'))
        while amount > self.points:
            amount = int(input('Enter a valid amount:\n'))
        board.last_action = 'BET'
        return amount
    elif choice == 'CHECK':
        board.last_action = 'CHECK'
        return 0
    elif choice == 'CALL':
        board.last_action = 'CALL'
        ideal = max(board.bets) - board.bets[self.id - 1]
        if ideal > self.points:
            return self.points
        else:
            return ideal
    elif choice == 'RAISE':
        amount = int(input('Amount:\n'))
        minimum = max(board.bets) - board.bets[self.id - 1]
        while amount <= minimum:
            amount = int(input(f'Enter an amount greater than {minimum}:\n'))
        board.last_action = 'RAISE'
        return amount
    elif choice == 'FOLD':
        board.last_action = 'FOLD'
        board.folded = self.order
        return 0
    return 0

strategy = Strategy(play, bet, 'HUMAN')