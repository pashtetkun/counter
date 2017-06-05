#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


class AddAccountDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, 'Добавление аккаунта', size=(300, 400))
        sizer = wx.BoxSizer(wx.VERTICAL)

        label_message = wx.StaticText(self, wx.ID_ANY, "", size=(200,30))
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
        self.checkbox_proxy = wx.CheckBox(self, wx.ID_ANY, "Прокси")
        self.Bind(wx.EVT_CHECKBOX, self.proxy_checked, self.checkbox_proxy)
        sizer_h.Add(self.checkbox_proxy)
        button_save = wx.Button(self, wx.ID_ANY, label='Сохранить')
        sizer_h.Add(button_save)
        sizer.Add(sizer_h)

        self.proxy_panel = wx.Panel(self)

        sizer_pane = wx.BoxSizer(wx.VERTICAL)

        label_ip = wx.StaticText(self.proxy_panel, wx.ID_ANY, "IP-адрес")
        sizer_pane.Add(label_ip, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)
        text_ip = wx.TextCtrl(self.proxy_panel, wx.ID_ANY)
        sizer_pane.Add(text_ip, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)

        label_port = wx.StaticText(self.proxy_panel, wx.ID_ANY, "Порт")
        sizer_pane.Add(label_port, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)
        text_port = wx.TextCtrl(self.proxy_panel, wx.ID_ANY)
        sizer_pane.Add(text_port, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)

        label_protocol = wx.StaticText(self.proxy_panel, wx.ID_ANY, "Протокол")
        sizer_pane.Add(label_protocol, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)
        choise_protocol = wx.Choice(self.proxy_panel, wx.ID_ANY, size=(200, 30))
        sizer_pane.Add(choise_protocol, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)

        label_proxy_login = wx.StaticText(self.proxy_panel, wx.ID_ANY, "Логин")
        sizer_pane.Add(label_proxy_login, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)
        text_proxy_login = wx.TextCtrl(self.proxy_panel, wx.ID_ANY)
        sizer_pane.Add(text_proxy_login, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)

        label_proxy_password = wx.StaticText(self.proxy_panel, wx.ID_ANY, "Пароль")
        sizer_pane.Add(label_proxy_password, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)
        text_proxy_password = wx.TextCtrl(self.proxy_panel, wx.ID_ANY)
        sizer_pane.Add(text_proxy_password, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)

        self.proxy_panel.SetSizer(sizer_pane)

        sizer.Add(self.proxy_panel)

        self.SetSizer(sizer)
        self.Layout()

        self.proxy_panel.Hide()

    def proxy_checked(self, event):
        if self.checkbox_proxy.GetValue():
            self.proxy_panel.Show()
            self.SetSize((300,400))
        else:
            self.proxy_panel.Hide()
            self.SetSize((300, 200))

if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, size=(400, 200));

    dialog = AddAccountDialog(frame)
    dialog.ShowModal()
    dialog.Destroy()

    frame.Show(True)
    app.MainLoop()