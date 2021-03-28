#!/usr/bin/env python3
'''
Tkinter simple graphic editor app
'''
import tkinter as tk
import re

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
        self.FigureTypes = ["oval", "rectangle", "arc"]

    def createWidgets(self):
        '''Create all the widgets'''
        self.L = tk.Label(self)
        self.L.grid(sticky="NEWS")
        self.L.columnconfigure(0, weight=1)
        self.L.columnconfigure(1, weight=1)
        self.L.rowconfigure(0, weight=1)
        self.T = tk.Text(self.L)
        self.T.grid(row=0, column=0, sticky="NEWS")
        self.C = tk.Canvas(self.L)
        self.C.grid(row=0, column=1, sticky="NEWS")

        self.BL = tk.Label(self.L)
        self.BL.grid(row=1, columnspan=2, sticky="E")
        self.Q = tk.Button(self.BL, text="Quit", command=self.master.quit)
        self.Q.grid(row=0, column=2)
        self.UT = tk.Button(self.BL, text="Update Text")
        self.UT.grid(row=0, column=1)
        self.UC = tk.Button(self.BL, text="Update Canvas", command = self.updateCanvas)
        self.UC.grid(row=0, column=0)

    def tryCreateFigure(self, opts):
        if len(opts) != 8:
            return {}
        if opts[0] not in self.FigureTypes:
            return {}
        try:
            figure = {}
            figure["type"] = opts[0]
            figure["coords"] = [ float(x) for x in opts[1:5] ]
            figure["options"] = {}
            figure["options"]["width"] = float(opts[5])
            def correctColor(color):
                return re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)
            if not correctColor(opts[6]) or not correctColor(opts[7]):
                return {}
            figure["options"]["outline"] = opts[6]
            figure["options"]["fill"] = opts[7]
            return figure
        except ValueError:
            return {}

    def parseText(self, text):
        lines = text.split("\n")
        self.Figures = []
        for i, line in enumerate(lines):
            figure = self.tryCreateFigure(line.split())
            if figure:
                self.Figures.append(figure)
            else:
                self.T.tag_add("error", f"{i+1}.0", f"{i+1}.end")
        self.T.tag_configure("error", background="red")

    def printFigures(self):
        for figure in self.Figures:
            self.C._create(figure['type'], figure['coords'], figure['options'])


    def updateCanvas(self):
        self.C.delete("all")
        self.T.tag_delete("error")
        self.parseText(self.T.get("1.0", "end-1c"))
        self.printFigures()

app = Application(title="Graphic Editor")
app.mainloop()