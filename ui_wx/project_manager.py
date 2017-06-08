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
        sizer = wx.GridBagSizer(vgap=5, hgap = 5)

        self.name_text = wx.TextCtrl(self, wx.ID_ANY, name='name')
        sizer.Add(self.name_text, pos=(0,0), flag=wx.EXPAND)
        accounts_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT, size=(200, 200))
        sizer.Add(accounts_list, pos=(1, 0), span=(4, 1))

        button_add_account = wx.Button(self, wx.ID_ANY, label="Добавить аккаунт")
        self.Bind(wx.EVT_BUTTON, self.add_account_click, button_add_account)
        sizer.Add(button_add_account, pos=(5,0), flag=wx.EXPAND)

        self.message_text = wx.StaticText(self, wx.ID_ANY, "")
        sizer.Add(self.message_text, pos=(0, 1), flag=wx.EXPAND)
        label_loadfromfile = wx.StaticText(self, wx.ID_ANY, "Загрузить аккаунты из списка")
        sizer.Add(label_loadfromfile, pos=(1,1))

        text_loadfromfile = wx.TextCtrl(self, wx.ID_ANY)
        sizer.Add(text_loadfromfile, pos=(2,1), flag=wx.EXPAND)
        button_loadfromfile = wx.Button(self, wx.ID_ANY, label="Загрузить")
        sizer.Add(button_loadfromfile, pos=(2,2))

        label_choice = wx.StaticText(self, wx.ID_ANY, "Выбрать из имеющихся")
        sizer.Add(label_choice, pos=(3,1))
        choice = wx.Choice(self, wx.ID_ANY, size=(200, 30))
        sizer.Add(choice, pos=(4,1))
        button_choose = wx.Button(self, wx.ID_ANY, "Выбрать")
        sizer.Add(button_choose, pos=(4,2))

        self.button_save = wx.Button(self, wx.ID_ANY, label="Сохранить")
        self.button_save.Bind(wx.EVT_BUTTON, self.save_click)
        sizer.Add(self.button_save, pos=(5, 2))

        self.SetSizer(sizer)
        self.Layout()

    def add_account_click(self, event):
        dialog = AddAccountDialog(self.Parent)
        dialog.ShowModal()
        dialog.Destroy()

    def save_click(self, event):
        name = self.name_text.GetValue()
        if not self.check_name(name):
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
        project_manager.refresh_projects(name)

    def check_name(self, name):
        project_manager = self.GetParent()
        if self.new_mode:
            if next((x for x in list(project_manager.projects_map.values()) if x.name == name), None):
                return False
        else:
            #id = self.table_projects.current_project.id
            #if next((x for x in self.table_projects.projects if x.name == name and x.id != id), None):
                #return False
            pass
        return True

    def show_values(self, project):
        self.Enable()
        self.name_text.SetValue(project.name)


class ProjectManager(wx.Panel):
    def __init__(self, parent):
        super(ProjectManager, self).__init__(parent)
        self.do_layout()
        self.projects_map = {}
        self.refresh_projects()

        self.project_card.Disable()
        self.button_delete_project.Disable()

    def do_layout(self):
        sizer = wx.GridBagSizer(vgap=5, hgap=5)

        self.projects_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT, size=(200, 300))
        self.projects_list.InsertColumn(0, "Проекты", width=200, format=wx.LIST_FORMAT_CENTRE)
        self.projects_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_project_selected)
        sizer.Add(self.projects_list, pos=(0,0))

        self.button_add_project = wx.Button(self, wx.ID_ANY, label='Добавить проект')
        self.button_add_project.Bind(wx.EVT_BUTTON, self.add_project_click)
        sizer.Add(self.button_add_project, pos=(1,0), flag=wx.EXPAND)

        self.project_card = ProjectCard(self)
        sizer.Add(self.project_card, pos=(0,1))

        buttons_boxsizer = wx.BoxSizer()
        self.button_delete_project = wx.Button(self, wx.ID_ANY, label='Удалить проект', size=(200, 30))
        self.button_delete_project.Bind(wx.EVT_BUTTON, self.delete_project_click)
        buttons_boxsizer.Add(self.button_delete_project)
        button_about_license = wx.Button(self, wx.ID_ANY, label='Информация о лицензии')
        buttons_boxsizer.Add(button_about_license, flag=wx.EXPAND)
        sizer.Add(buttons_boxsizer, pos=(1,1))

        self.SetSizer(sizer)
        self.Layout()

    def clear_values(self):
        text_login = wx.FindWindowByName('name', self.project_card)
        text_login.SetValue('')

    def add_project_click(self, event):
        self.project_card.Enable()
        self.clear_values()
        self.project_card.new_mode = True

    def refresh_projects(self, selected=None):
        projects = db.get_all_projects()
        if not projects:
            self.project_card.Disable()
            self.button_delete_project.Disable()

        self.projects_list.DeleteAllItems()
        for idx, project in enumerate(projects):
            self.projects_list.Append([project.name])
            self.projects_map[idx] = project
            if project.name == selected:
                self.projects_list.Select(idx)

        self.projects_list.Layout()

    def on_project_selected(self, event):
        project = self.projects_map[event.Item.Id]
        self.project_card.show_values(project)
        self.button_delete_project.Enable()

    def delete_project_click(self, event):
        project = self.projects_map[self.projects_list.GetFirstSelected()]
        dlg = wx.MessageBox(message="Удалить проект '%s'?" % project.name, caption='Удаление',
                               style=wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg == wx.YES:
            db.delete_project(project.name)
            self.refresh_projects()


if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, size=(800, 400));

    project_manager = ProjectManager(frame)

    frame.Show(True)
    app.MainLoop()