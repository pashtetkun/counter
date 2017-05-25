#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


class MainWindow:
    def __init__(self, width, height):
        app = wx.App()
        wnd = wx.Frame(None, wx.ID_ANY, "main window")
        wnd.Show(True)
        app.MainLoop()

if __name__ == "__main__":
    MainWindow(1000, 500);