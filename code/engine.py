# *-* coding: UTF-8 *-*
from gameboard import *
from gamepieces import *
from user import *


# - Must also check for check or checkmate (again,
#   not in this class)
# - Bonde kan angripe med vanlig trekk

class Engine(object):
    def __init__(self):
        self.W_king_pos = [4, 0]
        self.B_king_pos = [4, 7]
        self.history = []  # Lager en liste som har oversikt over hvilke trekk som har blitt gjort
        self.turn = 0
        self.board = GameBoard()
        self.sjakkbrett = self.board.brett
        self.player_white = User('W')
        self.player_black = User('B')

        while True:
            print(self.board.console_board())  # Visualiserer brettet i konsollen
            game = self.update()
            if game == 'GG':  # Spillet slutter hvis en av spillerene skriver 'GG'
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
                if white_choice == 'GG':  # Hvis hvit spiller skriver 'GG'
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
                if black_choice == 'GG':  # Hvis svart spiller skriver 'GG'
                    print('White wins!')
                    return black_choice
                fromX = int(black_choice[0])
                fromY = int(black_choice[1])
                toX = int(black_choice[2])
                toY = int(black_choice[3])
                history = black_choice[4]

            # ===============================================================================================

            brikke_flyttes = self.sjakkbrett[fromX][fromY]

            if not brikke_flyttes:  # hvis du valgte tom rute
                print('Deeeet var en tom rute.')
                continue
            if self.turn % 2 and brikke_flyttes.color == "B":  # Hvis hvit prøver å styre svarte brikker
                print('Styr dine egne brikker du...')
                continue
            if not self.turn % 2 and brikke_flyttes.color == "W":  # Hvis svart prøver å styre hvite brikker
                print('Styr dine egne brikker du...')
                continue
            try:  # Hvis valgt destinasjon inneholder friendly piece
                if brikke_flyttes.color == self.sjakkbrett[toX][toY].color:
                    print('Hey, det e fienden du sga dreba!')
                    continue
            except AttributeError:
                pass

            #########################################################################
            # Dette pisset e et resultat av å få trussel både før og etter trekket
            trussel_før = self.threat()  # Trusselbildet før trekket utføres
            brikke_flyttes.x = toX
            brikke_flyttes.y = toY
            self.sjakkbrett[fromX][fromY] = None
            til_rute = self.sjakkbrett[toX][toY]
            self.sjakkbrett[toX][toY] = brikke_flyttes
            trussel_etter = self.threat()  # Trusselbildet etter trekket utføres
            self.sjakkbrett[fromX][fromY] = brikke_flyttes
            self.sjakkbrett[toX][toY] = til_rute
            brikke_flyttes.x = fromX
            brikke_flyttes.y = fromY
            #########################################################################

            if self.W_king_pos in trussel_etter[1] or self.B_king_pos in trussel_etter[3]:
                print('Kongen vil bli truet av dette trekket!')
                continue

            if brikke_flyttes.is_valid_movement(toX, toY, self.sjakkbrett, self.history,
                                                trussel_før):  # Hvis valid movement
                print('Moving %s from (%i,%i) to (%i,%i)!' % (brikke_flyttes.letter, fromX, fromY, toX, toY))
                self.sjakkbrett[fromX][fromY] = None  # Valgt rute blir tom
                brikke_flyttes.x = toX  # x-verdien til objektet oppdateres...
                brikke_flyttes.y = toY  # y-verdien til objektet oppdateres...
                self.sjakkbrett[toX][toY] = brikke_flyttes  # Destinasjonsruten får brikken
                self.history.append(str(self.turn) + ': ' + history)  # Trekket som ble gjort lagres i history-listen
                input_ikke_valid = False
                if brikke_flyttes.letter == 'K':
                    self.W_king_pos = [toX, toY]
                elif brikke_flyttes.letter == 'k':
                    self.B_king_pos = [toX, toY]

            else:
                print('Invalid move. Try again nigga!')
                # input_ikke_valid er fremdeles True, så loopen kjøres igjen

    # =============================================================================================================

    # Lager liste med trusler for svart og hvit
    def threat(self):
        B_piece_threat = []
        W_piece_threat = []
        W_king_threat = []
        B_king_threat = []
        for x in range(8):
            for y in range(8):
                this_pos = self.sjakkbrett[x][y]
                pos = self.sjakkbrett
                if this_pos == None:
                    pass

                elif this_pos.letter == 'P' or this_pos.letter == 'p':
                    if this_pos.letter == 'P':
                        tall = 1
                        save = W_piece_threat
                    else:
                        tall = -1
                        save = B_piece_threat
                    save.append([this_pos.x + 1, this_pos.y + tall])
                    save.append([this_pos.x - 1, this_pos.y + tall])

                elif this_pos.letter == 'r' or this_pos.letter == 'R':
                    if this_pos.letter == 'r':
                        save = B_piece_threat
                    else:
                        save = W_piece_threat
                    for i in range(-1, 2):
                        if i == 0:
                            pass
                        else:
                            for p in range(-1, 2):
                                if p == 0:
                                    pass
                                else:
                                    teller = 0
                                    while True:
                                        teller += 1
                                        if p == 1:
                                            k = this_pos.y + teller * i
                                            l = this_pos.x
                                            if (k) > 7 or (k) < 0:
                                                break
                                        else:
                                            k = this_pos.y
                                            l = this_pos.x + teller * i
                                            if (l) > 7 or (l) < 0:
                                                break
                                        if pos[l][k]:
                                            save.append([l, k])
                                            break
                                        else:
                                            save.append([l, k])

                elif this_pos.letter == 'q' or this_pos.letter == 'Q':
                    if this_pos.letter == 'q':
                        save = B_piece_threat
                    else:
                        save = W_piece_threat
                    for i in range(-1, 2):
                        if i == 0:
                            pass
                        else:
                            for p in range(-1, 2):
                                if p == 0:
                                    pass
                                else:
                                    teller1 = 0
                                    while True:
                                        teller1 += 1
                                        if p == 1:
                                            k1 = this_pos.y + teller1 * i
                                            l1 = this_pos.x + teller1 * i
                                        else:
                                            k1 = this_pos.y + teller1 * i
                                            l1 = this_pos.x - teller1 * i
                                        if k1 > 7 or k1 < 0 or l1 > 7 or l1 < 0:
                                            break
                                        elif pos[l1][k1]:
                                            save.append([l1, k1])
                                            break
                                        else:
                                            save.append([l1, k1])
                                    teller2 = 0
                                    while True:
                                        teller2 += 1
                                        if p == 1:
                                            k2 = this_pos.y + teller2 * i
                                            l2 = this_pos.x
                                            if (k2) > 7 or (k2) < 0:
                                                break
                                        else:
                                            k2 = this_pos.y
                                            l2 = this_pos.x + teller2 * i
                                            if (l2) > 7 or (l2) < 0:
                                                break
                                        if pos[l2][k2]:
                                            save.append([l2, k2])
                                            break
                                        else:
                                            save.append([l2, k2])

                elif this_pos.letter == 'k' or this_pos.letter == 'K':
                    if this_pos.letter == 'k':
                        save = B_king_threat
                    else:
                        save = W_king_threat
                    for i in range(-1, 2):
                        for p in range(-1, 2):
                            if i == p and i == 0:
                                pass
                            else:
                                if 0 <= this_pos.x + i <= 7 and 0 <= this_pos.y + p <= 7:
                                    save.append([this_pos.x + i, this_pos.y + p])

                elif this_pos.letter == 'b' or this_pos.letter == 'B':
                    if this_pos.letter == 'b':
                        save = B_piece_threat
                    else:
                        save = W_piece_threat
                    for i in range(-1, 2):
                        if i == 0:
                            pass
                        else:
                            for p in range(-1, 2):
                                if p == 0:
                                    pass
                                else:
                                    teller = 0
                                    while True:
                                        teller += 1
                                        if p == 1:
                                            k = this_pos.y + teller * i
                                            l = this_pos.x + teller * i
                                        else:
                                            k = this_pos.y + teller * i
                                            l = this_pos.x - teller * i
                                        if k > 7 or k < 0 or l > 7 or l < 0:
                                            break
                                        elif pos[l][k]:
                                            save.append([l, k])
                                            break
                                        else:
                                            save.append([l, k])

                elif this_pos.letter == 'n' or this_pos.letter == 'N':
                    if this_pos.letter == 'n':
                        save = B_piece_threat
                    else:
                        save = W_piece_threat
                    for i in range(-2, 3):
                        if i == 0:
                            pass
                        else:
                            for p in range(-2, 3):
                                if p == 0 or abs(p) == abs(i):
                                    pass
                                else:
                                    if 0 <= this_pos.x + i <= 7 and 0 <= this_pos.y + p <= 7:
                                        save.append([this_pos.x + i, this_pos.y + p])

                else:
                    print(self.sjakkbrett[x][y])

        # Fjerner duplikater i trussellisten
        W_new_threat_list = []
        for elem in B_piece_threat:
            if elem not in W_new_threat_list and 0 <= elem[0] <= 7 and 0 <= elem[1] <= 7:
                W_new_threat_list.append(elem)
        B_piece_threat = W_new_threat_list

        # Fjerner duplikater i trussellisten
        B_new_threat_list = []
        for elem in W_piece_threat:
            if elem not in B_new_threat_list and 0 <= elem[0] <= 7 and 0 <= elem[1] <= 7:
                B_new_threat_list.append(elem)
        W_piece_threat = B_new_threat_list

        return B_king_threat, B_piece_threat, W_king_threat, W_piece_threat


Engine()
