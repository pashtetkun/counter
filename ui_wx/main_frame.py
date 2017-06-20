#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import dbmanager as db
from ui_wx.main_notebook import MainNotebook


class MainFrame(wx.Frame):
    def __init__(self, width, height):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Инстаграммер", size=(width, height))
        self.Center(dir=wx.BOTH)
        #icon = wx.Icon()
        #icon.CopyFromBitmap(wx.Bitmap("../smoking.ico", wx.BITMAP_TYPE_ANY))
        #self.SetIcon(icon)

        notebook = MainNotebook(self)
        boxsizer = wx.BoxSizer(wx.VERTICAL)
        boxsizer.Add(notebook)

        self.SetSizer(boxsizer)
        self.Layout()

if __name__ == "__main__":
    db.initialize()
    app = wx.App()
    frame = MainFrame(1000, 500);
    frame.Show(True)
    app.MainLoop()