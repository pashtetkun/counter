#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


class MainNotebook(wx.Notebook):
    def __init__(self, parent):
        super(MainNotebook, self).__init__(parent)
        panel0 = wx.Panel(self)
        panel1 = wx.Panel(self)
        panel2 = wx.Panel(self)
        panel3 = wx.Panel(self)
        panel4 = wx.Panel(self)
        self.AddPage(panel0, 'Менеджер проектов')
        self.AddPage(panel1, 'Менеджер заданий')
        self.AddPage(panel2, 'Сбор аудитории')
        self.AddPage(panel3, 'Настройки')
        self.AddPage(panel4, 'Логи')

        self.SetFont(wx.Font(wx.FontInfo(20)))


if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, size=(1000, 600))
    notebook = MainNotebook(frame)

    frame.Show(True)
    app.MainLoop()