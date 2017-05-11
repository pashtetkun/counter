#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import themed_tk as tk


class ProjectsManager(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack()

        self.table_projects = self.table_left_create()
        self.table_tasks = self.table_right_create()
        self.buttons_frame_left = self.buttons_frame_left_create()
        self.buttons_frame_right = self.buttons_frame_right_create()

        self.table_projects.grid(row=0, column=0, sticky="nesw")
        self.table_tasks.grid(row=0, column=1, sticky="nesw")
        self.buttons_frame_left.grid(row=1, column=0, sticky="nesw")
        self.buttons_frame_right.grid(row=1, column=1, sticky="nesw")

        self.rowconfigure(0, minsize=200)
        self.columnconfigure(0, minsize=100)
        self.rowconfigure(1, minsize=60)
        self.columnconfigure(1, minsize=900)

    def table_left_create(self):
        table_left = ttk.Frame(self)

        self.columns1 = ("Проекты",)
        self.table1 = ttk.Treeview(table_left, show="headings", selectmode="browse",
                                   columns=self.columns1)
        for col in self.columns1:
            self.table1.heading(col, text=col)

        self.table1.pack()
        return table_left

    def table_right_create(self):
        table_right = ttk.Frame(self)

        self.columns = ("Логин", "Задание", "Статус", "Подписки", "Подписчики", "Прогресс")
        self.table = ttk.Treeview(table_right, show="headings", selectmode="browse",
                                  columns=self.columns)
        for col in self.columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=150)

        self.table.pack()
        return table_right

    def buttons_frame_left_create(self):
        buttonsFrame1 = ttk.Frame(self)

        self.bAddProject = ttk.Button(buttonsFrame1, text='Добавить проект')
        self.bAddProject.grid(row=0, column=0, sticky="nesw")
        self.bDelProject = ttk.Button(buttonsFrame1, text='Удалить проект')
        self.bDelProject.grid(row=1, column=0, sticky="nesw")

        buttonsFrame1.rowconfigure(0, minsize=20)
        buttonsFrame1.columnconfigure(0, minsize=100)
        buttonsFrame1.rowconfigure(1, minsize=20)

        return buttonsFrame1

    def buttons_frame_right_create(self):
        buttonsFrame = ttk.Frame(self)

        self.bAddAccount = ttk.Button(buttonsFrame, text='Добавить аккаунт', width=20)
        self.bAddAccount.grid(row=0, column=0, sticky="nesw")
        self.bDelAccount = ttk.Button(buttonsFrame, text='Удалить аккаунт')
        self.bDelAccount.grid(row=1, column=0, sticky="nesw")

        self.bAddTask = ttk.Button(buttonsFrame, text='Добавить задание')
        self.bAddTask.grid(row=0, column=1, sticky="nesw")
        self.bDelTask = ttk.Button(buttonsFrame, text='Удалить задание')
        self.bDelTask.grid(row=1, column=1, sticky="nesw")

        self.bStart = ttk.Button(buttonsFrame, text='Старт')
        self.bStart.grid(row=0, column=2, sticky="nesw")
        self.bStartAll = ttk.Button(buttonsFrame, text='Старт все')
        self.bStartAll.grid(row=1, column=2, sticky="nesw")

        self.bPause = ttk.Button(buttonsFrame, text='Пауза')
        self.bPause.grid(row=0, column=3, sticky="nesw")
        self.bPauseAll = ttk.Button(buttonsFrame, text='Пауза все')
        self.bPauseAll.grid(row=1, column=3, sticky="nesw")

        self.bStop = ttk.Button(buttonsFrame, text='Стоп')
        self.bStop.grid(row=0, column=4, sticky="nesw")
        self.bStopAll = ttk.Button(buttonsFrame, text='Стоп все')
        self.bStopAll.grid(row=1, column=4, sticky="nesw")

        self.bLicense = ttk.Button(buttonsFrame, text='Информация\nо лицензии')
        self.bLicense.grid(row=0, column=5, rowspan=2, sticky="nesw")

        buttonsFrame.rowconfigure(0, minsize=20)
        buttonsFrame.columnconfigure(0, minsize=100)
        buttonsFrame.rowconfigure(1, minsize=20)
        buttonsFrame.columnconfigure(1, minsize=100)
        buttonsFrame.columnconfigure(2, minsize=100)
        buttonsFrame.columnconfigure(3, minsize=100)
        buttonsFrame.columnconfigure(4, minsize=100)
        buttonsFrame.columnconfigure(5, minsize=100)

        return buttonsFrame


if __name__ == "__main__":
    root = tk.ThemedTk()
    print(root.get_themes())  # Returns a list of all themes that can be set
    root.set_theme("radiance")
    projectsManager = ProjectsManager(root);
    root.mainloop()