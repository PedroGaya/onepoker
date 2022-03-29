from classes.strategy import Strategy

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
    amount = int(input('Bet an amount:\n'))

    while amount > self.points:
        amount = int(input('Enter a valid amount:\n'))

    return amount

strategy = Strategy(play, bet, 'HUMAN')