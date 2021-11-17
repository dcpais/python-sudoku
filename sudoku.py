import tkinter as tk
from tkinter.constants import ANCHOR
import numpy as np

class Sudoku:
    """
    class for Game logic.
    """
    pass


class View:

    def __init__(self, game: Sudoku, HEIGHT=600, WIDTH=500):
        """
        Initialize view class with all neccesary vars.
        View class holds root TK window and will pack all 'main'
        game views into the master window (self._mw)

        :param game: an instance of the Sudoku gamelogic class
        :param HEIGHT: customizable height of window
        :param WIDTH: customizable width of window 
        """
        self._root = tk.Tk()
        self._h = HEIGHT
        self._w = WIDTH
        self._mw = tk.Frame(self._root, height=HEIGHT, width=WIDTH, background="lightblue")
        self._mw.pack()

        #Window customizations
        self._root.title("Sudoku")
        self._root.deiconify()

        #Setup and load menu
        self._root.mainloop()


    def load_menu(self):
        self.clear_window()
        menu_frame = tk.Frame(self._mw, ANCHOR=tk.CENTER).pack()
        tk.Button(menu_frame, command=self.init_game).pack()
        tk.Button(menu_frame, command=self._root.destroy).pack()
 

    def init_game(self):
        self._mw.clea


    def clear_window(self):
        for scene in self._mw.winfo_children(): scene.destroy()



def main():
    WINDOW = View()




if __name__ == "__main__":
    main()