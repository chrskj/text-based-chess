# *-* coding: UTF-8 *-*
from gamepieces import *


# sjakkbrikker: bonde: P, tÃ¥rn: R, hest: N, lÃ¸per: B, konge: K, dronning: Q

class GameBoard(object):

    # __init__ blir alltid kalt når objektet lages. Så typisk setup-kode legges her
    def __init__(self):
        """Creates the board which will be used."""
        brett = [['.' for l in range(8)] for i in range(8)]

        # brettet initialiseres til matrise med kun None
        # fylles inn av game_piece i piece_setup_raggiz
        self.brett_raggiz = [[None for l in range(8)] for i in range(8)]
        self.piece_setup_raggiz()
        

    def piece_setup_raggiz(self):
        # bare ha objektene rett i brett
        
        self.brett_raggiz[0][0] = Rook('W', 0, 0)
        self.brett_raggiz[0][7] = Rook('W', 0, 7)
        self.brett_raggiz[0][1] = Knight('W', 0, 1)
        self.brett_raggiz[0][6] = Knight('W', 0, 6)
        self.brett_raggiz[0][2] = Bishop('W', 0, 2)
        self.brett_raggiz[0][5] = Bishop('W', 0, 5)
        self.brett_raggiz[0][3] = Queen('W', 0, 3)
        self.brett_raggiz[0][4] = King('W', 0, 4)
        for i in range(8):   # bønder
            self.brett_raggiz[1][i] = Pawn('W', 1, i)

        self.brett_raggiz[7][0] = Rook('B', 7, 0)
        self.brett_raggiz[7][7] = Rook('B', 7, 7)
        self.brett_raggiz[7][1] = Knight('B', 7, 1)
        self.brett_raggiz[7][6] = Knight('B', 7, 6)
        self.brett_raggiz[7][2] = Bishop('B', 7, 2)
        self.brett_raggiz[7][5] = Bishop('B', 7, 5)
        self.brett_raggiz[7][3] = Queen('B', 7, 3)
        self.brett_raggiz[7][4] = King('B', 7, 4)
        for i in range(8):   # bønder
            self.brett_raggiz[6][i] = Pawn('B', 6, i)


    def console_board_raggiz(self):
        for i in reversed(range(8)):  # gå gjennom hver rad, printe rad 1 (white) til slutt (nederst)
            rad = self.brett_raggiz[i]
            rad_string = ""
            for rute in rad:  # gå gjennom hver rute i raden
                
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
            print( rad_string )
            

    def piece_setup(self, pos):
        """Sets up the individual pieces. Each piece is its own object with the name of the gamepiece + its position.
        For example the rook on position 0,0 will have the name 'Rook00'. Each object is saved in a dictionary called 'd'."""
        d = {}

        for y in range(0, len(pos), 7):
            for x in range(0, len(pos), 7):
                if y == 0 or y == 1:
                    d['Rook'+str(x)+str(y)] = Rook('B', x, y)
                    pos[y][x] = (d['Rook'+str(x)+str(y)].letter).lower()
                else:
                    d['Rook'+str(x)+str(y)] = Rook('W', x, y)
                    pos[y][x] = d['Rook'+str(x)+str(y)].letter

        for y in range(0, len(pos), 7):
            for x in range(1, len(pos), 5):
                if y == 0 or y == 1:
                    d['Knight'+str(x)+str(y)] = Knight('B', x, y)
                    pos[y][x] = (d['Knight'+str(x)+str(y)].letter).lower()
                else:
                    d['Knight'+str(x)+str(y)] = Knight('W', x, y)
                    pos[y][x] = d['Knight'+str(x)+str(y)].letter

        for y in range(0, len(pos), 7):
            for x in range(2, len(pos), 3):
                if y == 0 or y == 1:
                    d['Bishop'+str(x)+str(y)] = Bishop('B', x, y)
                    pos[y][x] = (d['Bishop'+str(x)+str(y)].letter).lower()
                else:
                    d['Bishop'+str(x)+str(y)] = Bishop('W', x, y)
                    pos[y][x] = d['Bishop'+str(x)+str(y)].letter

        for y in range(0, len(pos), 7):
            for x in range(3, len(pos), 7):
                if y == 0 or y == 1:
                    d['Queen'+str(x)+str(y)] = Queen('B', x, y)
                    pos[y][x] = (d['Queen'+str(x)+str(y)].letter).lower()
                else:
                    d['Queen'+str(x)+str(y)] = Queen('W', x, y)
                    pos[y][x] = d['Queen'+str(x)+str(y)].letter

        for y in range(0, len(pos), 7):
            for x in range(4, len(pos), 7):
                if y == 0 or y == 1:
                    d['King'+str(x)+str(y)] = King('B', x, y)
                    pos[y][x] = (d['King'+str(x)+str(y)].letter).lower()
                else:
                    d['King'+str(x)+str(y)] = King('W', x, y)
                    pos[y][x] = d['King'+str(x)+str(y)].letter

        for y in range(1, len(pos), 5):
            for x in range(0, len(pos), 1):
                if y == 0 or y == 1:
                    d['Pawn'+str(x)+str(y)] = Pawn('B', x, y)
                    pos[y][x] = (d['Pawn'+str(x)+str(y)].letter).lower()
                else:
                    d['Pawn'+str(x)+str(y)] = Pawn('W', x, y)
                    pos[y][x] = d['Pawn'+str(x)+str(y)].letter

        return [pos, d]

    def console_board(self, pos):
        """Visualizes the game board in the console."""

        print('     0 1 2 3 4 5 6 7 \n',
              '   ________________\n',
              '0 | %s %s %s %s %s %s %s %s\n' % (pos[0][0], pos[0][1], pos[0][2], pos[0][3], pos[0][4], pos[0][5],
                                              pos[0][6], pos[0][7]),
              '1 | %s %s %s %s %s %s %s %s\n' % (pos[1][0], pos[1][1], pos[1][2], pos[1][3], pos[1][4], pos[1][5],
                                             pos[1][6], pos[1][7]),
              '2 | %s %s %s %s %s %s %s %s\n' % (pos[2][0], pos[2][1], pos[2][2], pos[2][3], pos[2][4], pos[2][5],
                                             pos[2][6], pos[2][7]),
              '3 | %s %s %s %s %s %s %s %s\n' % (pos[3][0], pos[3][1], pos[3][2], pos[3][3], pos[3][4], pos[3][5],
                                             pos[3][6], pos[3][7]),
              '4 | %s %s %s %s %s %s %s %s\n' % (pos[4][0], pos[4][1], pos[4][2], pos[4][3], pos[4][4], pos[4][5],
                                             pos[4][6], pos[4][7]),
              '5 | %s %s %s %s %s %s %s %s\n' % (pos[5][0], pos[5][1], pos[5][2], pos[5][3], pos[5][4], pos[5][5],
                                             pos[5][6], pos[5][7]),
              '6 | %s %s %s %s %s %s %s %s\n' % (pos[6][0], pos[6][1], pos[6][2], pos[6][3], pos[6][4], pos[6][5],
                                             pos[6][6], pos[6][7]),
              '7 | %s %s %s %s %s %s %s %s\n' % (pos[7][0], pos[7][1], pos[7][2], pos[7][3], pos[7][4], pos[7][5],
                                             pos[7][6], pos[7][7])
              )
