#!/usr/bin/env python3
'''
Tkinter 15 puzzle app
'''
import tkinter as tk

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
        self.createWidgets()

    def createWidgets(self):
        '''Create all the widgets'''
        self.L = tk.Label(self, relief = tk.GROOVE)
        self.L.grid(sticky="NEWS")
        for i in range(4):
            self.L.columnconfigure(i, weight=1)
            self.L.rowconfigure(i+1, weight=1)
        self.N = tk.Button(self.L, text="New", command=self.CreateNewPlacement)
        self.N.grid(row = 0, column = 0, columnspan = 2)
        self.Q = tk.Button(self.L, text="Quit", command=self.master.quit)
        self.Q.grid(row = 0, column = 2, columnspan = 2)
        self.puzzles = []
        for i in range(15):
            puzzle = tk.Button(self.L, text=i+1)
            puzzle.grid(row = (i // 4)+1, column = i % 4, sticky = "NEWS")
            self.puzzles.append(puzzle)

    def CreateNewPlacement(self):
        print("new")
        pass

app = Application(title="15 puzzle")
app.mainloop()