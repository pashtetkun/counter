#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.ttk as ttk


class ProjectsManager(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack()

        self.left_panel_pack()
        self.right_panel_pack()

    def left_panel_pack(self):
        self.leftPanel = ttk.Frame(self)
        self.leftPanel.pack(side=LEFT)

        self.columns1 = ("Проекты",)
        self.table1 = ttk.Treeview(self.leftPanel, show="headings", selectmode="browse",
                                  columns=self.columns1)
        for col in self.columns1:
            self.table1.heading(col, text=col)

        self.table1.pack()

        self.buttonsFrame1 = ttk.Frame(self.leftPanel)
        self.buttonsFrame1.pack()

        self.bAddProject = ttk.Button(self.buttonsFrame1, text='Добавить проект')
        self.bAddProject.grid(row=0, column=0, sticky="nesw")
        self.bDelProject = ttk.Button(self.buttonsFrame1, text='Удалить проект')
        self.bDelProject.grid(row=1, column=0, sticky="nesw")

        self.buttonsFrame1.rowconfigure(0, minsize=20)
        self.buttonsFrame1.columnconfigure(0, minsize=100)
        self.buttonsFrame1.rowconfigure(1, minsize=20)


    def right_panel_pack(self):
        self.rightPanel = ttk.Frame(self)
        self.rightPanel.pack(expand=YES, fill=BOTH, anchor="w")

        self.columns = ("Логин", "Задание", "Статус", "Подписки", "Подписчики", "Прогресс")
        self.table = ttk.Treeview(self.rightPanel, show="headings", selectmode="browse",
                                  columns=self.columns)
        for col in self.columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=100)

        self.table.pack()

        self.buttons_frame_pack()

    def buttons_frame_pack(self):
        self.buttonsFrame = ttk.Frame(self.rightPanel)
        self.buttonsFrame.pack(side=LEFT)

        self.bAddAccount = ttk.Button(self.buttonsFrame, text='Добавить аккаунт', width=20)
        self.bAddAccount.grid(row=0, column=0,  sticky="nesw")
        self.bDelAccount = ttk.Button(self.buttonsFrame, text='Удалить аккаунт')
        self.bDelAccount.grid(row=1, column=0, sticky="nesw")

        self.bAddTask = ttk.Button(self.buttonsFrame, text='Добавить задание')
        self.bAddTask.grid(row=0, column=1, sticky="nesw")
        self.bDelTask = ttk.Button(self.buttonsFrame, text='Удалить задание')
        self.bDelTask.grid(row=1, column=1, sticky="nesw")

        self.bStart = ttk.Button(self.buttonsFrame, text='Старт')
        self.bStart.grid(row=0, column=2, sticky="nesw")
        self.bStartAll = ttk.Button(self.buttonsFrame, text='Старт все')
        self.bStartAll.grid(row=1, column=2, sticky="nesw")

        self.bPause = ttk.Button(self.buttonsFrame, text='Пауза')
        self.bPause.grid(row=0, column=3, sticky="nesw")
        self.bPauseAll = ttk.Button(self.buttonsFrame, text='Пауза все')
        self.bPauseAll.grid(row=1, column=3, sticky="nesw")

        self.bStop = ttk.Button(self.buttonsFrame, text='Стоп')
        self.bStop.grid(row=0, column=4, sticky="nesw")
        self.bStopAll = ttk.Button(self.buttonsFrame, text='Стоп все')
        self.bStopAll.grid(row=1, column=4, sticky="nesw")

        self.bLicense = ttk.Button(self.buttonsFrame, text='Информация о лицензии')
        self.bLicense.grid(row=0, column=5, rowspan=2, sticky="nesw")

        self.buttonsFrame.rowconfigure(0, minsize=20)
        self.buttonsFrame.columnconfigure(0, minsize=100)
        self.buttonsFrame.rowconfigure(1, minsize=20)
        self.buttonsFrame.columnconfigure(1, minsize=100)
        self.buttonsFrame.columnconfigure(2, minsize=100)
        self.buttonsFrame.columnconfigure(3, minsize=100)
        self.buttonsFrame.columnconfigure(4, minsize=100)
        self.buttonsFrame.columnconfigure(5, minsize=100)





if __name__ == "__main__":
    root = Tk()
    projectsManager = ProjectsManager(root);
    root.mainloop()