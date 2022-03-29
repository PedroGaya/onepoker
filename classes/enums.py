from enum import Enum

class GameResult(Enum):
    NOT_FINISHED = 0
    P1_WIN = 1
    P2_WIN = 2
    DRAW = 3

class HandState(Enum):
    DOUBLE_DOWN = 0
    UP_DOWN = 1
    DOUBLE_UP = 2

class GameState(Enum):
    PLAY = 0
    BET = 1

class DeckTypes(Enum):
    PERFECT = 0
    MANGA = 1