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
            print('TREKK NUMMER ', self.turn)

            # ===============================================================================================

            # Hvit sin tur på oddetallsrunder, og motsatt for svart
            if self.turn % 2:
                print('Hvit sin tur!')
                try:
                    white_choice = self.player_white.movement_input()
                except ValueError:
                    print('Skriv noe som gir mening!')
                    continue
                if white_choice == 'GG':  # Hvis hvit spiller skriver 'GG'
                    print('Svart vinner!')
                    return white_choice
                fromX = int(white_choice[0])
                fromY = int(white_choice[1])
                toX = int(white_choice[2])
                toY = int(white_choice[3])
                history = white_choice[4]
            else:
                print('Svart sin tur!')
                try:
                    black_choice = self.player_black.movement_input()
                except ValueError:
                    print('Skriv noe som gir mening!')
                    continue
                if black_choice == 'GG':  # Hvis svart spiller skriver 'GG'
                    print('Hvit vinner!')
                    return black_choice
                fromX = int(black_choice[0])
                fromY = int(black_choice[1])
                toX = int(black_choice[2])
                toY = int(black_choice[3])
                history = black_choice[4]

            # ===============================================================================================

            brikke_flyttes = self.sjakkbrett[fromX][fromY]

            if not brikke_flyttes:  # hvis du valgte tom rute
                print('Tom rute')
                continue
            if self.turn % 2 and brikke_flyttes.color == "B":  # Hvis hvit prøver å styre svarte brikker
                print('Kan bare styre dine egne brikker')
                continue
            if not self.turn % 2 and brikke_flyttes.color == "W":  # Hvis svart prøver å styre hvite brikker
                print('Kan bare styre dine egne brikker')
                continue
            try:  # Hvis valgt destinasjon inneholder friendly piece
                if brikke_flyttes.color == self.sjakkbrett[toX][toY].color:
                    print('Kan ikke angripe egne brikker!')
                    continue
            except AttributeError:
                pass

            ############################################################################################################
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
            ############################################################################################################

            if self.turn % 2:  # Hvis hvit sin tur
                if self.W_king_pos in trussel_etter[1]:  # Hvis hvit konge er truet etter hvit sitt trekk
                    print('Kongen vil bli truet av dette trekket!')
                    continue
            else:
                if self.B_king_pos in trussel_etter[3]:  # Hvis svart konge er truet etter svart sitt trekk
                    print('Kongen vil bli truet av dette trekket!')
                    continue

            if brikke_flyttes.is_valid_movement(toX, toY, self.sjakkbrett, self.history, trussel_før):  # Valid movement
                print('Flytter %s fra (%i,%i) til (%i,%i)!' % (brikke_flyttes.letter, fromX, fromY, toX, toY))
                self.sjakkbrett[fromX][fromY] = None  # Valgt rute blir tom
                brikke_flyttes.x = toX  # x-verdien til objektet oppdateres...
                brikke_flyttes.y = toY  # y-verdien til objektet oppdateres...
                self.sjakkbrett[toX][toY] = brikke_flyttes  # Destinasjonsruten får brikken
                self.history.append(str(self.turn) + ': ' + history)  # Trekket som ble gjort lagres i history-listen
                input_ikke_valid = False
                ########################################################################################################
                if brikke_flyttes.letter == 'K':
                    self.W_king_pos = [toX, toY]  # Lagrer posisjonen til hvit konge
                elif brikke_flyttes.letter == 'k':
                    self.B_king_pos = [toX, toY]  # Lagrer posisjonen til svart konge
                ########################################################################################################
                if self.turn % 2:  # Hvis hvit sin tur
                    if self.B_king_pos in trussel_etter[3]:  # Hvis svart konge er truet etter hvit sitt trekk
                        print('SJAKK')
                        for x in trussel_etter[0]:
                            if not self.sjakkbrett[x[0]][x[1]] and x not in trussel_etter[3]:  # Trekk som ikke er truet
                                print('Det er visst en vei ut')
                            else:  # Hvis konge er innestengt
                                pass  # Mer kommer+++
                else:
                    if self.W_king_pos in trussel_etter[1]:  # Hvis hvit konge er truet etter svart sitt trekk
                        print('SJAKK')
                        for x in trussel_etter[2]:  # For mulige trekk til hvit konge
                            if not self.sjakkbrett[x[0]][x[1]] and x not in trussel_etter[1]:  # Trekk som ikke er truet
                                print('Det er visst en vei ut')
                            else:  # Hvis konge er innestengt
                                pass  # Mer kommer+++
                ########################################################################################################
                if (brikke_flyttes.letter == 'P' or brikke_flyttes.letter == 'p') and (brikke_flyttes.y == 7 or brikke_flyttes.y == 0):
                    if self.turn % 2:
                        farge = 'W'
                        x = 7
                    else:
                        farge = 'B'
                        x = 0
                    ny_brikke = input('Gratulerer, velg en brikke du ønsker').lower()
                    if ny_brikke == 'r':
                        self.sjakkbrett[toX][toY] = Rook(farge, x, toY)
                    elif ny_brikke == 'n':
                        self.sjakkbrett[toX][toY] = Knight(farge, x, toY)
                    elif ny_brikke == 'b':
                        self.sjakkbrett[toX][toY] = Bishop(farge, x, toY)
                    elif ny_brikke == 'q':
                        self.sjakkbrett[toX][toY] = Queen(farge, x, toY)
                ########################################################################################################
            else:
                print('Ulovlig trekk!')
                # input_ikke_valid er fremdeles True, så loopen kjøres igjen

    # ==================================================================================================================

    # Lager liste med trusler for svart og hvit
    def threat(self):  # Funksjonen som lager en liste over trusler
        B_piece_threat = []  # Listen som skal brukes for å lagre trusselen som de svarte brikkene lager
        W_piece_threat = []  # Listen som skal brukes for å lagre trusselen som de hvite brikkene lager
        W_king_threat = []  # Listen som skal brukes for å lagre trusselen som den hvite kongen lager
        B_king_threat = []  # Listen som skal brukes for å lagre trusselen som den svarte kongen lager
        for x in range(8):  # Går gjennom alle ruter med koordinater [x,y]
            for y in range(8):
                this_pos = self.sjakkbrett[x][y]  # Denne refererer til den gjeldende ruten
                pos = self.sjakkbrett  # Denne refererer til alle ruter
                if this_pos == None:  # Hvis ruten ikke inneholder noe så hopper vi over den
                    pass

                elif this_pos.letter == 'P' or this_pos.letter == 'p':  # Hvis ruten inneholder en bonde
                    if this_pos.letter == 'P':  # Hvis bonden er hvit
                        tall = 1
                        save = W_piece_threat  # Lagrer trusselen til hvit sin liste
                    else:
                        tall = -1
                        save = B_piece_threat  # Lagrer trusselen til svart sin liste
                    save.append([this_pos.x + 1, this_pos.y + tall])  # Lagrer det skrå angrepet til bonden
                    save.append([this_pos.x - 1, this_pos.y + tall])  # Lagrer det andre skrå angrepet til bonden

                elif this_pos.letter == 'r' or this_pos.letter == 'R':  # Hvis ruten inneholder et tårn
                    if this_pos.letter == 'r':  # Hvis tårnet er svart
                        save = B_piece_threat  # Lagrer trusselen til svart sin liste
                    else:
                        save = W_piece_threat  # Lagrer trusselen til hvit sin liste
                    for i in range(-1, 2):  # loop med tallene -1 og 1. 0 ignoreres
                        if i == 0:  # Ignoreres som sagt
                            pass  # Yup...
                        else:
                            for p in range(-1, 2):
                                # Same shit, -1 og 1. Hvis du har MAD skills så ser du at me har
                                # tallkombinasjonane [-1,-1],[-1,1],[1,-1],[1,1], dette er fordi tårnet kan bevege seg
                                # i fire retninger
                                if p == 0:
                                    pass
                                else:
                                    teller = 0  # Må ha en teller siden tårnet bevege seg bortøve uknow.
                                    while True:
                                        teller += 1  # Øker teller...
                                        if p == 1:  # opp/ned
                                            k = this_pos.y + teller * i  # opp hvis i=1 og ned hvis i=-1
                                            l = this_pos.x  # Konstant
                                            if (k) > 7 or (k) < 0:  # ABORT hvis ruten er utenfor brettet
                                                break
                                        else:  # høyre/venstre
                                            k = this_pos.y  # Konstant
                                            l = this_pos.x + teller * i  # høyre hvis i=1 og venstre hvis i=-1
                                            if (l) > 7 or (l) < 0:  # ABORT hvis ruten er utenfor brettet
                                                break
                                        if pos[l][k]:  # Hvis ruten har en brikke i seg så lagres den og loopen stoppes
                                            save.append([l, k])
                                            break
                                        else:
                                            save.append([l, k])

                elif this_pos.letter == 'q' or this_pos.letter == 'Q':  # Hvis ruten inneholder en dronning
                    # OK, dronning e basically bare tårn og løper i samme if-setning. Se på de for mer info.
                    if this_pos.letter == 'q':  # Hvis svart dronning
                        save = B_piece_threat  # Lagrer trusselen til svart sin liste
                    else:
                        save = W_piece_threat  # Lagrer trusselen til hvit sin liste
                    for i in range(-1, 2):  # Same deal, -1 og 1
                        if i == 0:  # Ignored
                            pass
                        else:
                            for p in range(-1, 2):  # Same deal, -1 og 1
                                if p == 0:  # Ignored
                                    pass
                                else:
                                    teller1 = 0
                                    while True:  # løper-delen
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
                                    while True:  # tårn-delen
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

                elif this_pos.letter == 'k' or this_pos.letter == 'K':  # Hvis ruten inneholder en konge
                    if this_pos.letter == 'k':  # Hvis svart konge!
                        save = B_king_threat  # Lagrer trusselen til svart sin konge-liste
                    else:
                        save = W_king_threat  # Lagrer trusselen til hvit sin konge-liste
                    for i in range(-1, 2):  # Same deal, -1 og 1
                        for p in range(-1, 2):  # Same deal, -1 og 1
                            if i == p and i == 0:  # Ignored
                                pass
                            else:
                                if 0 <= this_pos.x + i <= 7 and 0 <= this_pos.y + p <= 7:  # Hvis innenfor brettet
                                    save.append([this_pos.x + i, this_pos.y + p])  # Save that shiet

                elif this_pos.letter == 'b' or this_pos.letter == 'B':  # Hvis ruten inneholder en løper
                    if this_pos.letter == 'b':  # Hvis svart løper!
                        save = B_piece_threat
                    else:
                        save = W_piece_threat
                    for i in range(-1, 2):  # Same deal, -1 og 1
                        if i == 0:  # Ignored
                            pass
                        else:
                            for p in range(-1, 2):  # Same deal, -1 og 1
                                if p == 0:  # Ignored
                                    pass
                                else:
                                    teller = 0  # Teller, fordi løper bevege seg bortøve
                                    while True:
                                        teller += 1  # Teller økes :O
                                        if p == 1:  # Opp/høyre (i=1) eller ned/venstre (i=-1)
                                            k = this_pos.y + teller * i
                                            l = this_pos.x + teller * i
                                        else:  # Opp/venstre (i=1) eller ned/høyre (i=-1)
                                            k = this_pos.y + teller * i
                                            l = this_pos.x - teller * i
                                        if k > 7 or k < 0 or l > 7 or l < 0:
                                            break
                                        elif pos[l][k]:  # Hvis ruten inneholder en brikke. Lagres og avslutter
                                            save.append([l, k])
                                            break
                                        else:  # Hvis tom lagres denne og loopen fortsetter
                                            save.append([l, k])

                elif this_pos.letter == 'n' or this_pos.letter == 'N':  # Hvis ruten inneholder en hest
                    if this_pos.letter == 'n':  # Hvis svart hest
                        save = B_piece_threat  # Lagrer trusselen til svart sin liste
                    else:
                        save = W_piece_threat  # Lagrer trusselen til hvit sin liste
                    for i in range(-2, 3):  # -2, -1, 1, 2
                        if i == 0:  # Ignored
                            pass
                        else:
                            for p in range(-2, 3):  # -2, -1, 1, 2
                                if p == 0 or abs(p) == abs(i):  # Hopper over tilfellene n[r i og p er like
                                    pass
                                else:  # Nå har me [-2, -1],[-2, 1],[-1, -2],[-1, 2],[1, -2],[1, 2], [2, -1], [2, 1]
                                    if 0 <= this_pos.x + i <= 7 and 0 <= this_pos.y + p <= 7:  # hvis innenfor brettet
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
        # Returnerer trussellisten til svart konge[0], svarte brikker[1], hvit konge[2] og hvite brikker[3]


Engine()
