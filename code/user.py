class User(object):
    def __init__(self, color):
        self.color = color

    def movement_input(self):
        """Ask the user for movement input"""

        a_ok = False
        while not a_ok:

            try:
                bokstav_tall = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
                fra = input('Select the piece you want to move(xy): ')
                if fra == 'GG':
                    return fra  # Returnerer bare 'GG' fra spiller
                til = input('Select where you want to move(x2y2): ')

                x = bokstav_tall[fra[0]]
                y = int(fra[1]) - 1
                x2 = bokstav_tall[til[0]]
                y2 = int(til[1]) - 1

                a_ok = True
                
            except:
                # hvis noe gikk galt, do it all again, siden a_ok er false
                # gjør dette for å hindre programkrasj hvis bruker skriver
                # inn noe som ikke er en key i dictionary og utløser
                # keyError
                print('Cmon man, not even valid input ༼⊙ʖ̯⊙༽ \n')

        return [x, y, x2, y2, '%s -> %s' % (fra, til)]
