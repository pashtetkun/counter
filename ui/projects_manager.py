#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter.ttk as ttk
from ttkthemes import themed_tk as tk


class TableProjects(ttk.Treeview):
    def __init__(self, parent):
        ttk.Treeview.__init__(self, parent)

        self.columns = ("Проекты", )
        self.configure(show="headings", selectmode="browse", columns=self.columns)
        for col in self.columns:
            self.heading(col, text=col)
            self.column(col, width=100)


class TableAccounts(ttk.Treeview):
    def __init__(self, parent):
        ttk.Treeview.__init__(self, parent)

        self.columns = ("", )
        self.configure(show="", selectmode="browse", columns=self.columns)
        for col in self.columns:
            self.heading(col, text=col)


class ProjectsManager(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack()

        self.table_projects = TableProjects(self)
        self.table_projects.grid(row=0, column=0, rowspan=7, sticky="ewns", padx=5, pady=10)
        self.button_add_project = ttk.Button(self, text='Добавить проект', state="disabled")
        self.button_add_project.grid(row=7, column=0, sticky="nesw")

        self.entry1 = ttk.Entry(self, state="disabled")
        self.entry1.grid(row=0, column=1, sticky="ew", padx=5, pady=10)
        self.table_accounts = TableAccounts(self)
        self.table_accounts.grid(row=1, column=1, rowspan=5, sticky="ew", padx=5, pady=10)
        self.button_add_account = ttk.Button(self, text='Добавить аккаунт', state="disabled")
        self.button_add_account.grid(row=6, column=1, sticky="ew", padx=5, pady=10)

        self.button_delete_project = ttk.Button(self, text='Удалить проект', state="disabled")
        self.button_delete_project.grid(row=7, column=1, sticky="nesw")

        self.label1 = ttk.Label(self, text="Загрузить аккаунты из списка")
        self.label1.grid(row=1, column=2, columnspan=2, sticky="ws")
        self.entry1 = ttk.Entry(self, state="disabled")
        self.entry1.grid(row=2, column=2, columnspan=2, sticky="ew")
        self.button_load = ttk.Button(self, text="Загрузить", state="disabled")
        self.button_load.grid(row=2, column=4)
        self.label2 = ttk.Label(self, text="Выбрать из имеющихся")
        self.label2.grid(row=3, column=2, columnspan=2, sticky="ws")
        self.cmb1 = ttk.Combobox(self, state="disabled")
        self.cmb1.grid(row=4, column=2, columnspan=2, sticky="ew")
        self.button_choose = ttk.Button(self, text="Выбрать", state="disabled")
        self.button_choose.grid(row=4, column=4)

        self.button_save = ttk.Button(self, text="Сохранить", state="disabled")
        self.button_save.grid(row=5, column=3, rowspan=2, columnspan=3, sticky="wens")

        self.rowconfigure(0, minsize=20, weight=1)
        self.rowconfigure(1, minsize=20, weight=1)
        self.rowconfigure(2, minsize=20, weight=1)
        self.rowconfigure(3, minsize=20, weight=1)
        self.rowconfigure(4, minsize=20, weight=1)
        self.rowconfigure(5, minsize=20, weight=1)
        self.rowconfigure(6, minsize=20, weight=1)
        self.rowconfigure(7, minsize=20, weight=1)
        self.columnconfigure(0, minsize=200, weight=1)
        self.columnconfigure(1, minsize=100, weight=1)
        self.columnconfigure(2, minsize=100, weight=1)
        self.columnconfigure(3, minsize=100, weight=1)
        self.columnconfigure(4, minsize=100, weight=1)


if __name__ == "__main__":
    root = tk.ThemedTk()
    print(root.get_themes())  # Returns a list of all themes that can be set
    root.set_theme("vista")
    projects_manager = ProjectsManager(root);
    root.mainloop()