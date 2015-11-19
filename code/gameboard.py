# *-* coding: UTF-8 *-*
from gamepieces import *


# sjakkbrikker: bonde: P, tÃ¥rn: R, hest: N, lÃ¸per: B, konge: K, dronning: Q

class GameBoard(object):
    # __init__ blir alltid kalt når objektet lages. Så typisk setup-kode legges her
    def __init__(self):
        """Creates the board which will be used."""
        # brettet initialiseres til matrise med kun None
        # fylles inn av game_piece i piece_setup
        self.brett = [[None for l in range(8)] for i in range(8)]
        self.piece_setup()

    def piece_setup(self):
        # bare ha objektene rett i brett

        self.brett[0][0] = Rook('W', 0, 0)
        self.brett[7][0] = Rook('W', 7, 0)
        self.brett[1][0] = Knight('W', 1, 0)
        self.brett[6][0] = Knight('W', 6, 0)
        self.brett[2][0] = Bishop('W', 2, 0)
        self.brett[5][0] = Bishop('W', 5, 0)
        self.brett[3][0] = Queen('W', 3, 0)
        self.brett[4][0] = King('W', 4, 0)
        for i in range(8):  # bønder
            self.brett[i][1] = Pawn('W', i, 1)

        self.brett[0][7] = Rook('B', 0, 7)
        self.brett[7][7] = Rook('B', 7, 7)
        self.brett[1][7] = Knight('B', 1, 7)
        self.brett[6][7] = Knight('B', 6, 7)
        self.brett[2][7] = Bishop('B', 2, 7)
        self.brett[5][7] = Bishop('B', 5, 7)
        self.brett[3][7] = Queen('B', 3, 7)
        self.brett[4][7] = King('B', 4, 7)
        for i in range(8):  # bønder
            self.brett[i][6] = Pawn('B', i, 6)

    def console_board(self):
        teller = 9
        for y in reversed(range(8)):  # gå gjennom hver rad, printe rad 1 (white) til slutt (nederst)
            teller -= 1
            rad_string = str(teller)+" "
            for x in (range(8)):  # gå gjennom hver rute i raden
                rute = self.brett[x][y]
                # hvis det IKKE er None i ruten, dvs hvis det er Game_Piece der
                if rute:
                    # Game_Piece har en egen attribute .letter
                    if rute.color == 'B':
                        rad_string += rute.letter.lower()
                    else:
                        rad_string += rute.letter
                # ellers, hvis det er None i ruten (den er tom)
                else:
                    rad_string += '.'

                rad_string += '  '  # sånn ting ikke står helt tett inntil hverandre
            print(rad_string)
        print('  A  B  C  D  E  F  G  H')