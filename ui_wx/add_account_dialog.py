#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import dbmanager as db
from models import Account
import instagramapi as api
import threading
import queue


class ThreadedClient(threading.Thread):

    def __init__(self, queue, login, password, isTest=False):
        threading.Thread.__init__(self)
        self.queue = queue
        self.login = login
        self.password = password
        self.isTest = isTest

    def run(self):
        if not self.isTest:
            insta_worker = api.InstaWorker(self.login, self.password)
            resp = insta_worker.do_login()
            if resp.success:
                #resp2 = insta_worker.get_account_info()
                #if resp2.success:
                    #self.queue.put(resp2)
                #else:
                    self.queue.put(resp)
            else:
                self.queue.put(resp)
        else:
            self.queue.put(api.ResponseStatus(True, None, ''))


class AddAccountDialog(wx.Dialog):
    def __init__(self, parent, callback=None):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, 'Добавление аккаунта', size=(300, 400))
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.gauge = wx.Gauge(self, wx.ID_ANY)
        sizer.Add(self.gauge)
        self.gauge.Hide()
        self.label_message = wx.StaticText(self, wx.ID_ANY, "", size=(200,30))
        sizer.Add(self.label_message, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        label_login = wx.StaticText(self, wx.ID_ANY, "Логин")
        sizer.Add(label_login, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)
        self.text_login = wx.TextCtrl(self, wx.ID_ANY)
        sizer.Add(self.text_login, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        label_password = wx.StaticText(self, wx.ID_ANY, "Пароль")
        sizer.Add(label_password, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)
        self.text_password = wx.TextCtrl(self, wx.ID_ANY)
        sizer.Add(self.text_password, flag=wx.EXPAND|wx.RIGHT|wx.LEFT, border=10)

        sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        self.checkbox_proxy = wx.CheckBox(self, wx.ID_ANY, "Прокси")
        self.Bind(wx.EVT_CHECKBOX, self.proxy_checked, self.checkbox_proxy)
        sizer_h.Add(self.checkbox_proxy)
        button_save = wx.Button(self, wx.ID_ANY, label='Сохранить')
        self.Bind(wx.EVT_BUTTON, self.save_clicked, button_save)
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

        self.callback = callback
        self.queue = queue.Queue()
        self.thread = None

    def proxy_checked(self, event):
        if self.checkbox_proxy.GetValue():
            self.proxy_panel.Show()
            self.SetSize((300,400))
        else:
            self.proxy_panel.Hide()
            self.SetSize((300, 200))

    def save_clicked(self, event):
        self.label_message.SetLabel("")
        self.label_message.Hide()
        login = self.text_login.GetValue()
        password = self.text_password.GetValue()
        if db.is_exist_account(login):
            self.label_message.Show()
            self.label_message.SetLabel("Аккаунт уже есть в базе")
            return
        self.gauge.Show()
        self.gauge.Pulse()

        self.thread = ThreadedClient(self.queue, login, password, True)
        self.thread.start()
        wx.CallLater(500, self.listen_queue)
        #self.master.after(200, self.listen_queue)

    def listen_queue(self):
        try:
            resp = self.queue.get(0)
            self.process_message(resp)
        except queue.Empty:
            #self.master.after(200, self.listen_queue)
            wx.CallLater(500, self.listen_queue)

    def process_message(self, resp):
        if resp.success:
            #follows = resp.results["follows"] if resp.results else 0
            #followers = resp.results["followers"] if resp.results else 0
            #user_id = resp.results["user_id"] if resp.results else ''
            #db.create_account(self.var_login.get(), self.var_password.get(), user_id, follows, followers)
            if self.callback:
                account = Account(login=self.text_login.GetValue(),
                                  password=self.text_password.GetValue())
                self.callback(account)
            self.Close()
        else:
            self.gauge.SetValue(100)
            self.gauge.Hide()
            self.label_message.Show()
            self.label_message.SetLabel("")

def callback(account):
    db.create_account(account)

if __name__ == "__main__":
    db.initialize()
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, size=(400, 200));

    dialog = AddAccountDialog(frame, callback)
    dialog.ShowModal()
    dialog.Destroy()

    frame.Show(True)
    app.MainLoop()