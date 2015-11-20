# *-* coding: UTF-8 *-*
from gameboard import *
from gamepieces import *
from user import *

######################## TO-DO ########################
# - Unngå at tårn, løper og dronning hopper over      #
#   andre brikker                                     #
# - When a move is attempted, a check must be made to #
#   ensure that the destination does not contain a    #
#   piece of the same color (NOT in this class,       #
#   probably in the "Game" class)                     #
# - Must also check for check or checkmate (again,    #
#   not in this class)                                #
# - Forhindre at motspillere kan bruke hverandres     #
#   brikker                                           #
#######################################################

class Engine(object):
    def __init__(self):
        self.turn = 0
        self.board = GameBoard()
        self.sjakkbrett = self.board.brett

        print(self.board.console_board())

        self.player_white = User('W')
        self.player_black = User('B')
        while True:
            self.update()
            print(self.board.console_board())

    def update(self):
        """Spør bruker om flytting av brikker og oppdaterer brettet."""
        self.turn += 1
        print("========================================")

        # input_ikke_valid er bare en ting som gjør at vi veldig enkelt kan
        # hoppe tilbake hit hvis dusten gir inn et invalid move. Slipper
        # å trekke fra turns og greier. Hvis trekket er valid, setter vi
        # bare input_ikke_valid til False, og går da ut av while-loopen

        input_ikke_valid = True
        while input_ikke_valid:

            print('TURN NUMMER ', self.turn)

            # Hvit sin tur på oddetallsrunder, og motsatt for svart
            if self.turn % 2:
                print('White\'s turn!')
                try:
                    white_choice = self.player_white.movement_input()
                except ValueError:
                    print('Skriv noge så gir meining!')
                    continue
                fromX = int(white_choice[0])
                fromY = int(white_choice[1])
                toX = int(white_choice[2])
                toY = int(white_choice[3])
            else:
                print('Black\'s turn!')
                try:
                    black_choice = self.player_black.movement_input()
                except ValueError:
                    print('Skriv noge så gir meining!')
                    continue
                fromX = int(black_choice[0])
                fromY = int(black_choice[1])
                toX = int(black_choice[2])
                toY = int(black_choice[3])

            brikke_flyttes = self.sjakkbrett[fromX][fromY]
            if not brikke_flyttes:  # hvis du valgte tom rute
                print('Deeeet var en tom rute.')
                continue
            try: # Prøver å finne color-verdien til valt brikke og destinasjon
                if brikke_flyttes.color == self.sjakkbrett[toX][toY].color:
                    print('Hey, det e fienden du sga dreba!')
                    continue
            except AttributeError:
                pass
            if brikke_flyttes.is_valid_movement(toX, toY, self.sjakkbrett):
                print(
                    'Moving %s from (%i,%i) to (%i,%i)!' % (brikke_flyttes.letter, fromX, fromY, toX, toY))
                self.sjakkbrett[fromX][fromY] = None
                brikke_flyttes.x = toX # chrskj: x og y-verdien må oppdateres...
                brikke_flyttes.y = toY # chrskj: x og y-verdien må oppdateres...
                # her må det til validering da, at vi ikke tar vår egen brikker m.m.
                self.sjakkbrett[toX][toY] = brikke_flyttes
                input_ikke_valid = False
            else:
                print('Invalid move. Try again nigga!')
                # input_ikke_valid er fremdeles True, så loopen kjøres igjen


Engine()
