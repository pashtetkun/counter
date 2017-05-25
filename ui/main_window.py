#!/usr/bin/python
# -*- coding: utf-8 -*-

from ui.main_tab_panel import MainTabPanel
from ttkthemes import themed_tk as tk
import tkinter.ttk as ttk
import random


class MainWindow:
    def __init__(self, width, height):
        self.root = tk.ThemedTk()
        #self.style = ttk.Style()
        #self.themes = self.style.theme_names()
        #self.theme = random.choice(self.themes)

        self.root.set_theme("vista")
        self.root.title("Инстаграммер (прототип) - %s" % 'vista')
        self.hs = self.root.winfo_screenheight()
        self.ws = self.root.winfo_screenwidth()
        self.root.geometry('%dx%d+%d+%d' % (width, height, (self.ws-width)//2, (self.hs-height)//2))
        self.root.resizable(width=False, height=False)

        self.main_tab_panel = MainTabPanel(self.root)
        self.main_tab_panel.pack()

        self.root.iconbitmap('smoking.ico')
        self.root.mainloop()


if __name__ == "__main__":
    MainWindow(1000, 500);