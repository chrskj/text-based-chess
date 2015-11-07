from gameboard import *
from gamepieces import *
from user import *


class Engine(object):

    def __init__(self):
        self.turn = 0
        # board not used? Tør ikkje sletta an
        board = GameBoard()
        self.player_white = User('W')
        self.player_black = User('B')
        while True:
            turn += 1
            self.update()
            if turn >= 10:
                break

    def update(self):
        print(self.turn)
        if self.turn % 2:
            print('White\'s turn!')
            white_choice = self.player_white.movement_input()
            return [white_choice[0], white_choice[1],
                    white_choice[2], white_choice[3]]
        else:
            print('Black\'s turn!')
            black_choice = self.player_black.movement_input()
            return [black_choice[0], black_choice[1],
                    black_choice[2], black_choice[3]]

Engine()
