#!/usr/bin/env python3
'''
Tkinter LabelEdit app
'''
import tkinter as tk

class InputLabel(tk.Label):
    def __init__(self, master=None, **kwards):
        self.text = tk.StringVar()
        super().__init__(master, textvariable = self.text, takefocus=True, highlightthickness=1, anchor="nw",**kwards)
        self.bind("<Button-1>", lambda event: self.focus_set())
        self.bind('<Any-KeyPress>', self.handler)

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
        self.IL.grid(row=0, column=0)
        self.Q = tk.Button(self.L, text="Quit", command=self.master.quit)
        self.Q.grid(row=1, column=0)

app = Application(title="LabelEdit")
app.mainloop()