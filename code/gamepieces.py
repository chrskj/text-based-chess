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

    def is_valid_movement(self, x2, y2, brett):
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
        self.letter = 'N'

    def is_valid_movement(self, x2, y2, brett):

        # if the movement-generalistics (e det et ord?) are ok
        if not super(Knight, self).is_valid_movement(x2, y2, brett):
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
        self.letter = 'Q'

    def is_valid_movement(self, x2, y2, brett):

        # not outside board
        if not super(Queen, self).is_valid_movement(x2, y2, brett):
            return False

        # if diagonal moving, x and y change by +- the same amount
        if abs(x2 - self.x) == abs(y2 - self.y):
            return True

        # if straight moving, x or y stays put, the other moves
        if (x2 == self.x and y2 != self.y) or (y2 == self.y and x2 != self.x):
            return True

        return False


class Pawn(Game_Piece):
    def __init__(self, col, x, y):

        # the parent class, Game_Piece, assigns color, x and y
        super(Pawn, self).__init__(col, x, y)
        self.letter = 'P'

    def is_valid_movement(self, x2, y2, brett):

        # not outside board
        if not super(Pawn, self).is_valid_movement(x2, y2, brett):
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

        # if taking something (
        # diagonal, x changes by +-1, y changes by thing*1)
        if y2 - self.y == 1 * thing and abs(x2 - self.x) == 1:
            return True

        return False


class Rook(Game_Piece):
    def __init__(self, col, x, y):

        # the parent class, Game_Piece, assigns color, x and y
        super(Rook, self).__init__(col, x, y)
        self.letter = 'R'
        self.has_moved = False

    def is_valid_movement(self, x2, y2, brett):

        # not outside board
        if not super(Rook, self).is_valid_movement(x2, y2, brett):
            return False

        # if moving horizontally
        if abs(self.x - x2) > 0 and self.y == y2:
            self.has_moved = True
            return True

        # if moving vertically
        if self.x == x2 and abs(self.y - y2) > 0:
            self.has_moved = True
            return True

        return False


class Bishop(Game_Piece):
    def __init__(self, col, x, y):

        # the parent class, Game_Piece, assigns color, x and y
        super(Bishop, self).__init__(col, x, y)
        self.letter = 'B'

    def is_valid_movement(self, x2, y2, brett):

        # not outside board
        if not super(Bishop, self).is_valid_movement(x2, y2, brett):
            return False

        # if the bishop will be moving horizontally
        if abs(self.x - x2) == abs(self.y - y2):
            return True

        return False


class King(Game_Piece):
    # Skeleton for the King-class

    def __init__(self, col, x, y):
        # the parent class, Game_Piece, assigns color, x and y
        super(King, self).__init__(col, x, y)
        self.letter = 'K'
        self.has_moved = False

    def is_valid_movement(self, x2, y2, brett):

        # not outside board
        if not super(King, self).is_valid_movement(x2, y2, brett):
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
        if not self.has_moved:

            # Kort rokade!
            if self.y == y2 and x2 - self.x == 2 and not brett[7][self.y].has_moved and not brett[5][self.y]:
                self.has_moved = True
                brett[7][self.y].has_moved = True
                brett[7][self.y].x = 5
                brett[5][self.y] = brett[7][self.y]
                brett[7][self.y] = None
                return True

            # Lang rokade!
            if self.y == y2 and self.x - x2 == 3 and not brett[0][self.y].has_moved and not brett[2][self.y] and not \
                    brett[3][self.y]:
                self.has_moved = True
                brett[0][self.y].has_moved = True
                brett[0][self.y].x = 2
                brett[2][self.y] = brett[0][self.y]
                brett[0][self.y] = None
                return True

        return False
