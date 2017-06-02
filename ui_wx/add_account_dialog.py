#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from wx.lib.agw.pycollapsiblepane import PyCollapsiblePane


class AddAccountDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, 'Добавление аккаунта', size=(200, 400))
        sizer = wx.BoxSizer(wx.VERTICAL)

        label_message = wx.StaticText(self, wx.ID_ANY, "")
        sizer.Add(label_message, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        label_login = wx.StaticText(self, wx.ID_ANY, "Логин")
        sizer.Add(label_login, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)
        text_login = wx.TextCtrl(self, wx.ID_ANY)
        sizer.Add(text_login, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        label_password = wx.StaticText(self, wx.ID_ANY, "Пароль")
        sizer.Add(label_password, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)
        text_password = wx.TextCtrl(self, wx.ID_ANY)
        sizer.Add(text_password, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        #checkbox_proxy = wx.CheckBox(self, wx.ID_ANY, "Прокси")
        #sizer_h.Add(checkbox_proxy)
        button_save = wx.Button(self, wx.ID_ANY, label='Сохранить')
        sizer_h.Add(button_save)
        sizer.Add(sizer_h, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        self.collapsible_pane = PyCollapsiblePane(self, wx.ID_ANY, "")
        self.checkbox_proxy1 = wx.CheckBox(self.collapsible_pane, wx.ID_ANY, "Прокси")
        self.Bind(wx.EVT_CHECKBOX, self.proxy_checked, self.checkbox_proxy1)
        #button_toggle_proxy = wx.ToggleButton(collapsible_pane, wx.ID_ANY, "Прокси")
        #collapsible_pane.SetButton(button_toggle_proxy)
        #collapsible_pane.SetLabel("dadadad")
        self.collapsible_pane.SetButton(self.checkbox_proxy1)
        sizer.Add(self.collapsible_pane, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        label_ip = wx.StaticText(self, wx.ID_ANY, "IP-адрес")
        sizer.Add(label_ip, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)
        text_ip = wx.TextCtrl(self, wx.ID_ANY)
        sizer.Add(text_ip, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        label_port = wx.StaticText(self, wx.ID_ANY, "Порт")
        sizer.Add(label_port, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)
        text_port = wx.TextCtrl(self, wx.ID_ANY)
        sizer.Add(text_port, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        choise_protocol = wx.Choice(self, wx.ID_ANY, size=(200, 30))
        sizer.Add(choise_protocol, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        label_proxy_login = wx.StaticText(self, wx.ID_ANY, "Логин")
        sizer.Add(label_proxy_login, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)
        text_proxy_login = wx.TextCtrl(self, wx.ID_ANY)
        sizer.Add(text_proxy_login, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        label_proxy_password = wx.StaticText(self, wx.ID_ANY, "Пароль")
        sizer.Add(label_proxy_password, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)
        text_proxy_password = wx.TextCtrl(self, wx.ID_ANY)
        sizer.Add(text_proxy_password, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)



        self.SetSizer(sizer)
        self.Layout()

    def proxy_checked(self, event):
        if self.checkbox_proxy1.GetValue():
            self.collapsible_pane.Expand()
        else:
            self.collapsible_pane.Collapse()

if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, size=(400, 400));

    dialog = AddAccountDialog(frame)
    dialog.ShowModal()
    dialog.Destroy()

    frame.Show(True)
    app.MainLoop()