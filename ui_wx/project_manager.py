#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from ui_wx.add_account_dialog import AddAccountDialog
import dbmanager as db


class ProjectCard(wx.Panel):
    def __init__(self, parent):
        super(ProjectCard, self).__init__(parent)
        self.do_layout()
        self.new_mode = False

    def do_layout(self):
        gridsizer = wx.GridBagSizer(vgap=5, hgap = 5)

        self.name_text = wx.TextCtrl(self, wx.ID_ANY, name='name')
        gridsizer.Add(self.name_text, pos=(0,0), flag=wx.EXPAND)
        accounts_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT, size=(200, 200))
        gridsizer.Add(accounts_list, pos=(1, 0), span=(4, 1))

        button_add_account = wx.Button(self, wx.ID_ANY, label="Добавить аккаунт")
        self.Bind(wx.EVT_BUTTON, self.addAccountClick, button_add_account)
        gridsizer.Add(button_add_account, pos=(5,0), flag=wx.EXPAND)

        self.message_text = wx.StaticText(self, wx.ID_ANY, "")
        gridsizer.Add(self.message_text, pos=(0, 1), flag=wx.EXPAND)
        label_loadfromfile = wx.StaticText(self, wx.ID_ANY, "Загрузить аккаунты из списка")
        gridsizer.Add(label_loadfromfile, pos=(1,1))

        text_loadfromfile = wx.TextCtrl(self, wx.ID_ANY)
        gridsizer.Add(text_loadfromfile, pos=(2,1), flag=wx.EXPAND)
        button_loadfromfile = wx.Button(self, wx.ID_ANY, label="Загрузить")
        gridsizer.Add(button_loadfromfile, pos=(2,2))

        label_choice = wx.StaticText(self, wx.ID_ANY, "Выбрать из имеющихся")
        gridsizer.Add(label_choice, pos=(3,1))
        choise = wx.Choice(self, wx.ID_ANY, size=(200, 30))
        gridsizer.Add(choise, pos=(4,1))
        button_choose = wx.Button(self, wx.ID_ANY, "Выбрать")
        gridsizer.Add(button_choose, pos=(4,2))

        button_save = wx.Button(self, wx.ID_ANY, label="Сохранить")
        self.Bind(wx.EVT_BUTTON, self.saveClick, button_save)
        gridsizer.Add(button_save, pos=(5, 2))

        self.SetSizer(gridsizer)
        self.Layout()

    def addAccountClick(self, event):
        dialog = AddAccountDialog(self.Parent)
        dialog.ShowModal()
        dialog.Destroy()

    def saveClick(self, event):
        name = self.name_text.GetValue()
        if not self.checkName(name):
            self.message_text.SetLabel('need unique name')
            return
        if self.new_mode:
            project = db.create_project(name)
        else:
            #project = self.table_projects.current_project
            #project.name = self.var_name.get()
            #db.update_project(project)
            pass

        project_manager = self.GetParent()
        project_manager.refreshProjects()



    def checkName(self, name):
        project_manager = self.GetParent()
        if self.new_mode:
            if next((x for x in project_manager.projects if x.name == name), None):
                return False
        else:
            #id = self.table_projects.current_project.id
            #if next((x for x in self.table_projects.projects if x.name == name and x.id != id), None):
                #return False
            pass
        return True




class ProjectManager(wx.Panel):
    def __init__(self, parent):
        super(ProjectManager, self).__init__(parent)
        self.do_layout()
        self.projects = []
        self.refreshProjects()

    def do_layout(self):
        gridsizer = wx.GridBagSizer(vgap=5, hgap=5)

        self.projects_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT, size=(200, 300))
        self.projects_list.InsertColumn(0, "Проекты", width=200, format=wx.LIST_FORMAT_CENTRE)
        gridsizer.Add(self.projects_list, pos=(0,0))

        button_add_project = wx.Button(self, wx.ID_ANY, label='Добавить проект')
        self.Bind(wx.EVT_BUTTON, self.addProjectClick, button_add_project)
        gridsizer.Add(button_add_project, pos=(1,0), flag=wx.EXPAND)

        self.project_card = ProjectCard(self)
        gridsizer.Add(self.project_card, pos=(0,1))

        buttons_boxsizer = wx.BoxSizer()
        self.button_delete_project = wx.Button(self, wx.ID_ANY, label='Удалить проект', size=(200, 30))
        buttons_boxsizer.Add(self.button_delete_project)
        button_about_license = wx.Button(self, wx.ID_ANY, label='Информация о лицензии')
        buttons_boxsizer.Add(button_about_license, flag=wx.EXPAND)
        gridsizer.Add(buttons_boxsizer, pos=(1,1))

        self.SetSizer(gridsizer)
        self.Layout()


    def clear_values(self):
        text_login = wx.FindWindowByName('name', self.project_card)
        text_login.SetValue('')

    def addProjectClick(self, event):
        self.project_card.Enable()
        self.clear_values()
        self.project_card.new_mode = True

    def refreshProjects(self):
        self.projects = db.get_all_projects()
        if not self.projects:
            self.project_card.Disable()
            self.button_delete_project.Disable()

        self.projects_list.DeleteAllItems()
        for project in self.projects:
            self.projects_list.Append([project.name])
        self.projects_list.Layout()



if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, size=(800, 400));

    project_manager = ProjectManager(frame)

    frame.Show(True)
    app.MainLoop()