#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from ui_wx.project_manager import ProjectManager


class MainNotebook(wx.Notebook):
    def __init__(self, parent):
        super(MainNotebook, self).__init__(parent)
        panel0 = ProjectManager(self)
        panel1 = wx.Panel(self)
        panel2 = wx.Panel(self)
        panel3 = wx.Panel(self)
        panel4 = wx.Panel(self)
        self.AddPage(panel0, 'Менеджер проектов')
        self.AddPage(panel1, 'Менеджер заданий ')
        self.AddPage(panel2, 'Сбор аудитории   ')
        self.AddPage(panel3, 'Настройки        ')
        self.AddPage(panel4, 'Логи             ')

        self.SetBackgroundColour('gray')
        self.SetFont(wx.Font(wx.FontInfo(16)))
        #self.SetPadding((5,5))
        #self.SetWindowStyle(wx.NB_FIXEDWIDTH)


if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, size=(1000, 600))
    notebook = MainNotebook(frame)

    frame.Show(True)
    app.MainLoop()