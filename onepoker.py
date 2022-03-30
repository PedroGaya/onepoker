from classes.deck import Deck
from classes.player import Player
from classes.board import Board

from classes.enums import DeckTypes, GameState
from classes.enums import GameResult

from strategies.human import strategy as human_strategy
from strategies.random import strategy as random_strategy

import numpy as np
import numpy.random as rd

def play_game(points=12, ante=1, deck_type=DeckTypes.PERFECT):
    deck = []

    if deck_type == DeckTypes.PERFECT:
        deck = np.array(range(2, 15))

    game_result = GameResult.NOT_FINISHED

    board = Board(points, ante)

    val = rd.randint(0, 2)

    p1 = Player(human_strategy, points, order=val, id=1)
    p2 = Player(random_strategy, points, order=(1-val), id=2)

    if(p1.strategy.name == 'HUMAN'):
        f_or_s = 'first.\nYou are P1.' if p1.order == 0 else 'second\nYou are P1.'
        print(f'You are going: {f_or_s}')

    p1.to_hand(rd.choice(deck))
    p2.to_hand(rd.choice(deck))
    p1.to_hand(rd.choice(deck))
    p2.to_hand(rd.choice(deck))

    print('Ante: ', board.ante)
    print('Starting points: ', points)
    while game_result == GameResult.NOT_FINISHED:
        
        print('P1 points before round:', p1.points)
        print('P2 points before round:', p2.points)
        round_w = play_round(p1, p2, board)
        print('P1 points after round:', p1.points)
        print('P2 points after round:', p2.points)

        if p1.points == 0:
            game_result = GameResult.P2_WIN
            break
        if p2.points == 0:
            game_result = GameResult.P1_WIN
            break

        if round_w != 'FIRST':
            p1.order ^= 1
            p2.order ^= 1

        p1.to_hand(rd.choice(deck))
        p2.to_hand(rd.choice(deck))

    print(game_result)



def play_round(p1: Player, p2: Player, board: Board):
    print('ROUND START')
    
    board.p1_hand = p1.hand_state()
    board.p2_hand = p2.hand_state()

    arr = [p1, p2]
    first = next(p for p in arr if p.order == 0)
    second = next(p for p in arr if p.order == 1)

    print(f'Going first: P{first.id}')
    print(f'Going second: P{second.id}')

    first.bet(board, ante=True)
    second.bet(board, ante=True)

    card_first = first.play(board)
    card_second = second.play(board)

    betting_round(first, second, board)

    if board.folded > -1:
        if board.folded == 0:
            card_first = 0
        if board.folded == 1:
            card_second = 0

    winner = get_winner(card_first, card_second)
    payout = [0, 0]

    if winner == 'FIRST':
        print(first.strategy.name, 'wins')
        if first.id == 1:
            payout = [np.sum(board.bets), 0]
        else:
            payout = [0, np.sum(board.bets)]
    elif winner == 'SECOND':
        if second.id == 1:
            payout = [np.sum(board.bets), 0]
        else:
            payout = [0, np.sum(board.bets)]
    elif winner == 'DRAW':
        payout = board.bets

    p1.points += payout[0]
    p2.points += payout[1]

    board.last_action = None
    board.folded = -1
    board.bets = [0, 0]

    print('ROUND DONE')
    return winner

def get_winner(card_first, card_second):
    print('First card: ', card_first if card_first else 'FOLD')
    print('Second card: ', card_second if card_second else 'FOLD')
    if card_first == card_second:
        return 'DRAW'
    if card_first == 2 and card_second == 14:
        return 'FIRST'
    if card_second == 2 and card_first == 14:
        return 'SECOND'
    if card_first > card_second:
        return 'FIRST'
    else:
        return 'SECOND'

def betting_round(first, second, board):
    should_continue = True
    while should_continue:
        first.bet(board)
        second.bet(board)
        print('Pot:', board.bets)
        call_or_fold = board.last_action == 'CALL' or board.last_action == 'FOLD'
        no_bets = board.bets[0] == board.bets[1]
        if no_bets or call_or_fold:
            should_continue = False

    

play_game()