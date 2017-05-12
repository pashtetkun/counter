#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import themed_tk as tk


class TasksManager(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack()

        self.table1_columns = ("Проекты",)
        self.table1 = ttk.Treeview(self, show="headings", selectmode="browse",
                                   columns=self.table1_columns)
        for col in self.table1_columns:
            self.table1.heading(col, text=col)

        self.table1.grid(row=0, column=0)

        self.table2_columns = ("Логин", "Задание", "Статус", "Подписки", "Подписчики", "Прогресс")
        self.table2 = ttk.Treeview(self, show="headings", selectmode="browse",
                                  columns=self.table2_columns)
        for col in self.table2_columns:
            self.table2.heading(col, text=col)
            self.table2.column(col, width=150)

        self.table2.grid(row=0, column=1, columnspan=5)

        self.bAddAccount = ttk.Button(self, text='Добавить аккаунт')
        self.bAddAccount.grid(row=1, column=0, sticky="nesw")
        self.bDelAccount = ttk.Button(self, text='Удалить аккаунт')
        self.bDelAccount.grid(row=2, column=0, sticky="nesw")

        self.bAddTask = ttk.Button(self, text='Добавить задание')
        self.bAddTask.grid(row=1, column=1, sticky="nesw")
        self.bDelTask = ttk.Button(self, text='Удалить задание')
        self.bDelTask.grid(row=2, column=1, sticky="nesw")

        self.bStart = ttk.Button(self, text='Старт')
        self.bStart.grid(row=1, column=2, sticky="nesw")
        self.bStartAll = ttk.Button(self, text='Старт все')
        self.bStartAll.grid(row=2, column=2, sticky="nesw")

        self.bPause = ttk.Button(self, text='Пауза')
        self.bPause.grid(row=1, column=3, sticky="nesw")
        self.bPauseAll = ttk.Button(self, text='Пауза все')
        self.bPauseAll.grid(row=2, column=3, sticky="nesw")

        self.bStop = ttk.Button(self, text='Стоп')
        self.bStop.grid(row=1, column=4, sticky="nesw")
        self.bStopAll = ttk.Button(self, text='Стоп все')
        self.bStopAll.grid(row=2, column=4, sticky="nesw")

        self.bLicense = ttk.Button(self, text='Информация\nо лицензии')
        self.bLicense.grid(row=1, column=5, rowspan=2, sticky="ns")

        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, minsize=20, weight=1)
        self.rowconfigure(2, minsize=20, weight=1)
        self.columnconfigure(0, minsize=200, weight=1)
        self.columnconfigure(1, minsize=100, weight=1)
        self.columnconfigure(2, minsize=100, weight=1)
        self.columnconfigure(3, minsize=100, weight=1)
        self.columnconfigure(4, minsize=100, weight=1)
        self.columnconfigure(5, minsize=100, weight=1)


if __name__ == "__main__":
    root = tk.ThemedTk()
    print(root.get_themes())  # Returns a list of all themes that can be set
    root.set_theme("radiance")
    projectsManager = TasksManager(root);
    root.mainloop()