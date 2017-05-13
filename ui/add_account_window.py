# coding=utf-8

import tkinter as tk
import tkinter.ttk as ttk


class AddAccountWindow(tk.Toplevel):
    def __init__(self, width, height, parent):
        tk.Toplevel.__init__(self, height=height, width=width)

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
        self.button_save = ttk.Button(self, text="Сохранить")
        self.button_save.grid(row=2, column=0, columnspan=2)

        self.rowconfigure(0, minsize=20, weight=1)
        self.rowconfigure(1, minsize=20, weight=1)
        self.rowconfigure(2, minsize=20, weight=1)
        self.columnconfigure(0, minsize=100, weight=1)
        self.columnconfigure(1, minsize=100, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    width = 1000
    height = 500
    hs = root.winfo_screenheight()
    ws = root.winfo_screenwidth()
    root.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))
    add_account_window = AddAccountWindow(250, 200, root)
    root.mainloop()