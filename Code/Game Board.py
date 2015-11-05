"""Ideer for sjakkbrikker: bonde: P, tårn: R, hest: N, springer: B, konge: K, dronning: Q.
Motspiller kan ha bokstaver i små bokstaver"""


class GameBoard(object):

    def __init__(self):
        self.game_board()
        self.console_board()

    def game_board(self):
        """Creates the board which will be used."""
        brett = [1 for i in range(8)]
        for i in range(8):
            brett[i] = ['.' for l in range(8)]

        return brett

    def console_board(self):
        """Visualizes the game board in the console."""
        print(' %s %s %s %s %s %s %s %s\n' % ('+', '+', '+', '+', '+', '+', '+', '+'),
              '%s %s %s %s %s %s %s %s\n' % ('+', '+', '+', '+', '+', '+', '+', '+'),
              '%s %s %s %s %s %s %s %s\n' % ('+', '+', '+', '+', '+', '+', '+', '+'),
              '%s %s %s %s %s %s %s %s\n' % ('+', '+', '+', '+', '+', '+', '+', '+'),
              '%s %s %s %s %s %s %s %s\n' % ('+', '+', '+', '+', '+', '+', '+', '+'),
              '%s %s %s %s %s %s %s %s\n' % ('+', '+', '+', '+', '+', '+', '+', '+'),
              '%s %s %s %s %s %s %s %s\n' % ('+', '+', '+', '+', '+', '+', '+', '+'),
              '%s %s %s %s %s %s %s %s\n' % ('+', '+', '+', '+', '+', '+', '+', '+')
              )

GameBoard()