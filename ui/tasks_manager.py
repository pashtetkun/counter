#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter.ttk as ttk
from ttkthemes import themed_tk as tk
from ui import add_account_window
from dbmanager import dbmanager


class TableTasks(ttk.Treeview):
    def __init__(self, parent):
        ttk.Treeview.__init__(self, parent)

        self.columns = ("Логин", "Задание", "Статус", "Подписки", "Подписчики", "Прогресс")
        self.configure(show="headings", selectmode="browse", columns=self.columns)
        for col in self.columns:
            self.heading(col, text=col)
            self.column(col, width=150)

    '''def add_tasks_info(self, tasks_info):
        for task_info in tasks_info:
            self.insert('', 'end',
                        values=(task_info["login"], '', '', '', '', ''))'''

    def refresh(self):
        self.delete()
        accounts = dbmanager.get_all_accounts()
        for account in accounts:
            self.insert('', 'end',
                        values=(account.login, '', '', '', '', ''))


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

        '''self.table2_columns = ("Логин", "Задание", "Статус", "Подписки", "Подписчики", "Прогресс")
        self.table2 = ttk.Treeview(self, show="headings", selectmode="browse",
                                  columns=self.table2_columns)
        for col in self.table2_columns:
            self.table2.heading(col, text=col)
            self.table2.column(col, width=150)'''
        self.table_tasks = TableTasks(self)

        self.table_tasks.grid(row=0, column=1, columnspan=5)

        self.button_add_account = ttk.Button(self, text='Добавить аккаунт',
                                             command=self.open_add_account_window)
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

        self.table_tasks.refresh()

    def add_account_callback(self, login, password):
        if dbmanager.create_account(login, password):
            self.table_tasks.refresh()
        #self.table_tasks.add_tasks_info([{"login": login}])
        #accounts = dbmanager.get_all_accounts()



    def open_add_account_window(self):
        form = add_account_window.AddAccountWindow(250, 200, self.winfo_toplevel(),
                                                   self.add_account_callback)


if __name__ == "__main__":
    root = tk.ThemedTk()
    print(root.get_themes())  # Returns a list of all themes that can be set
    root.set_theme("radiance")
    dbmanager.initialize()
    projects_manager = TasksManager(root);
    root.mainloop()