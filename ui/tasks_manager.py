#!/usr/bin/python
# -*- coding: utf-8 -*-

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

        self.button_add_account = ttk.Button(self, text='Добавить аккаунт')
        self.button_add_account.grid(row=1, column=0, sticky="nesw")
        self.button_del_account = ttk.Button(self, text='Удалить аккаунт')
        self.button_del_account.grid(row=2, column=0, sticky="nesw")

        self.button_add_task = ttk.Button(self, text='Добавить задание')
        self.button_add_task.grid(row=1, column=1, sticky="nesw")
        self.button_del_task = ttk.Button(self, text='Удалить задание')
        self.button_del_task.grid(row=2, column=1, sticky="nesw")

        self.button_start = ttk.Button(self, text='Старт')
        self.button_start.grid(row=1, column=2, sticky="nesw")
        self.button_start_all = ttk.Button(self, text='Старт все')
        self.button_start_all.grid(row=2, column=2, sticky="nesw")

        self.button_pause = ttk.Button(self, text='Пауза')
        self.button_pause.grid(row=1, column=3, sticky="nesw")
        self.button_pause_all = ttk.Button(self, text='Пауза все')
        self.button_pause_all.grid(row=2, column=3, sticky="nesw")

        self.button_stop = ttk.Button(self, text='Стоп')
        self.button_stop.grid(row=1, column=4, sticky="nesw")
        self.button_stop_all = ttk.Button(self, text='Стоп все')
        self.button_stop_all.grid(row=2, column=4, sticky="nesw")

        self.button_license = ttk.Button(self, text='Информация\nо лицензии')
        self.button_license.grid(row=1, column=5, rowspan=2, sticky="ns")

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
    projects_manager = TasksManager(root);
    root.mainloop()