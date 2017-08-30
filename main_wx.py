#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import dbmanager as db
from ui_wx.main_notebook import MainNotebook

if __name__ == "__main__":
    db.initialize()
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Инстаграммер", size=(1000, 500))
    frame.Center(dir=wx.BOTH)
    notebook = MainNotebook(frame)
    frame.Show(True)
    app.MainLoop()