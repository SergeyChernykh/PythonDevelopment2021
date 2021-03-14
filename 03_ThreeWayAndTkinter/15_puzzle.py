#!/usr/bin/env python3
'''
Tkinter skeleton app
'''
import tkinter as tk

class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()

    def createWidgets(self):
        '''Create all the widgets'''
        self.N = tk.Button(self, text="New", command=self.CreateNewPlacement)
        self.N.grid(row = 0, column = 0, columnspan = 2, sticky="NEWS")
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        self.Q.grid(row = 0, column = 2, columnspan = 2, sticky="NEWS")
        self.puzzles = []
        for i in range(15):
            puzzle = tk.Button(self, text=i+1)
            puzzle.grid(row = (i // 4)+1, column = i % 4, sticky = "NEWS")
            self.puzzles.append(puzzle)

    def CreateNewPlacement(self):
        print("new")
        pass

app = Application(title="15 puzzle")
app.mainloop()