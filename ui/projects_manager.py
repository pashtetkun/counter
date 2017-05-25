#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter.ttk as ttk
from ttkthemes import themed_tk as thk
import tkinter as tk
import tkinter.messagebox as tmb
from ui import add_account_window, table_projects
import dbmanager as db

'''
class TableProjects(ttk.Treeview):
    def __init__(self, parent):
        ttk.Treeview.__init__(self, parent)

        self.columns = ("Проекты", )
        self.configure(show="headings", selectmode="browse", columns=self.columns)
        for col in self.columns:
            self.heading(col, text=col)
            self.column(col, width=100)
        self.projects = []
        self.current_project = None

    def clear(self):
        for row in self.get_children():
            self.delete(row)

    def refresh(self, selected=None):
        self.clear()
        projects = db.get_all_projects()
        for project in projects:
            self.insert('', 'end', iid=project.name,
                        values=(project.name, ))
        self.projects = projects
        if selected:
            self.selection_set(selected)
            self.set_current_project(selected)
        else:
            self.current_project = None

    def set_current_project(self, name):
        self.current_project = next((x for x in self.projects if x.name == name), None)
        return self.current_project
'''


class TableAccounts(ttk.Treeview):
    def __init__(self, parent):
        ttk.Treeview.__init__(self, parent)

        self.columns = ("", )
        self.configure(show="", selectmode="browse", columns=self.columns)
        for col in self.columns:
            self.heading(col, text=col)
        self.accounts = []
        self.current_account = None
        self.deleted_accounts = []

    def clear(self):
        for row in self.get_children():
            self.delete(row)

    def initialize(self, project_id):
        self.accounts = db.get_accounts_for_project(project_id)
        self.refresh()

    def refresh(self, selected=None):
        self.clear()
        for account in self.accounts:
            self.insert('', 'end', iid=account.login,
                        values=(account.login, ))
        if selected:
            self.selection_set(selected)
            self.set_current_account(selected)
        else:
            self.current_account = None

    def add_account(self, account):
        if not next((x for x in self.accounts if x.login == account.login), None):
            self.accounts.append(account)
            self.accounts.sort(key=lambda x: x.login)
            self.refresh(account.login)

    def delete_account(self, account):
        if account.id:
            self.deleted_accounts.append(account)
        self.accounts.remove(account)
        self.refresh()

    def set_current_account(self, login):
        self.current_account = next((x for x in self.accounts if x.login == login), None)
        return self.current_account


