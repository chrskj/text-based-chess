import tkinter as tk
from PIL import Image, ImageTk
# from pathlib import Path

class ChessBoard(tk.Frame):

    def __init__(self, parent):

        #p = Path(__file__).parents[0]
        #print(str(p) + '/resources/debrief2.wav')

        # length of one square in px
        size = 70
        width = self.height = 70*8

        self.images = [ [None for x in range(8)] for y in range(8) ]
        self.images.append(tk.PhotoImage(file='resources/b_b.png'))

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth = 0, highlightthickness = 0,
                                width = width, height = self.height,
                                background = 'blue')


        self.canvas.pack(side = 'top', fill = 'both', expand = True)

        fill = fill1 = 'green'
        fill2 = 'white'
        for i in range(8):
            for j in range(8):
                if j != 0:
                    fill = fill2 if (fill == fill1) else fill1
                    print(fill)
                self.canvas.create_rectangle(j*size, i*size, (j+1)*size,
                                             (i+1)*size, fill=fill )


    def place_piece(self, x, y, piece_letter, piece_color):
        letr = piece_letter.lower()
        colr = piece_color[0].lower()

        photo = tk.PhotoImage(file=(letr + '_' + colr + '.png'))

        self.images[x][y] = photo


    def remove_piece(self, x, y):
        self.images[x][y] = None


    def visualize(self):
        for i in range(8):
            rad = self.images[i]
            for j in range(8):
                rute = rad[j]
                if rute:
                    self.canvas.create_image(
                        (i*70) + 5,
                        (j * 70 ) + 5,
                        file = rute
                    )


root = tk.Tk()
brett = ChessBoard(root)
brett.pack(side = 'top', fill = 'both', expand = True)
root.mainloop()

print('213123')

brett.place_piece(3, 4, 'b','b')

