#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import themed_tk as thk
import os


class LicenseWindow(tk.Toplevel):
    def __init__(self, width, height, callback=None):
        tk.Toplevel.__init__(self, height=height, width=width)

        self.title("")
        self.transient(self.master)
        self.grab_set()
        self.geometry('%dx%d+%d+%d'
                      % (width, height, (self.winfo_screenwidth() - width) // 2, (self.winfo_screenheight() - height) // 2))
        #self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.frame = ttk.Frame(self)
        self.frame.pack()
        #image = tk.PhotoImage(file=os.path.join(os.getcwd(), '../Smoking.gif'))
        image = tk.PhotoImage(file=os.path.join(os.getcwd(), 'Smoking.gif'))
        self.label1 = ttk.Label(self.frame, image=image, compound="image")
        self.label1.image = image
        self.label1.pack(side=tk.LEFT)
        self.label2 = ttk.Label(self.frame, text="бла-бла-бла\nбла-бла-бла\n"*6)
        self.label2.pack(side=tk.LEFT, anchor="n")


if __name__ == "__main__":
    root = thk.ThemedTk()
    root.set_theme("vista")
    width = 1000
    height = 500
    hs = root.winfo_screenheight()
    ws = root.winfo_screenwidth()
    root.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))
    add_account_window = LicenseWindow(400, 400)
    root.mainloop()