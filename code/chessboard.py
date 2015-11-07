import tkinter as tk
from pathlib import Path

class ChessBoard(tk.Frame):

    def __init__(self, parent):

        #p = Path(__file__).parents[0]
        #print(str(p) + '/resources/debrief2.wav')

        # length of one square in px
        size = 70
        width = self.height = 70*8

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

def main():
    root = tk.Tk()
    brett = ChessBoard(root)
    brett.pack(side = 'top', fill = 'both', expand = True)
    root.mainloop()

main()
