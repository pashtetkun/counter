#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from ui_wx.add_account_dialog import AddAccountDialog


class ProjectCard(wx.Panel):
    def __init__(self, parent):
        super(ProjectCard, self).__init__(parent)
        self.do_layout()

    def do_layout(self):
        gridsizer = wx.GridBagSizer(vgap=5, hgap = 5)

        name_text = wx.TextCtrl(self, wx.ID_ANY)
        gridsizer.Add(name_text, pos=(0,0), flag=wx.EXPAND)
        accounts_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT, size=(200, 200))
        gridsizer.Add(accounts_list, pos=(1, 0), span=(4, 1))

        button_add_account = wx.Button(self, wx.ID_ANY, label="Добавить аккаунт")
        self.Bind(wx.EVT_BUTTON, self.addAccountClick, button_add_account)
        gridsizer.Add(button_add_account, pos=(5,0), flag=wx.EXPAND)

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
        gridsizer.Add(button_save, pos=(5, 2))

        self.SetSizer(gridsizer)
        self.Layout()

    def addAccountClick(self, event):
        dialog = AddAccountDialog(self.Parent)
        dialog.ShowModal()
        dialog.Destroy()



class ProjectManager(wx.Panel):
    def __init__(self, parent):
        super(ProjectManager, self).__init__(parent)
        self.do_layout()

    def do_layout(self):
        gridsizer = wx.GridBagSizer(vgap=5, hgap=5)

        projects_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT, size=(200, 300))
        projects_list.InsertColumn(0, "Проекты", width=200, format=wx.LIST_FORMAT_CENTRE)
        gridsizer.Add(projects_list, pos=(0,0))

        button_add_project = wx.Button(self, wx.ID_ANY, label='Добавить проект')
        gridsizer.Add(button_add_project, pos=(1,0), flag=wx.EXPAND)

        project_card = ProjectCard(self)
        gridsizer.Add(project_card, pos=(0,1))

        buttons_boxsizer = wx.BoxSizer()
        button_delete_project = wx.Button(self, wx.ID_ANY, label='Удалить проект', size=(200, 30))
        buttons_boxsizer.Add(button_delete_project)
        button_about_license = wx.Button(self, wx.ID_ANY, label='Информация о лицензии')
        buttons_boxsizer.Add(button_about_license, flag=wx.EXPAND)
        gridsizer.Add(buttons_boxsizer, pos=(1,1))

        self.SetSizer(gridsizer)
        self.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, size=(800, 400));

    project_manager = ProjectManager(frame)

    frame.Show(True)
    app.MainLoop()