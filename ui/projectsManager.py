#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.ttk as ttk


class ProjectsManager(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack()

        self.columns = ("project", "login", "task", "status", "followed", "followers", "progress")
        self.table = ttk.Treeview(self, show ="headings",selectmode="browse",
                               columns=self.columns)
        for col in self.columns:
            self.table.heading(col, text=col)

        self.table.pack()

        self.buttonsFrame = ttk.Frame(self)
        self.buttonsFrame.pack()
        self.bAddAccount = ttk.Button(self.buttonsFrame, text='Добавить аккаунт')
        self.bAddAccount.pack()



if __name__ == "__main__":
    root = Tk()
    projectsManager = ProjectsManager(root);
    root.mainloop()