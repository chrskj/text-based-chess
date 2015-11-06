from gamepieces import *


# sjakkbrikker: bonde: P, tårn: R, hest: N, løper: B, konge: K, dronning: Q

class GameBoard(object):
    def __init__(self):
        pos = self.game_board()
        self.piece_setup(pos)
        self.console_board(pos)

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
                    pos[6][y] = 'P'
                    pos[1][y] = 'p'
            else:
                for y in range(8):
                    teller += 1
                    pos[x][y] = pieces[teller]
                    pos[0][y] = pos[0][y].lower()

    def console_board(self, pos):
        """Visualizes the game board in the console."""

        print(' %s %s %s %s %s %s %s %s\n' % (pos[0][0], pos[0][1], pos[0][2], pos[0][3], pos[0][4], pos[0][5],
                                              pos[0][6], pos[0][7]),
              '%s %s %s %s %s %s %s %s\n' % (pos[1][0], pos[1][1], pos[1][2], pos[1][3], pos[1][4], pos[1][5],
                                             pos[1][6], pos[1][7]),
              '%s %s %s %s %s %s %s %s\n' % (pos[2][0], pos[2][1], pos[2][2], pos[2][3], pos[2][4], pos[2][5],
                                             pos[2][6], pos[2][7]),
              '%s %s %s %s %s %s %s %s\n' % (pos[3][0], pos[3][1], pos[3][2], pos[3][3], pos[3][4], pos[3][5],
                                             pos[3][6], pos[3][7]),
              '%s %s %s %s %s %s %s %s\n' % (pos[4][0], pos[4][1], pos[4][2], pos[4][3], pos[4][4], pos[4][5],
                                             pos[4][6], pos[4][7]),
              '%s %s %s %s %s %s %s %s\n' % (pos[5][0], pos[5][1], pos[5][2], pos[5][3], pos[5][4], pos[5][5],
                                             pos[5][6], pos[5][7]),
              '%s %s %s %s %s %s %s %s\n' % (pos[6][0], pos[6][1], pos[6][2], pos[6][3], pos[6][4], pos[6][5],
                                             pos[6][6], pos[6][7]),
              '%s %s %s %s %s %s %s %s\n' % (pos[7][0], pos[7][1], pos[7][2], pos[7][3], pos[7][4], pos[7][5],
                                             pos[7][6], pos[7][7])
              )