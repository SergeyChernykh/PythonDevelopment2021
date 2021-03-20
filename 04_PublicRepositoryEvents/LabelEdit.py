#!/usr/bin/env python3
'''
Tkinter LabelEdit app
'''
import tkinter as tk
from tkinter import font

class InputLabel(tk.Label):
    def __init__(self, master=None, **kwards):
        self.text = tk.StringVar()
        self.font = font.Font(family="Consolas", size=10, weight="normal")
        super().__init__(master, font=self.font, textvariable = self.text, takefocus=True, highlightthickness=1, anchor="nw",**kwards)
        self.Cursor = tk.Frame(self, width=2, bd = 2, relief=tk.RIDGE)
        self.bind("<Button-1>", self.mouse_click_handler)
        self.bind('<Any-KeyPress>', self.handler)

    def mouse_click_handler(self, event):
        print(event)
        self.focus_set()
        self.Cursor.place(relheight = 1, x = event.x)

    def handler(self, event):
        print(event)
        if event.char.isprintable():
            self.text.set(self.text.get() + event.char)

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
        self.L = tk.Label(self)
        self.L.grid(sticky="NEWS")
        self.IL = InputLabel(self.L)
        self.IL.grid(row=0, column=0, sticky="NEWS")
        self.Q = tk.Button(self.L, text="Quit", command=self.master.quit)
        self.Q.grid(row=1, column=0)

app = Application(title="LabelEdit")
app.mainloop()