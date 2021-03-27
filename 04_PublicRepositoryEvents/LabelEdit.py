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
        super().__init__(
            master,
            font=self.font,
            textvariable=self.text,
            takefocus=True,
            highlightthickness=1,
            anchor="nw",
            **kwards)
        self.Cursor = tk.Frame(self, width=2, bd=2, relief=tk.RIDGE)
        self.bind("<Button-1>", self.mouse_click_handler)
        self.bind('<Any-KeyPress>', self.key_press_handler)

    def get_cursor_pos(self, x):
        for i in range(len(self.text.get()) + 1):
            if self.font.measure(self.text.get()[:i]) > x:
                return i - 1
        return len(self.text.get())

    def move_cursor(self, i):
        self.Cursor.place(
            relheight=1,
            x=self.font.measure(self.text.get()[:i]))

    def mouse_click_handler(self, event):
        self.focus_set()
        self.move_cursor(self.get_cursor_pos(event.x))

    def key_press_handler(self, event):
        print(event)
        i = self.get_cursor_pos(int(self.Cursor.place_info()['x']))
        if event.keysym == "BackSpace":
            self.text.set(self.text.get()[:i - 1] + self.text.get()[i:])
            self.move_cursor(i - 1)
        elif event.keysym == "Left":
            self.move_cursor(i - 1)
        elif event.keysym == "Right":
            self.move_cursor(i + 1)
        elif event.keysym == "Home":
            self.move_cursor(0)
        elif event.keysym == "End":
            self.move_cursor(len(self.text.get()))
        elif event.keysym == "Up" or event.keysym == "Down" or event.keysym == "Next" or event.keysym == "Prior":
            pass
        elif event.char.isprintable():
            text = self.text.get()
            self.text.set(text[:i] + event.char + text[i:])
            self.move_cursor(i + 1)


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
