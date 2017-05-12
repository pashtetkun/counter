# coding=utf-8

from tkinter import *
import tkinter.ttk as ttk
import dbmanager.dbmanager as dbmanager
from instagram_api import auth_provider
from ui.mainTabPanel import MainTabPanel
from ttkthemes import themed_tk as tk


class AddAccountWindow(Toplevel):
    def __init__(self, width, height, parent):
        Toplevel.__init__(self, height=height, width=width)

        self.title("Добавить аккаунт")
        self.transient(parent)
        hs = self.winfo_screenheight()
        ws = self.winfo_screenwidth()
        self.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))

        self.label_login = ttk.Label(self, text='Логин')
        self.label_login.grid(row=0, column=0)
        self.entry_login = ttk.Entry(self)
        self.entry_login.grid(row=0, column=1)
        self.label_password = ttk.Label(self, text='Пароль')
        self.label_password.grid(row=1, column=0)
        self.entry_password = ttk.Entry(self)
        self.entry_password.grid(row=1, column=1)
        self.buttonSave = ttk.Button(self, text="Сохранить")
        self.buttonSave.grid(row=2, column=0, columnspan=2)

        self.rowconfigure(0, minsize=20, weight=1)
        self.rowconfigure(1, minsize=20, weight=1)
        self.rowconfigure(2, minsize=20, weight=1)
        self.columnconfigure(0, minsize=100, weight=1)
        self.columnconfigure(1, minsize=100, weight=1)


if __name__ == "__main__":
    root = Tk()
    width = 1000
    height = 500
    hs = root.winfo_screenheight()
    ws = root.winfo_screenwidth()
    root.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))
    addAccountWindow = AddAccountWindow(250, 200, root)
    root.mainloop()