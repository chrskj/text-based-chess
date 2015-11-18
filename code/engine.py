# *-* coding: UTF-8 *-*
from gameboard import *
from gamepieces import *
from user import *

"""
Problemer som eksisterer:
- Linje 53 gir posisjonen som du flytter til dens bokstav, men denne blir stor selv om letter skal vÃ¦re lagret som
  smÃ¥ for svart spillers brikker(objekter
- Flytting av brikker fungerer i starten, men plutselig skjer det noe som gjÃ¸r at de nekter.
"""

class Engine(object):
    def __init__(self):
        self.turn = 0
        # board = GameBoard().piece_setup(GameBoard().game_board())
        self.board = GameBoard()
        self.sjakkbrett = self.board.brett_raggiz
        
        # print(GameBoard().console_board(board[0]))
        print( self.board.console_board_raggiz() ) 

        self.player_white = User('W')
        self.player_black = User('B')
        while True:
            # flytter turn-plussingen inn i update, gjør det litt mer elegant
            # self.turn += 1
            # print(GameBoard().console_board(self.update(board[0], board[1])))
            self.update()
            print( self.board.console_board_raggiz() )
            # if self.turn >= 10:
            #     break

    # def update(self, board, chesspiece):
    def update(self):
        """SpÃ¸r bruker om flytting av brikker og oppdaterer brettet."""
        self.turn += 1
        print("========================================")

        # input_ikke_valid er bare en ting som gjør at vi veldig enkelt kan
        # hoppe tilbake hit hvis dusten gir inn et invalid move. Slipper
        # å trekke fra turns og greier. Hvis trekket er valid, setter vi
        # bare input_ikke_valid til False, og går da ut av while-loopen

        input_ikke_valid = True
        while input_ikke_valid:
            
            print('TURN NUMMER ', self.turn)

            # Hvit sin tur pÃ¥ oddetallsrunder, og motsatt for svart
            if self.turn % 2:
                print('White\'s turn!')
                white_choice = self.player_white.movement_input()
                # Lagrer valgene fra bruker i listen choice_list
                # det e ikkje FEIL å gjør det, men code readability > spara et par linje og et par bytes
                # choice_list = [int(white_choice[0]), int(white_choice[1]), int(white_choice[2]), int(white_choice[3])]
                fromX = int(white_choice[0])
                fromY = int(white_choice[1])
                toX = int(white_choice[2])
                toY = int(white_choice[3])
            else:
                print('Black\'s turn!')
                black_choice = self.player_black.movement_input()
                # choice_list = [int(black_choice[0]), int(black_choice[1]), int(black_choice[2]), int(black_choice[3])]
                fromX = int(black_choice[0])
                fromY = int(black_choice[1])
                toX = int(black_choice[2])
                toY = int(black_choice[3])
        
            # skjønte ikkje heilt det under, prøve bare min egen litt enklere/finere
            brikke_flyttes = self.sjakkbrett[fromX][fromY]
            if not brikke_flyttes:  # hvis du valgte tom rute
                print('Deeeet var en tom rute.')
                break
            if brikke_flyttes.is_valid_movement(toX, toY):
                print('Moving %s from (%i,%i) to (%i,%i). Valid move!' %(brikke_flyttes.letter, fromX, fromY, toX, toY))
                self.sjakkbrett[fromX][fromY] = None
                # her må det til validering da, at vi ikke tar vår egen brikker m.m.
                self.sjakkbrett[toX][toY] = brikke_flyttes
                input_ikke_valid = False
            else:
                print('Invalid move! Try again nigga')
                # input_ikke_valid er fremdeles True, så loopen kjøres igjen
                
                
##            # GÃ¥r gjennom alle keys og values for dictionaryen chesspiece
##            for k, v in chesspiece.items():
##                # Hvis x og y-verdien til et objekt i ordboken stemmer overens med brukerens input, sÃ¥ blir den valgt
##                if choice_list[0] == v.x and choice_list[1] == v.y:
##                    # Hvis brukerens valgte destinasjon er et valid movement, sÃ¥ utfÃ¸res fÃ¸lgende kode.
##                    if v.is_valid_movement(choice_list[2], choice_list[3]):
##                        print('Valid move!')
##                        # Ny x og y-verdi blir valgt ut ifra brukerens input
##                        v.x = choice_list[3]
##                        v.y = choice_list[2]
##                        # Den nye plassen fÃ¥r bokstaven til objektet som skal stÃ¥ der
##                        board[v.x][v.y] = v.letter
##                        # Den gamle plassen fÃ¥r symbolet '.'
##                        board[choice_list[1]][choice_list[0]] = '.'
##                        break
##                    # Hvis det ikke er et valid movement
##                    else:
##                        print('Invalid movement!')
##                        self.turn -= 1
##                        continue

        # return board


Engine()
