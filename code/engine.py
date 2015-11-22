# *-* coding: UTF-8 *-*
from gameboard import *
from gamepieces import *
from user import *


# - Must also check for check or checkmate (again,
#   not in this class)
# - En pasant

class Engine(object):
    def __init__(self):
        self.history = []  # Lager en liste som har oversikt over hvilke trekk som har blitt gjort
        self.turn = 0
        self.board = GameBoard()
        self.sjakkbrett = self.board.brett
        self.player_white = User('W')
        self.player_black = User('B')

        while True:
            print(self.board.console_board())  # Visualiserer brettet i konsollen
            if self.update() == 'surrender':  # Spillet slutter hvis en av spillerene skriver 'surrender'
                break
        print(self.history)  # Printer ut alle trekkene som har blitt gjort

    def update(self):
        """Spør bruker om flytting av brikker og oppdaterer brettet."""
        self.turn += 1
        print("========================================")
        input_ikke_valid = True

        while input_ikke_valid:
            print('TURN NUMMER ', self.turn)

            # ===============================================================================================

            # Hvit sin tur på oddetallsrunder, og motsatt for svart
            if self.turn % 2:
                print('White\'s turn!')
                try:
                    white_choice = self.player_white.movement_input()
                except ValueError:
                    print('Skriv noge så gir meining!')
                    continue
                if white_choice == 'surrender':  # Hvis hvit spiller skriver 'surrender'
                    print('Black wins!')
                    return white_choice
                fromX = int(white_choice[0])
                fromY = int(white_choice[1])
                toX = int(white_choice[2])
                toY = int(white_choice[3])
                history = white_choice[4]
            else:
                print('Black\'s turn!')
                try:
                    black_choice = self.player_black.movement_input()
                except ValueError:
                    print('Skriv noge så gir meining!')
                    continue
                if black_choice == 'surrender':  # Hvis svart spiller skriver 'surrender'
                    print('White wins!')
                    return white_choice
                fromX = int(black_choice[0])
                fromY = int(black_choice[1])
                toX = int(black_choice[2])
                toY = int(black_choice[3])
                history = black_choice[4]

            # ===============================================================================================

            brikke_flyttes = self.sjakkbrett[fromX][fromY]

            if self.turn % 2 and brikke_flyttes.color == "B":  # Hvis hvit prøver å styre svarte brikker
                print('Styr dine egne brikker du...')
                continue
            if not self.turn % 2 and brikke_flyttes.color == "W":  # Hvis svart prøver å styre hvite brikker
                print('Styr dine egne brikker du...')
                continue
            if not brikke_flyttes:  # hvis du valgte tom rute
                print('Deeeet var en tom rute.')
                continue
            try:  # Hvis valgt destinasjon inneholder friendly piece
                if brikke_flyttes.color == self.sjakkbrett[toX][toY].color:
                    print('Hey, det e fienden du sga dreba!')
                    continue
            except AttributeError:
                pass

            if brikke_flyttes.is_valid_movement(toX, toY, self.sjakkbrett):  # Hvis valid movement
                print(
                    'Moving %s from (%i,%i) to (%i,%i)!' % (brikke_flyttes.letter, fromX, fromY, toX, toY))
                self.sjakkbrett[fromX][fromY] = None
                brikke_flyttes.x = toX  # x-verdien til objektet oppdateres...
                brikke_flyttes.y = toY  # y-verdien til objektet oppdateres...
                # her må det til validering da, at vi ikke tar vår egen brikker m.m.
                self.sjakkbrett[toX][toY] = brikke_flyttes
                self.history.append(history)  # Trekket som ble gjort lagres i history-listen
                input_ikke_valid = False

            else:
                print('Invalid move. Try again nigga!')
                # input_ikke_valid er fremdeles True, så loopen kjøres igjen

                # ===============================================================================================

Engine()
