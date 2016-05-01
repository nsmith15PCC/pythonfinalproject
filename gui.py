from tkinter import *

class GUI(Frame):
    def __init__ (self):
        Frame.__init__(self)
        self.master.title("Autograder")
        self.grid()

        self._filelist = Frame(self)
        self._filelist.grid (row = 0, column = 0)