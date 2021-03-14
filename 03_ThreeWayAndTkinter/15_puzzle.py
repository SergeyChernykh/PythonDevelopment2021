#!/usr/bin/env python3
'''
Tkinter 15 puzzle app
'''
import tkinter as tk
import random

class Application(tk.Frame):

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")

        self.NumOfRows = 4
        self.NumOfColumns = 4
        self.FreePuzzle = self.NumOfRows * self.NumOfColumns-1
        self.WinReplacement = [i for i in range(self.NumOfRows*self.NumOfColumns)]

        self.createWidgets()
        self.createNewGame()

    def createWidgets(self):
        '''Create all the widgets'''
        self.L = tk.Label(self, relief = tk.GROOVE)
        self.L.grid(sticky="NEWS")
        for i in range(self.NumOfColumns):
            self.L.columnconfigure(i, weight=1)
        for i in range(self.NumOfRows):
            self.L.rowconfigure(i+1, weight=1)
        self.N = tk.Button(self.L, text="New", command=self.createNewGame)
        self.N.grid(row = 0, column = 0, columnspan = 2)
        self.Q = tk.Button(self.L, text="Quit", command=self.master.quit)
        self.Q.grid(row = 0, column = 2, columnspan = 2)
        self.Puzzles = []
        for i in range(self.NumOfRows * self.NumOfColumns - 1):
            puzzle = tk.Button(self.L)
            self.Puzzles.append(puzzle)

    def showWidgets(self):
        '''Show all the widgets'''
        self.L.grid(sticky="NEWS")
        self.N.grid(row = 0, column = 0, columnspan = 2)
        self.Q.grid(row = 0, column = 2, columnspan = 2)
        for i, puzzle in enumerate(self.Puzzles):
            puzzle["text"] = self.Replacement[i] + 1
            puzzle.grid(row = (i // self.NumOfRows)+1, column = i % self.NumOfColumns, sticky = "NEWS")

    def initNewGame(self):
        '''Create new replacement'''
        self.Replacement = self.WinReplacement[:-1].copy()
        random.shuffle(self.Replacement)
        self.Replacement.append(self.FreePuzzle)

    def createNewGame(self):
        self.initNewGame()
        self.showWidgets()


app = Application(title = "15 puzzle")
app.mainloop()