#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.ttk as ttk
from ui import tasksManager


class MainTabPanel(ttk.Notebook):
    def __init__(self, parent):
        self.style = ttk.Style()

        print(self.style.theme_names())

        '''self.style.theme_settings("default", {
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
            "TNotebook.Tab": {"configure": {"padding": [50, 50]}, "minwidth": 200}})
        self.style.theme_use("default")'''
        #self.style.configure('MainTab.TNotebook.Tab', minwidth=200)

        ttk.Notebook.__init__(self, parent)
        self.pack()

        self.projectsManager = ttk.Frame(self)
        self.add(self.projectsManager,     text='Менеджер проектов', state="disabled")

        self.tasksManager = tasksManager.TasksManager(self)
        self.add(self.tasksManager,        text='Менеджер заданий ')

        self.accumulationManager = ttk.Frame(self)
        self.add(self.accumulationManager, text=' Сбор аудитории  ', state="disabled")

        self.settingsManager = ttk.Frame(self)
        self.add(self.settingsManager,     text='    Настройки    ', state="disabled")

        self.logsManager = ttk.Frame(self)
        self.add(self.logsManager,         text='    Логи         ', state="disabled")

        self.select(1)


if __name__ == "__main__":
    root = Tk()
    width = 1000
    height = 500
    hs = root.winfo_screenheight()
    ws = root.winfo_screenwidth()
    root.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))
    mainTabPanel = MainTabPanel(root)
    root.mainloop()

