from gameboard import *
from gamepieces import *
from user import *

class Engine(object):

    def __init__(self):
        turn = 0
        board = GameBoard()
        player_white = User('W')
        player_black = User('B')
        while True:
            turn += 1
            self.update(turn, player_white, player_black)
            if turn >= 10:
                break

    def update(self, turn, player_white, player_black):
        print(turn)
        if turn % 2:
            print('White\'s turn!')
            white_choice = player_white.movement_input()
            return [white_choice[0], white_choice[1], white_choice[2], white_choice[3]]
        else:
            print('Black\'s turn!')
            black_choice = player_black.movement_input()
            return [black_choice[0], black_choice[1], black_choice[2], black_choice[3]]

Engine()