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

    p1 = Player(human_strategy, points, order=val)
    p2 = Player(random_strategy, points, order=(1-val))

    if(p1.strategy.name == 'HUMAN'):
        f_or_s = 'first.\nYou are P1.' if p1.order == 0 else 'second\nYou are P2.'
        print(f'You are going: {f_or_s}')

    p1.to_hand(rd.choice(deck))
    p2.to_hand(rd.choice(deck))
    p1.to_hand(rd.choice(deck))
    p2.to_hand(rd.choice(deck))

    print('Ante: ', board.ante)
    while game_result == GameResult.NOT_FINISHED:
        round_w = play_round(p1, p2, board)

        print('Round winner :', round_w)

        if p1.points == 0:
            game_result = GameResult.P2_WIN
            break
        if p2.points == 0:
            game_result = GameResult.P1_WIN
            break

        if round_w != GameResult.P1_WIN:
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

    first.bet(board)
    second.bet(board)

    print('Pot: ', np.sum(board.bets))

    winner = get_winner(card_first, card_second)
    if winner == GameResult.P1_WIN:
        first.points += np.sum(board.bets)
    if winner == GameResult.P2_WIN:
        second.points += np.sum(board.bets)
    if winner == GameResult.DRAW:
        first.points += board.bets[first.id - 1]
        second.points += board.bets[second.id - 1]

    board.bets = [0, 0]
    print('P1 points after round: ', p1.points)
    print('P2 points after round: ', p2.points)
    print('ROUND DONE')
    return winner

def get_winner(card_first, card_second):
    print('First card: ', card_first)
    print('Second card: ', card_second)
    if card_first == card_second:
        return GameResult.DRAW
    if card_first == 2 and card_second == 14:
        return GameResult.P1_WIN
    if card_second == 2 and card_first == 14:
        return GameResult.P2_WIN
    if card_first > card_second:
        return GameResult.P1_WIN
    else:
        return GameResult.P2_WIN

play_game()