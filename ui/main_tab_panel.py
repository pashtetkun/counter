#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from ui import tasks_manager, projects_manager


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

        self.projects_manager = projects_manager.ProjectsManager(self)
        self.add(self.projects_manager,     text='Менеджер проектов')

        self.tasks_manager = tasks_manager.TasksManager(self)
        self.add(self.tasks_manager, text='Менеджер заданий ')

        self.accumulation_manager = ttk.Frame(self)
        self.add(self.accumulation_manager, text=' Сбор аудитории  ', state="disabled")

        self.settings_manager = ttk.Frame(self)
        self.add(self.settings_manager, text='    Настройки    ', state="disabled")

        self.logs_manager = ttk.Frame(self)
        self.add(self.logs_manager, text='    Логи         ', state="disabled")

        self.select(1)


if __name__ == "__main__":
    root = tk.Tk()
    width = 1000
    height = 500
    hs = root.winfo_screenheight()
    ws = root.winfo_screenwidth()
    root.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))
    main_tab_panel = MainTabPanel(root)
    root.mainloop()

