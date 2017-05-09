# coding=utf-8

from tkinter import *
import tkinter.ttk as ttk
import dbmanager.dbmanager as dbmanager
from instagram_api import auth_provider


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('640x480+400+90')
        self.but = ttk.Button(self.root, text='Жми')
        self.but.bind("<Button-1>", self.action)
        self.but.pack()

        self.lblVar = StringVar()
        self.lbl = ttk.Label(self.root, textvariable=self.lblVar)
        self.lbl.pack()

        self.but2 = ttk.Button(self.root, text='Жми2')
        self.but2.bind("<Button-1>", self.action2)
        self.but2.pack()

        self.lblVar2 = StringVar()
        self.lbl2 = ttk.Label(self.root, textvariable=self.lblVar2)
        self.lbl2.pack()

        self.root.mainloop()

    def action(self, event):
        #self.lblVar.set("Hello world!!!")
        dbmanager.create_tables()
        dbmanager.create_account("user", "123456")


    def action2(self, event):
        result = auth_provider.doLogin("ptsibizov", "animes123")
        self.lblVar2.set(result)


if __name__ == "__main__":
    mainWindow = MainWindow();