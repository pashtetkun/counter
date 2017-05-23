#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import dbmanager as db


if __name__ == "__main__":
    db.initialize()
    app = wx.App()
    wnd = wx.Frame(None, wx.ID_ANY, "main window")
    wnd.Show(True)
    app.MainLoop()