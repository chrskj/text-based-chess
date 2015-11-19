class User(object):
    def __init__(self, color):
        self.color = color

    def movement_input(self):
        """Ask the user for movement input"""
        bokstav_tall = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        fra = input('Select the piece you want to move(xy): ')
        til = input('Select where you want to move(x2y2): ')

        x = bokstav_tall[fra[0]]
        y = int(fra[1]) - 1
        x2 = bokstav_tall[til[0]]
        y2 = int(til[1]) - 1

        return [x, y, x2, y2]
