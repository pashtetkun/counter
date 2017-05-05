# coding=utf-8

from tkinter import *
import tkinter.ttk as ttk
import dbmanager.dbmanager as dbmanager


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

        self.root.mainloop()

    def action(self, event):
        #self.lblVar.set("Hello world!!!")
        dbmanager.create_tables()
        dbmanager.create_account("user", "123456")


if __name__ == "__main__":
    mainWindow = MainWindow();