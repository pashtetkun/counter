#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from ui import spinbox


class TaskMultiFollowingWindow(tk.Toplevel):
    def __init__(self, width, height, parent, callback=None):
        tk.Toplevel.__init__(self, height=height, width=width)

        self.title("Фолловинг по списку")
        self.transient(parent)
        self.grab_set()
        hs = self.winfo_screenheight()
        ws = self.winfo_screenwidth()
        self.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))

        self.header = ttk.Label(self, text='Фолловинг по списку')
        self.header.grid(row=0, column=0, columnspan=4)
        self.label_logins = ttk.Label(self, text="Файл со списком пользователей для фолловинга:")
        self.label_logins.grid(row=1, column=0, sticky="w")
        self.var_logins = tk.StringVar()
        self.entry_logins = ttk.Entry(self, textvariable=self.var_logins)
        self.entry_logins.grid(row=1, column=1)
        self.button_choose = ttk.Button(self, text="Выбрать")
        self.button_choose.grid(row=1, column=2)

        self.label_delay_actions = ttk.Label(self, text='Задержка в секундах между действиями:')
        self.label_delay_actions.grid(row=2, column=0, sticky="w")
        self.label_delay_actions_from = ttk.Label(self, text="от")
        self.label_delay_actions_from.grid(row=2, column=1)
        self.var_delay_actions_from = tk.StringVar()
        self.spinbox_delay_actions_from = spinbox.Spinbox(self, from_=1, to=10, increment=1)
        self.spinbox_delay_actions_from.grid(row=2, column=2)
        self.label_delay_actions_to = ttk.Label(self, text="до")
        self.label_delay_actions_to.grid(row=2, column=3)
        self.var_delay_actions_to = tk.StringVar()
        self.spinbox_delay_actions_to = spinbox.Spinbox(self, from_=1, to=10, increment=1)
        self.spinbox_delay_actions_to.grid(row=2, column=4)

        self.label_followed_count = ttk.Label(self, text="Количество пользователей, которых следует зафолловить:")
        self.label_followed_count.grid(row=3, column=0, sticky="w")
        self.var_followed_count = tk.StringVar()
        self.spinbox_followed_count = spinbox.Spinbox(self, from_=1, to=10, increment=1)
        self.spinbox_followed_count.grid(row=3, column=1)

        self.check_private = ttk.Checkbutton(self, text="не подписываться на приватные страницы")
        self.check_private.grid(row=4, column=0, sticky="w")

        self.check_followed = ttk.Checkbutton(self, text="не подписываться на тех, кто находится в подписчиках")
        self.check_followed.grid(row=5, column=0, sticky="w")

        self.frame_likes = ttk.Frame(self)
        self.frame_likes.grid(row=6, column=0)
        self.frame_pause = ttk.Frame(self)
        self.frame_pause.grid(row=6, column=1)

        self.button_add = ttk.Button(self, text="Добавить задание")
        self.button_add.grid(row=7, column=0, columnspan=4)

        self.rowconfigure(0, minsize=10, weight=1)
        self.rowconfigure(1, minsize=10, weight=1)
        self.rowconfigure(2, minsize=10, weight=1)
        self.rowconfigure(3, minsize=10, weight=1)
        self.rowconfigure(4, minsize=10, weight=1)
        self.rowconfigure(5, minsize=10, weight=1)
        self.rowconfigure(6, minsize=100, weight=1)
        self.rowconfigure(7, minsize=10, weight=1)
        self.columnconfigure(0, minsize=350, weight=1)
        self.columnconfigure(1, minsize=100, weight=1)
        self.columnconfigure(2, minsize=100, weight=1)
        self.columnconfigure(3, minsize=100, weight=1)
        self.columnconfigure(4, minsize=100, weight=1)

        self.callback = callback


if __name__ == "__main__":
    root = tk.Tk()
    width = 1000
    height = 500
    hs = root.winfo_screenheight()
    ws = root.winfo_screenwidth()
    root.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))
    TaskMultiFollowingWindow(800, 300, root)
    root.mainloop()