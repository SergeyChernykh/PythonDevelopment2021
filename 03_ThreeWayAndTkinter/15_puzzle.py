#!/usr/bin/env python3
'''
Tkinter 15 puzzle app
'''
import tkinter as tk
from tkinter import messagebox
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

        self.createWidgets()
        self.createNewGame()

    def createWidgets(self):
        '''Create all the widgets'''
        self.L = tk.Label(self)
        self.L.grid(sticky="NEWS")
        for i in range(self.NumOfColumns):
            self.L.columnconfigure(i, weight=1)
        for i in range(self.NumOfRows):
            self.L.rowconfigure(i + 1, weight=1)
        self.N = tk.Button(self.L, text="New", command=self.createNewGame)
        self.N.grid(row=0, column=0, columnspan=2)
        self.Q = tk.Button(self.L, text="Quit", command=self.master.quit)
        self.Q.grid(row=0, column=2, columnspan=2)
        self.Puzzles = []
        for i in range(self.NumOfRows * self.NumOfColumns):
            puzzle = tk.Button(self.L, height=1, width=2)

            def handler(p=puzzle):
                self.movePuzzle(p)
            puzzle['command'] = handler
            self.Puzzles.append(puzzle)

    def showWidgets(self):
        '''Show all the widgets'''
        self.L.grid(sticky="NEWS")
        self.N.grid(row=0, column=0, columnspan=2)
        self.Q.grid(row=0, column=2, columnspan=2)
        for i in self.Replacement:
            puzzle = self.Puzzles[i]
            row = (i // self.NumOfRows)
            column = i % self.NumOfColumns
            if (row == self.FreePuzzleRow and column == self.FreePuzzleColumn):
                puzzle.grid_remove()
            else:
                puzzle["text"] = self.Replacement[i] + 1
                puzzle.grid(row=row + 1, column=column, sticky="NEWS")

    def initNewGame(self):
        self.FreePuzzleRow = self.NumOfRows - 1
        self.FreePuzzleColumn = self.NumOfColumns - 1
        '''Create new replacement'''
        self.Replacement = [
            i for i in range(
                self.NumOfRows *
                self.NumOfColumns -
                1)]
        random.shuffle(self.Replacement)
        self.Replacement.append(self.NumOfRows * self.NumOfColumns - 1)

    def createNewGame(self):
        self.initNewGame()
        self.showWidgets()

    def isSorted(self, replacement):
        for i, e in enumerate(replacement[1:]):
            if e <= replacement[i]:
                return False
        return True

    def movePuzzle(self, puzzle):
        row = puzzle.grid_info()['row'] - 1
        column = puzzle.grid_info()['column']
        if row == self.FreePuzzleRow and column == self.FreePuzzleColumn:
            return

        if (abs(row - self.FreePuzzleRow) == 1 and column == self.FreePuzzleColumn) or (
                abs(column - self.FreePuzzleColumn) and row == self.FreePuzzleRow):
            puzzle_shift = row * self.NumOfRows + column
            free_puzzle_shift = self.FreePuzzleRow * self.NumOfRows + self.FreePuzzleColumn

            # Move puzzle to empty space
            self.Replacement[puzzle_shift], self.Replacement[free_puzzle_shift] = self.Replacement[free_puzzle_shift], self.Replacement[puzzle_shift]
            self.FreePuzzleRow, self.FreePuzzleColumn = row, column
            self.showWidgets()
            if (self.isSorted(self.Replacement)):
                messagebox.showinfo("", "You win :-)")
                self.createNewGame()


app = Application(title="15 puzzle")
app.mainloop()
