#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter.ttk as ttk
from ttkthemes import themed_tk as thk
import tkinter as tk
import dbmanager as db


class TableProjects(ttk.Treeview):
    def __init__(self, parent, unallocated=False):
        ttk.Treeview.__init__(self, parent)

        self.columns = ("Проекты", )
        self.configure(show="headings", selectmode="browse", columns=self.columns)
        for col in self.columns:
            self.heading(col, text=col)
            self.column(col, width=100)
        self.projects = []
        self.current_project = None
        self.unallocated = unallocated

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


if __name__ == "__main__":
    root = thk.ThemedTk()
    print(root.get_themes())  # Returns a list of all themes that can be set
    root.set_theme("vista")
    table_projects = TableProjects(root);
    table_projects.pack()
    root.mainloop()