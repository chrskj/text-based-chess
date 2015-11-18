from gameboard import *
from gamepieces import *
from user import *

"""
Problemer som eksisterer:
- Linje 53 gir posisjonen som du flytter til dens bokstav, men denne blir stor selv om letter skal være lagret som
  små for svart spillers brikker(objekter
- Flytting av brikker fungerer i starten, men plutselig skjer det noe som gjør at de nekter.
"""

class Engine(object):
    def __init__(self):
        self.turn = 0
        board = GameBoard().piece_setup(GameBoard().game_board())
        print(GameBoard().console_board(board[0]))
        self.player_white = User('W')
        self.player_black = User('B')
        while True:
            self.turn += 1
            print(GameBoard().console_board(self.update(board[0], board[1])))
            if self.turn >= 10:
                break

    def update(self, board, chesspiece):
        """Spør bruker om flytting av brikker og oppdaterer brettet."""

        # Angir hvilken runde spillet er på
        print(self.turn)

        # Hvit sin tur på oddetallsrunder, og motsatt for svart
        if self.turn % 2:
            print('White\'s turn!')
            white_choice = self.player_white.movement_input()
            # Lagrer valgene fra bruker i listen choice_list
            choice_list = [int(white_choice[0]), int(white_choice[1]), int(white_choice[2]), int(white_choice[3])]
        else:
            print('Black\'s turn!')
            black_choice = self.player_black.movement_input()
            choice_list = [int(black_choice[0]), int(black_choice[1]), int(black_choice[2]), int(black_choice[3])]

        # Går gjennom alle keys og values for dictionaryen chesspiece
        for k, v in chesspiece.items():
            # Hvis x og y-verdien til et objekt i ordboken stemmer overens med brukerens input, så blir den valgt
            if choice_list[0] == v.x and choice_list[1] == v.y:
                # Hvis brukerens valgte destinasjon er et valid movement, så utføres følgende kode.
                if v.is_valid_movement(choice_list[2], choice_list[3]):
                    print('Valid move!')
                    # Ny x og y-verdi blir valgt ut ifra brukerens input
                    v.x = choice_list[3]
                    v.y = choice_list[2]
                    # Den nye plassen får bokstaven til objektet som skal stå der
                    board[v.x][v.y] = v.letter
                    # Den gamle plassen får symbolet '.'
                    board[choice_list[1]][choice_list[0]] = '.'
                    break
                # Hvis det ikke er et valid movement
                else:
                    print('Invalid movement!')
                    self.turn -= 1
                    continue

        return board


Engine()
