from gameboard import *
from gamepieces import *
from user import *


class Engine(object):
    def __init__(self):
        self.turn = 0
        board = GameBoard()
        self.player_white = User('W')
        self.player_black = User('B')
        while True:
            self.turn += 1
            print(board.console_board(self.update(board)))
            if self.turn >= 10:
                break

    def update(self, board):
        """Spør bruker om flytting av brikker og oppdaterer brettet."""
        print(self.turn)

        if self.turn % 2:
            print('White\'s turn!')
            white_choice = self.player_white.movement_input()
            choice_list = [int(white_choice[0]), int(white_choice[1]), int(white_choice[2]), int(white_choice[3])]
        else:
            print('Black\'s turn!')
            black_choice = self.player_black.movement_input()
            choice_list = [int(black_choice[0]), int(black_choice[1]), int(black_choice[2]), int(black_choice[3])]

        brikke_valg = board.pos[choice_list[0]][choice_list[1]]
        print(brikke_valg)
        brikke_plassering = board.pos[choice_list[2]][choice_list[3]]
        print(brikke_plassering)
        brikke_plassering = brikke_valg
        brikke_valg = '.'
        print(brikke_valg)
        print(brikke_plassering)
        print(board.pos)



Engine()
