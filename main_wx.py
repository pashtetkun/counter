#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import dbmanager as db
from ui_wx.main_frame import MainFrame

if __name__ == "__main__":
    db.initialize()
    app = wx.App()
    frame = MainFrame(1000, 500);
    frame.Show(True)
    app.MainLoop()