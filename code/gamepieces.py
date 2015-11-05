
######################## TO-DO ########################
# - Make King class                                   #
# - Probably something else                           #  
#                                                     #
# - When a move is attempted, a check must be made to #
#   ensure that the destination does not contain a    #
#   piece of the same color (NOT in this class,       #
#   probably in the "Game" class)                     #
# - Must also check for check or checkmate (again,    #
#   not in this class)                                #
#######################################################
# sjakkbrikker: bonde: P, tårn: R, hest: N, løper: B, konge: K, dronning: Q

class Game_Piece:

    # parent class for game pieces, all game pieces will inherit from this one

    def __init__(self, col, x, y, letter):
        # color 'W' or 'B'
        self.color = col
        # x and y in [0, 7]
        self.x = x
        self.y = y
        # letter for piece
        self.letter = letter

    def is_valid_movement(self, x2, y2):
        # if not moving at all
        if self.x == x2 and self.y == y2:
            return False

        # if attempting to move outside of board
        if x2 > 7 or x2 < 0 or y2 > 7 or y2 < 0:
            return False
        return True


class Knight(Game_Piece):

    def __init__(self, col, x, y, letter):
        super(Knight, self).__init__(col, x, y, letter)

    def is_valid_movement(self, x2, y2):

        # if the movement-generalistics (e det et ord?) are ok
        if not super(Knight, self).is_valid_movement(x2, y2):
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

    def __init__(self, col, x, y, letter):

        # the parent class, Game_Piece, assigns color, x and y
        super(Queen, self).__init__(col, x, y, letter)

    def is_valid_movement(self, x2, y2):

        # not outside board
        if not super(Queen, self).is_valid_movement(x2, y2):
            return False

        # if diagonal moving, x and y change by +- the same amount
        if abs(x2 - self.x) == abs(y2 - self.y):
            return True

        # if straight moving, x or y stays put, the other moves
        if (x2 == self.x and y2 != self.y) or (y2 == self.y and x2 != self.x):
            return True

        return False


class Pawn(Game_Piece):

    def __init__(self, col, x, y, letter):

        # the parent class, Game_Piece, assigns color, x and y
        super(Pawn, self).__init__(col, x, y, letter)

    def is_valid_movement(self, x2, y2):

        # not outside board
        if not super(Pawn, self).is_valid_movement(x2, y2):
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

    def __init__(self, col, x, y, letter):

        # the parent class, Game_Piece, assigns color, x and y
        super(Rook, self).__init__(col, x, y, letter)

    def is_valid_movement(self, x2, y2):

        # not outside board
        if not super(Rook, self).is_valid_movement(x2, y2):
            return False

        # if moving horizontally
        if abs(self.x - x2) > 0 and self.y == y2:
            return True

        # if moving vertically
        if self.x == x2 and abs(self.y - y2) > 0:
            return True

        return False


class Bishop(Game_Piece):

    def __init__(self, col, x, y, letter):

        # the parent class, Game_Piece, assigns color, x and y
        super(Bishop, self).__init__(col, x, y, letter)

    def is_valid_movement(self, x2, y2):

        # not outside board
        if not super(Bishop, self).is_valid_movement(x2, y2):
            return False

        # if the bishop will be moving horizontally
        if abs(self.x - x2) == abs(self.x - y2):
            return True

        return False


class King(Game_Piece):

    # Skeleton for the King-class
    def __init__(self, col, x, y, letter):

        # the parent class, Game_Piece, assigns color, x and y
        super(King, self).__init__(col, x, y, letter)

    def is_valid_movement(self, x2, y2):

        pass

        return False
