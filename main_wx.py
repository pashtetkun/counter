#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from ui_wx.main_frame import MainFrame

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(1000, 500);
    frame.Show(True)
    app.MainLoop()