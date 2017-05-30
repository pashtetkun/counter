#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


class ProjectCard(wx.Panel):
    def __init__(self, parent):
        super(ProjectCard, self).__init__(parent)
        self.do_layout()

    def do_layout(self):
        gridsizer = wx.GridBagSizer()

        name_text = wx.TextCtrl(self, wx.ID_ANY)
        gridsizer.Add(name_text, pos=(0,0))
        accounts_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT)
        gridsizer.Add(accounts_list, pos=(1, 0), span=(4, 1))

        #button_add_account = wx.Button(self, wx.)

        label_loadfromfile = wx.StaticText(self, wx.ID_ANY, "Загрузить аккаунты из списка")
        gridsizer.Add(label_loadfromfile, pos=(1,1))

        text_loadfromfile = wx.TextCtrl(self, wx.ID_ANY)
        gridsizer.Add(text_loadfromfile, pos=(2,1))
        button_loadfromfile = wx.Button(self, wx.ID_ANY, label="Загрузить")
        gridsizer.Add(button_loadfromfile, pos=(2,2))

        label_choice = wx.StaticText(self, wx.ID_ANY, "Выбрать из имеющихся")
        gridsizer.Add(label_choice, pos=(3,1))
        choise = wx.Choice(self, wx.ID_ANY)
        gridsizer.Add(choise, pos=(4,1))
        button_choose = wx.Button(self, wx.ID_ANY, "Выбрать")
        gridsizer.Add(button_choose, pos=(4,2))

        self.SetSizer(gridsizer)
        self.Layout()


class ProjectManager(wx.Panel):
    def __init__(self, parent):
        super(ProjectManager, self).__init__(parent)
        self.do_layout()

    def do_layout(self):
        gridsizer = wx.GridBagSizer()

        projects_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT)
        gridsizer.Add(projects_list, pos=(0,0))

        button_add_project = wx.Button(self, wx.ID_ANY, label='Добавить проект')
        gridsizer.Add(button_add_project, pos=(1,0))

        project_card = ProjectCard(self)
        gridsizer.Add(project_card, pos=(0,1))

        buttons_boxsizer = wx.BoxSizer()
        button_delete_project = wx.Button(self, wx.ID_ANY, label='Удалить проект')
        buttons_boxsizer.Add(button_delete_project)
        button_about_license = wx.Button(self, wx.ID_ANY, label='Информация о лицензии')
        buttons_boxsizer.Add(button_about_license)
        gridsizer.Add(buttons_boxsizer, pos=(1,1))

        self.SetSizer(gridsizer)
        self.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, size=(1000, 600));

    project_manager = ProjectManager(frame)

    frame.Show(True)
    app.MainLoop()