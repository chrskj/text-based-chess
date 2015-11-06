class User(object):
    def __init__(self, color):
        self.color = color

    def movement_input(self):
        """Ask the user for movement input"""
        x, y = input('Select the piece you want to move(x y): ').split()
        x2, y2 = input('Select where you want to move(x y): ').split()

        return [x, y, x2, y2]
