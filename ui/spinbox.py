#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk


class Spinbox(ttk.Widget):
    def __init__(self, master, **kw):
        ttk.Widget.__init__(self, master, 'ttk::spinbox', kw)

if __name__ == '__main__':
    root = tk.Tk()
    opts = { 'from': 0, 'to': 10, 'increment': 1 }
    sp1 = tk.Spinbox(root, **opts)
    sp1.place(x=5, y=5)
    sp2 = Spinbox(root, **opts)
    sp2.place(x=5, y=30)
    root.mainloop()