# *-* coding: UTF-8 *-*
# sjakkbrikker: bonde: P, tÅrn: R, hest: N, løper: B, konge: K, dronning: Q

class Game_Piece(object):
    # parent class for game pieces, all game pieces will inherit from this one

    def __init__(self, col, x, y):
        # color 'W' or 'B'
        self.color = col
        # x and y in [0, 7]
        self.x = x
        self.y = y

    def is_valid_movement(self, x2, y2, brett, history, trussel_før):
        # if not moving at all
        if self.x == x2 and self.y == y2:
            return False

        # if attempting to move outside of board
        if x2 > 7 or x2 < 0 or y2 > 7 or y2 < 0:
            return False
        return True


class Knight(Game_Piece):
    def __init__(self, col, x, y):
        super(Knight, self).__init__(col, x, y)
        if self.color == 'W':
            self.letter = 'N'
        else:
            self.letter = 'n'

    def is_valid_movement(self, x2, y2, brett, history, trussel_før):

        # if the movement-generalistics (e det et ord?) are ok
        if not super(Knight, self).is_valid_movement(x2, y2, brett, history, trussel_før):
            return False

        # the four moves to the "sides"
        if abs(x2 - self.x) == 2 and abs(y2 - self.y) == 1:
            return True

        # the four moves "up" and "down"
        if abs(x2 - self.x) == 1 and abs(y2 - self.y) == 2:
            return True

        # if not any of the eight moves above, we've exhausted our options
        return False


class Queen(Game_Piece):
    def __init__(self, col, x, y):

        # the parent class, Game_Piece, assigns color, x and y
        super(Queen, self).__init__(col, x, y)
        if self.color == 'W':
            self.letter = 'Q'
        else:
            self.letter = 'q'

    def is_valid_movement(self, x2, y2, brett, history, trussel_før):

        # not outside board
        if not super(Queen, self).is_valid_movement(x2, y2, brett, history, trussel_før):
            return False

        # if diagonal moving, x and y change by +- the same amount
        if abs(x2 - self.x) == abs(y2 - self.y):
            if x2 - self.x > 0 and y2 - self.y > 0:
                for i in range(1, x2 - self.x):
                    if brett[self.x + i][self.y + i]:
                        print('Det va visst noge imellom her.')
                        return False
            if x2 - self.x < 0 and y2 - self.y > 0:
                for i in range(1, self.x - x2):
                    if brett[self.x - i][self.y + i]:
                        print('Det va visst noge imellom her.')
                        return False
            if x2 - self.x > 0 and y2 - self.y < 0:
                for i in range(1, x2 - self.x):
                    if brett[self.x + i][self.y - i]:
                        print('Det va visst noge imellom her.')
                        return False
            if x2 - self.x < 0 and y2 - self.y < 0:
                for i in range(1, self.x - x2):
                    if brett[self.x - i][self.y - i]:
                        print('Det va visst noge imellom her.')
                        return False
            return True

        # if straight moving, x or y stays put, the other moves
        if (x2 == self.x and y2 != self.y) or (y2 == self.y and x2 != self.x):
            if x2 - self.x > 0:  # End more to the right than start
                for i in range(1, x2 - self.x):
                    if brett[x2 - i][self.y]:
                        print('Det va visst noge imellom her.')
                        return False
            if self.x - x2 > 0:  # Start more to the right than end
                for i in range(1, self.x - x2):
                    if brett[self.x - i][self.y]:
                        print('Det va visst noge imellom her.')
                        return False
            if y2 - self.y > 0:  # End higher up than start
                for i in range(1, y2 - self.y):
                    if brett[self.x][y2 - i]:
                        print('Det va visst noge imellom her.')
                        return False
            if self.y - y2 > 0:  # Start higher up than end
                for i in range(1, self.y - y2):
                    if brett[self.x][self.y - i]:
                        print('Det va visst noge imellom her.')
                        return False
            return True

        return False


class Pawn(Game_Piece):
    def __init__(self, col, x, y):

        # the parent class, Game_Piece, assigns color, x and y
        super(Pawn, self).__init__(col, x, y)
        if self.color == 'W':
            self.letter = 'P'
        else:
            self.letter = 'p'

    def is_valid_movement(self, x2, y2, brett, history, trussel_før):

        # not outside board
        if not super(Pawn, self).is_valid_movement(x2, y2, brett, history, trussel_før):
            return False

        # using 'thing' to avoid processing each color on its own, which
        # would lead to a lot of duplicate code.
        if self.color == 'W':
            thing = 1
        else:
            thing = -1

        # if move forward (x unchanged)
        if self.x == x2:
            # if normal move
            if y2 - self.y == 1 * thing:
                return True
            # if first move
            if y2 - self.y == 2 * thing and (self.y == 1 or self.y == 6):
                return True

        # 0,3,4,9,10
        # if taking something (
        # diagonal, x changes by +-1, y changes by thing*1)
        if y2 - self.y == 1 * thing and abs(x2 - self.x) == 1:
            if not brett[x2][y2]:
                # En pasant!
                # hvis y2 = 2 eller 5 og forrige trekk beveget seg to steg fremover og er på samme x-verdi som deg
                if (y2 == 2 or y2 == 5) and int(history[-1][10]) - int(history[-1][4]) == 2 * -thing and ord(history[-1][9]) - 65 == x2:
                    brett[x2][y2 - thing] = None
                    return True
                print('Ingenting å angripe...')
                return False
            return True

        return False


