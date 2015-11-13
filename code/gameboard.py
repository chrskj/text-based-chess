from gamepieces import *


# sjakkbrikker: bonde: P, tårn: R, hest: N, løper: B, konge: K, dronning: Q

class GameBoard(object):
    def __init__(self):
        self.pos = self.game_board()
        self.piece_setup(self.pos)
        self.console_board(self.pos)

    def game_board(self):
        """Creates the board which will be used."""
        brett = [1 for i in range(8)]
        for i in range(8):
            brett[i] = ['.' for l in range(8)]

        return brett

    def piece_setup(self, pos):
        """Sets up the individual pieces."""
        pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for x in (0, 1, 6, 7):
            teller = -1
            if x == 1 or x == 6:
                for y in range(8):
                    self.pos[6][y] = 'P'
                    self.pos[1][y] = 'p'
            else:
                for y in range(8):
                    teller += 1
                    self.pos[x][y] = pieces[teller]
                    self.pos[0][y] = self.pos[0][y].lower()

    def console_board(self, pos):
        """Visualizes the game board in the console."""

        print(' %s %s %s %s %s %s %s %s\n' % (self.pos[0][0], self.pos[0][1], self.pos[0][2], self.pos[0][3], self.pos[0][4], self.pos[0][5],
                                              self.pos[0][6], self.pos[0][7]),
              '%s %s %s %s %s %s %s %s\n' % (self.pos[1][0], self.pos[1][1], self.pos[1][2], self.pos[1][3], self.pos[1][4], self.pos[1][5],
                                             self.pos[1][6], self.pos[1][7]),
              '%s %s %s %s %s %s %s %s\n' % (self.pos[2][0], self.pos[2][1], self.pos[2][2], self.pos[2][3], self.pos[2][4], self.pos[2][5],
                                             self.pos[2][6], self.pos[2][7]),
              '%s %s %s %s %s %s %s %s\n' % (self.pos[3][0], self.pos[3][1], self.pos[3][2], self.pos[3][3], self.pos[3][4], self.pos[3][5],
                                             self.pos[3][6], self.pos[3][7]),
              '%s %s %s %s %s %s %s %s\n' % (self.pos[4][0], self.pos[4][1], self.pos[4][2], self.pos[4][3], self.pos[4][4], self.pos[4][5],
                                             self.pos[4][6], self.pos[4][7]),
              '%s %s %s %s %s %s %s %s\n' % (self.pos[5][0], self.pos[5][1], self.pos[5][2], self.pos[5][3], self.pos[5][4], self.pos[5][5],
                                             self.pos[5][6], self.pos[5][7]),
              '%s %s %s %s %s %s %s %s\n' % (self.pos[6][0], self.pos[6][1], self.pos[6][2], self.pos[6][3], self.pos[6][4], self.pos[6][5],
                                             self.pos[6][6], self.pos[6][7]),
              '%s %s %s %s %s %s %s %s\n' % (self.pos[7][0], self.pos[7][1], self.pos[7][2], self.pos[7][3], self.pos[7][4], self.pos[7][5],
                                             self.pos[7][6], self.pos[7][7])
              )