# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.ttk as ttk


def action(event):
    lblVar.set("Hello world!!!")


if __name__ == "__main__":
    root = Tk()
    root.geometry('640x480+400+90')
    but = ttk.Button(root, text='Жми')
    but.bind("<Button-1>", action)
    but.pack()

    lblVar = StringVar()
    lbl = ttk.Label(root, textvariable=lblVar)
    lbl.pack()

    root.mainloop()