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
        self.Figures = {}
        self.DefaultOptions = {
            "width": 2.0,
            "outline": "#00ff00",
            "fill": "#ff00ff"}

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
        self.C.bind("<ButtonPress-1>", self.moveStart)
        self.C.bind("<B1-Motion>", self.moveMove)

        self.BL = tk.Label(self.L)
        self.BL.grid(row=1, columnspan=2, sticky="E")
        self.Q = tk.Button(self.BL, text="Quit", command=self.master.quit)
        self.Q.grid(row=0, column=2)
        self.UT = tk.Button(
            self.BL,
            text="Update Text",
            command=self.updateText)
        self.UT.grid(row=0, column=1)
        self.UC = tk.Button(
            self.BL,
            text="Update Canvas",
            command=self.updateCanvas)
        self.UC.grid(row=0, column=0)

    def tryCreateFigure(self, opts):
        if len(opts) != 8:
            return {}
        if opts[0] not in self.FigureTypes:
            return {}
        try:
            figure = {}
            figure["type"] = opts[0]
            figure["coords"] = [float(x) for x in opts[1:5]]
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
        figures = []
        for i, line in enumerate(lines):
            figure = self.tryCreateFigure(line.split())
            if figure:
                figures.append(figure)
            else:
                self.T.tag_add("error", f"{i+1}.0", f"{i+1}.end")
        self.T.tag_configure("error", background="red")
        return figures

    def createFigures(self, figures):
        self.Figures = {}
        for figure in figures:
            self.Figures[self.C._create(
                figure['type'], figure['coords'], figure['options'])] = figure

    def updateCanvas(self):
        self.C.delete("all")
        self.T.tag_delete("error")
        self.createFigures(self.parseText(self.T.get("1.0", "end-1c")))

    def moveStart(self, event):
        self.CurrectObject = self.C.find_overlapping(
            event.x, event.y, event.x + 1, event.y + 1)
        self.PrevCoods = [event.x, event.y]
        self.NewFigureFlag = False
        if not self.CurrectObject:
            self.NewFigureFlag = True
            self.CurrectObject = self.C.create_oval(
                event.x, event.y, event.x, event.y, self.DefaultOptions)
            self.Figures[self.CurrectObject] = {
                "type": "oval", "coords": [], "options": self.DefaultOptions}
        else:
            self.CurrectObject = self.CurrectObject[-1]

    def moveMove(self, event):
        if not self.NewFigureFlag:
            self.C.move(
                self.CurrectObject,
                event.x - self.PrevCoods[0],
                event.y - self.PrevCoods[1])
            self.PrevCoods = [event.x, event.y]
        else:
            self.C.coords(
                self.CurrectObject,
                self.PrevCoods[0],
                self.PrevCoods[1],
                event.x,
                event.y)

    def updateText(self):
        self.T.delete("1.0", "end")
        text = ""
        for obj in self.C.find_all():
            self.Figures[obj]['coords'] = self.C.coords(obj)
            text += "\n" + self.Figures[obj]['type']
            for c in self.Figures[obj]['coords']:
                text += " " + str(c)
            text += " " + str(self.Figures[obj]['options']['width'])
            text += " " + str(self.Figures[obj]['options']['outline'])
            text += " " + str(self.Figures[obj]['options']['fill'])
        self.T.insert("1.0", text[1:])


app = Application(title="Graphic Editor")
app.mainloop()