class Rook(Game_Piece):
    def __init__(self, col, x, y):

        # the parent class, Game_Piece, assigns color, x and y
        super(Rook, self).__init__(col, x, y)
        if self.color == 'W':
            self.letter = 'R'
        else:
            self.letter = 'r'
        self.has_moved = False

    def is_valid_movement(self, x2, y2, brett, history, trussel_før):

        # not outside board
        if not super(Rook, self).is_valid_movement(x2, y2, brett, history, trussel_før):
            return False

        # if straight moving, x or y stays put, the other moves
        if (x2 == self.x and y2 != self.y) or (y2 == self.y and x2 != self.x):
            if x2 - self.x > 0:  # End more to the right than start
                for i in range(1, x2 - self.x):
                    if brett[x2 - i][self.y]:
                        print('Det va visst noge imellom her.')
                        return False
            if self.x - x2 > 0:  # Start more to the right than end
                for i in range(1, self.x - x2):
                    if brett[self.x - i][self.y]:
                        print('Det va visst noge imellom her.')
                        return False
            if y2 - self.y > 0:  # End higher up than start
                for i in range(1, y2 - self.y):
                    if brett[self.x][y2 - i]:
                        print('Det va visst noge imellom her.')
                        return False
            if self.y - y2 > 0:  # Start higher up than end
                for i in range(1, self.y - y2):
                    if brett[self.x][self.y - i]:
                        print('Det va visst noge imellom her.')
                        return False
            self.has_moved = True
            return True

        return False


class Bishop(Game_Piece):
    def __init__(self, col, x, y):

        # the parent class, Game_Piece, assigns color, x and y
        super(Bishop, self).__init__(col, x, y)
        if self.color == 'W':
            self.letter = 'B'
        else:
            self.letter = 'b'

    def is_valid_movement(self, x2, y2, brett, history, trussel_før):

        # not outside board
        if not super(Bishop, self).is_valid_movement(x2, y2, brett, history, trussel_før):
            return False

        if abs(x2 - self.x) == abs(y2 - self.y):
            if x2 - self.x > 0 and y2 - self.y > 0:
                for i in range(1, x2 - self.x):
                    if brett[self.x + i][self.y + i]:
                        print('Det va visst noge imellom her.')
                        return False
            if x2 - self.x < 0 and y2 - self.y > 0:
                for i in range(1, self.x - x2):
                    if brett[self.x - i][self.y + i]:
                        print('Det va visst noge imellom her.')
                        return False
            if x2 - self.x > 0 and y2 - self.y < 0:
                for i in range(1, x2 - self.x):
                    if brett[self.x + i][self.y - i]:
                        print('Det va visst noge imellom her.')
                        return False
            if x2 - self.x < 0 and y2 - self.y < 0:
                for i in range(1, self.x - x2):
                    if brett[self.x - i][self.y - i]:
                        print('Det va visst noge imellom her.')
                        return False
            return True

        return False


class King(Game_Piece):
    # Skeleton for the King-class

    def __init__(self, col, x, y):
        # the parent class, Game_Piece, assigns color, x and y
        super(King, self).__init__(col, x, y)
        if self.color == 'W':
            self.letter = 'K'
        else:
            self.letter = 'k'
        self.has_moved = False

    def is_valid_movement(self, x2, y2, brett, history, trussel_før):
        if self.color == 'W':  # Hvis hvit konge blir variablene trusselen som de svarte brikker påfører
            trussel_brikker = trussel_før[1]
            trussel_konge = trussel_før[0]
            trussel_Vbrikker = trussel_før[3]
        else:
            trussel_brikker = trussel_før[3]
            trussel_konge = trussel_før[2]
            trussel_Vbrikker = trussel_før[1]

        # not outside board
        if not super(King, self).is_valid_movement(x2, y2, brett, history, trussel_før):
            return False

        # Hvis ruten er truet
        if [x2, y2] in trussel_brikker:
            print('Konge er truet!')
            return False

        # Hvis ruten er truet av motstanderens konge
        if [x2, y2] in trussel_konge and [x2, y2] not in trussel_Vbrikker:
            print('Sorry dude, you have no backup.')
            return False

        # Diagonal movement for the king
        if abs(x2 - self.x) == 1 and abs(y2 - self.y) == 1:
            self.has_moved = True
            return True

        # up/down-movement for the king
        if x2 == self.x and abs(y2 - self.y) == 1:
            self.has_moved = True
            return True

        # left/right-movement for the king
        if y2 == self.y and abs(x2 - self.x) == 1:
            self.has_moved = True
            return True

        # If first move
        if not self.has_moved and [self.x, self.y] not in trussel_brikker:

            # Kort rokade!
            if self.y == y2 and x2 - self.x == 2 and not brett[7][self.y].has_moved and not brett[5][self.y] and \
                    [5, self.y] not in trussel_brikker:
                self.has_moved = True  # Konge har flyttet seg
                brett[7][self.y].has_moved = True  # Tårn har flyttet seg
                brett[7][self.y].x = 5  # Tårn får tilegnet x-verdien 5
                brett[5][self.y] = brett[7][self.y]  # Tårn flyttes til rute [5,y]
                brett[7][self.y] = None  # Forrige rute blir tom
                return True

            # Lang rokade!
            if self.y == y2 and self.x - x2 == 3 and not brett[0][self.y].has_moved and not brett[2][self.y] and not \
                    brett[3][self.y] and [2, self.y] not in trussel_brikker and [3, self.y] not in trussel_brikker:
                self.has_moved = True  # Konge har flyttet seg
                brett[0][self.y].has_moved = True  # Tårn har flyttet seg
                brett[0][self.y].x = 2  # Tårn får tilegnet x-verdien 2
                brett[2][self.y] = brett[0][self.y]  # Tårn flyttes til rute [2,y]
                brett[0][self.y] = None  # Forrige rute blir tom
                return True

        return False