class ProjectsManager(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack()

        #self.table_projects = TableProjects(self)
        self.table_projects = table_projects.TableProjects(self)
        self.table_projects.grid(row=0, column=0, rowspan=8, sticky="ewns", padx=5, pady=10)
        self.table_projects.bind('<<TreeviewSelect>>', self.select_project_handler)
        self.button_add_project = ttk.Button(self, text='Добавить проект', command=self.add_project_click)
        self.button_add_project.grid(row=8, column=0, sticky="nesw")

        self.var_name = tk.StringVar()
        self.var_name.trace('w', self.trace_change_name)
        self.entry0 = ttk.Entry(self, textvariable=self.var_name, state="disabled")
        self.entry0.grid(row=0, column=1, sticky="ew", padx=5, pady=10)
        self.table_accounts = TableAccounts(self)
        self.table_accounts.grid(row=1, column=1, rowspan=5, sticky="ew", padx=5, pady=10)
        self.table_accounts.bind('<<TreeviewSelect>>', self.select_account_handler)
        self.button_add_account = ttk.Button(self, text='Добавить аккаунт', state='disabled',
                                             command=self.open_account_window)
        self.button_add_account.grid(row=6, column=1, sticky="ew", padx=5, pady=10)
        self.button_delete_account = ttk.Button(self, text='Удалить аккаунт',
                                                command=self.delete_account_click, state="disabled")
        self.button_delete_account.grid(row=7, column=1, sticky="ew", padx=5, pady=10)

        self.button_delete_project = ttk.Button(self, text='Удалить проект',
                                                command=self.delete_project_click, state="disabled")
        self.button_delete_project.grid(row=8, column=1, sticky="nesw")

        self.var_message = tk.StringVar()
        self.label0 = ttk.Label(self, textvariable=self.var_message)
        self.label0.grid(row=0, column=2, columnspan = 3, sticky='ws')
        self.label1 = ttk.Label(self, text="Загрузить аккаунты из списка")
        self.label1.grid(row=1, column=2, columnspan=2, sticky="ws")
        self.var_path = tk.StringVar()
        self.entry1 = ttk.Entry(self, textvariable=self.var_path, state="disabled")
        self.entry1.grid(row=2, column=2, columnspan=2, sticky="ew")
        self.button_load = ttk.Button(self, text="Загрузить", state="disabled")
        self.button_load.grid(row=2, column=4)
        self.label2 = ttk.Label(self, text="Выбрать из имеющихся")
        self.label2.grid(row=3, column=2, columnspan=2, sticky="ws")
        self.cmb1 = ttk.Combobox(self, state="disabled")
        self.cmb1.grid(row=4, column=2, columnspan=2, sticky="ew")
        self.button_choose = ttk.Button(self, text="Выбрать", state="disabled")
        self.button_choose.grid(row=4, column=4)

        self.button_save = ttk.Button(self, text="Сохранить", state='disabled', command=self.save_click)
        self.button_save.grid(row=6, column=3, rowspan=2, columnspan=3, sticky="ewns")

        self.rowconfigure(0, minsize=20, weight=1)
        self.rowconfigure(1, minsize=20, weight=1)
        self.rowconfigure(2, minsize=20, weight=1)
        self.rowconfigure(3, minsize=20, weight=1)
        self.rowconfigure(4, minsize=20, weight=1)
        self.rowconfigure(5, minsize=20, weight=1)
        self.rowconfigure(6, minsize=20, weight=1)
        self.rowconfigure(7, minsize=20, weight=1)
        self.rowconfigure(8, minsize=20, weight=1)
        self.columnconfigure(0, minsize=200, weight=1)
        self.columnconfigure(1, minsize=100, weight=1)
        self.columnconfigure(2, minsize=100, weight=1)
        self.columnconfigure(3, minsize=100, weight=1)
        self.columnconfigure(4, minsize=100, weight=1)

        self.table_projects.refresh()

        if not self.table_projects.projects:
            self.button_delete_project.configure(state='disabled')
        else:
            self.button_delete_project.configure(state='active')

        self.is_new = False

    def add_account_callback(self, account):
        #account = kwargs["account"]
        #password = kwargs["password"]
        if account:
            #db.create_account(login, password, '0', 0, 0)
            self.table_accounts.add_account(account)

    def open_account_window(self):
        add_account_window.AddAccountWindow(200, 250, self.add_account_callback)

    def add_project_click(self):

        self.clear_values()
        self.entry0.configure(state='active')
        self.entry1.configure(state='active')
        self.button_add_account.configure(state='active')
        self.button_load.configure(state='active')
        self.cmb1.configure(state='active')
        self.button_choose.configure(state='active')
        self.button_save.configure(state='disabled')

        if self.table_projects.current_project:
            self.table_projects.selection_remove(self.table_projects.current_project.name)

        self.is_new = True

    def clear_values(self):
        self.var_name.set("")
        self.var_path.set("")
        self.table_accounts.clear()

    def show_values(self, project_name):
        #self.var_name.set(project_name)
        pass

    def save_click(self):
        if not self.check_name():
            self.var_message.set('need unique name')
            return
        name = self.var_name.get()
        project = None
        if self.is_new:
            project = db.create_project(name)
        else:
            project = self.table_projects.current_project
            project.name = self.var_name.get()
            db.update_project(project)

        accounts = self.table_accounts.accounts
        for account in accounts:
            if not account.project:
                account.project = project
            db.create_account(account)

        deleted_accounts = self.table_accounts.deleted_accounts
        for account in deleted_accounts:
            db.delete_account(account.login)

        self.table_projects.refresh(name)

    def check_name(self):
        name = self.var_name.get()
        if self.is_new:
            if next((x for x in self.table_projects.projects if x.name == name), None):
                return False
        else:
            id = self.table_projects.current_project.id
            if next((x for x in self.table_projects.projects if x.name == name and x.id != id), None):
                return False
        return True

    def select_account_handler(self, e):
        sel = e.widget.selection()
        if sel:
            login = sel[0]
            self.select_account(login)

    def select_account(self, login):
        self.button_delete_account.configure(state='active')
        self.table_accounts.set_current_account(login)

    def select_project_handler(self, e):
        sel = e.widget.selection()
        if sel:
            name = sel[0]
            self.select_project(name)

    def select_project(self, name):
        self.is_new = False
        self.var_name.set(name)
        self.entry0.configure(state='active')
        self.entry1.configure(state='active')
        self.button_choose.configure(state='active')
        self.button_load.configure(state='active')
        self.cmb1.configure(state='active')
        self.button_add_account.configure(state='active')
        self.button_delete_project.configure(state='active')
        current_project = self.table_projects.set_current_project(name)
        self.table_accounts.initialize(current_project.id)
        if not self.table_accounts.accounts:
            self.button_delete_account.configure(state='disabled')
        else:
            self.button_delete_account.configure(state='active')

    def delete_project_click(self):
        project = self.table_projects.current_project
        if tmb.askquestion(title="", message="Удалить проект '%s'?" % project.name) == 'yes':
            prev_name = self.table_projects.prev(project.name)
            next_name = self.table_projects.next(project.name)
            db.delete_project(project.name)
            name = prev_name if prev_name else next_name
            self.table_projects.refresh(name)
            if self.table_projects.projects:
                self.button_delete_project.configure(state='active')
            else:
                self.button_delete_project.configure(state='disabled')
                self.clear_values()
                self.entry0.configure(state='disabled')
                self.entry1.configure(state='disabled')
                self.button_choose.configure(state='disabled')
                self.button_load.configure(state='disabled')
                self.cmb1.configure(state='disabled')
                self.button_add_account.configure(state='disabled')
                self.button_delete_project.configure(state='disabled')

    def delete_account_click(self):
        account = self.table_accounts.current_account
        if tmb.askquestion(title="", message="Удалить %s?" % account.login) == 'yes':
            #db.delete_account(account.login)
            self.table_accounts.delete_account(account)
            #self.table_accounts.refresh()
            self.button_delete_account.configure(state='disabled')
            if self.table_accounts.accounts:
                self.button_delete_account.configure(state='active')
            else:
                self.button_delete_account.configure(state='disabled')

    def trace_change_name(self, a, b, c):
        self.var_message.set("")
        if self.var_name.get():
            self.button_save.configure(state="active")
        else:
            self.button_save.configure(state="disabled")


if __name__ == "__main__":
    db.initialize()
    root = thk.ThemedTk()
    print(root.get_themes())  # Returns a list of all themes that can be set
    root.set_theme("vista")
    projects_manager = ProjectsManager(root);
    root.mainloop()