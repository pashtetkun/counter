#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import themed_tk as thk
import instagramapi as api
import threading
import queue
import dbmanager as db


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
                resp2 = insta_worker.get_account_info()
                if resp2.success:
                    self.queue.put(resp2)
                else:
                    self.queue.put(resp)
            else:
                self.queue.put(resp)
        else:
            self.queue.put(api.ResponseStatus(True, None, ''))


class AddAccountWindow(tk.Toplevel):
    def __init__(self, width, height, callback=None):
        tk.Toplevel.__init__(self, height=height, width=width)

        self.height = height
        self.width = width
        self.offsetx = (self.winfo_screenwidth() - self.width) // 2
        self.offsety = (self.winfo_screenheight() - self.height) // 2

        self.title("Добавить аккаунт")
        self.transient(self.master)
        self.grab_set()
        self.geometry('%dx%d+%d+%d'
                      % (self.width, self.height, self.offsetx, self.offsety))
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.frame = ttk.Frame(self)
        self.frame.pack()

        self.frame_account = ttk.Frame(self.frame)
        self.frame_account.pack(fill="x", expand=1)

        self.var_message = tk.StringVar()
        self.label_message = ttk.Label(self.frame_account, textvariable=self.var_message, width=20)
        self.label_message.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.label_message.grid_remove()
        self.progressbar = ttk.Progressbar(self.frame_account, mode='indeterminate', orient=tk.HORIZONTAL)
        self.progressbar.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.progressbar.grid_remove()

        self.label1 = ttk.Label(self.frame_account, text='Логин')
        self.label1.grid(row=1, column=0, sticky="w", columnspan=2)
        self.var_login = tk.StringVar()
        self.var_login.set("")
        self.var_login.trace('w', self.trace_change_entry)
        self.entry1 = ttk.Entry(self.frame_account, textvariable=self.var_login)
        self.entry1.grid(row=2, column=0, sticky="we", columnspan=2)
        self.label2 = ttk.Label(self.frame_account, text='Пароль')
        self.label2.grid(row=3, column=0, sticky="w", columnspan=2)
        self.var_password = tk.StringVar()
        self.var_password.set("")
        self.var_password.trace('w', self.trace_change_entry)
        self.entry2 = ttk.Entry(self.frame_account, textvariable=self.var_password)
        self.entry2.grid(row=4, column=0, sticky="we", columnspan=2)

        self.var_proxy = tk.IntVar()
        self.check1 = ttk.Checkbutton(self.frame_account, text="Прокси", command=self.proxy_checked,
                                      variable=self.var_proxy)
        self.check1.grid(row=5, column=0, sticky="w")
        self.button_save = ttk.Button(self.frame_account, text="Добавить", command=self.save, state="disabled")
        self.button_save.grid(row=5, column=1)

        self.frame_account.rowconfigure(0, minsize=30, weight=1, pad=25)
        self.frame_account.rowconfigure(1, minsize=20, weight=1)
        self.frame_account.rowconfigure(2, minsize=20, weight=1)
        self.frame_account.rowconfigure(3, minsize=20, weight=1)
        self.frame_account.rowconfigure(4, minsize=20, weight=1)
        self.frame_account.rowconfigure(5, minsize=60, weight=1)
        self.frame_account.columnconfigure(0, minsize=75, weight=1)
        self.frame_account.columnconfigure(1, minsize=75, weight=1)

        self.frame_proxy = ttk.Frame(self.frame)
        self.frame_proxy.pack(fill='x', expand=1)

        self.label4 = ttk.Label(self.frame_proxy, text='IP-адрес')
        self.label4.grid(row=0, column=0, sticky="w")
        self.var_ip = tk.StringVar()
        self.entry4 = ttk.Entry(self.frame_proxy, textvariable=self.var_ip)
        self.entry4.grid(row=1, column=0, sticky="ew")

        self.label5 = ttk.Label(self.frame_proxy, text='Порт')
        self.label5.grid(row=2, column=0, sticky="w")
        self.var_port = tk.StringVar()
        self.entry5 = ttk.Entry(self.frame_proxy, textvariable=self.var_port)
        self.entry5.grid(row=3, column=0, sticky="ew")

        self.label6 = ttk.Label(self.frame_proxy, text='Протокол')
        self.label6.grid(row=4, column=0, sticky="w")
        self.var_protocol = tk.StringVar()
        self.cmb1 = ttk.Combobox(self.frame_proxy, textvariable=self.var_protocol, width=16)
        self.cmb1.grid(row=5, column=0, sticky="ew")

        self.label7 = ttk.Label(self.frame_proxy, text='Логин')
        self.label7.grid(row=6, column=0, sticky="w")
        self.var_proxy_login = tk.StringVar()
        self.entry7 = ttk.Entry(self.frame_proxy, textvariable=self.var_proxy_login)
        self.entry7.grid(row=7, column=0, sticky="ew")
        self.label8 = ttk.Label(self.frame_proxy, text='Пароль')
        self.label8.grid(row=8, column=0, sticky="w")
        self.var_proxy_password = tk.StringVar()
        self.entry8 = ttk.Entry(self.frame_proxy, textvariable=self.var_proxy_password)
        self.entry8.grid(row=9, column=0, sticky="ew")

        self.frame_proxy.rowconfigure(0, minsize=20, weight=1)
        self.frame_proxy.rowconfigure(1, minsize=20, weight=1)
        self.frame_proxy.rowconfigure(2, minsize=20, weight=1)
        self.frame_proxy.rowconfigure(3, minsize=20, weight=1)
        self.frame_proxy.rowconfigure(4, minsize=20, weight=1)
        self.frame_proxy.rowconfigure(5, minsize=20, weight=1)
        self.frame_proxy.rowconfigure(6, minsize=20, weight=1)
        self.frame_proxy.rowconfigure(7, minsize=20, weight=1)
        self.frame_proxy.rowconfigure(8, minsize=20, weight=1)
        self.frame_proxy.rowconfigure(9, minsize=20, weight=1)
        self.frame_proxy.columnconfigure(0, minsize=100, weight=1)

        self.callback = callback

        #self.proxy_checked()
        self.queue = queue.Queue()
        self.thread = None

    def save(self):
        self.var_message.set("")
        if db.is_exist_account(self.var_login.get()):
            self.label_message.grid()
            self.var_message.set("Аккаунт уже есть в базе")
            return
        self.button_save.configure(state='disabled')
        self.entry1.configure(state="disabled")
        self.entry2.configure(state="disabled")
        self.progressbar.grid(row=0, column=0)
        self.progressbar.start()
        self.thread = ThreadedClient(self.queue, self.var_login.get(), self.var_password.get(), True)
        self.thread.start()
        self.master.after(200, self.listen_queue)

    def listen_queue(self):
        try:
            resp = self.queue.get(0)
            self.process_message(resp)
        except queue.Empty:
            self.master.after(200, self.listen_queue)

    def process_message(self, resp):
        if resp.success:
            follows = resp.results["follows"] if resp.results else 0
            followers = resp.results["followers"] if resp.results else 0
            user_id = resp.results["user_id"] if resp.results else ''
            db.create_account(self.var_login.get(), self.var_password.get(), user_id, follows, followers)
            if self.callback:
                self.callback(True)
            self.destroy()
        else:
            self.progressbar.stop()
            self.progressbar.grid_remove()
            self.var_message.set(resp.message)
            self.label_message.grid()
            self.entry1.configure(state="active")
            self.entry2.configure(state="active")

    def proxy_checked(self):
        if self.var_proxy.get() == 1 :
            self.frame_proxy.pack()
            self.height  += 100
            self.geometry('%dx%d+%d+%d'
                          % (self.width, self.height, self.offsetx, self.offsety))
        else:
            self.frame_proxy.forget()
            self.height -= 100
            self.geometry('%dx%d+%d+%d'
                          % (self.width, self.height, self.offsetx, self.offsety))

    def close_window(self):
        if self.thread:
            pass
        self.destroy()


    def trace_change_entry(self, a, b, c):
        if self.var_login.get() and self.var_password.get():
            self.button_save.configure(state="active")
            self.var_message.set("")
        else:
            self.button_save.configure(state="disabled")


if __name__ == "__main__":
    root = thk.ThemedTk()
    root.set_theme("vista")
    width = 1000
    height = 500
    hs = root.winfo_screenheight()
    ws = root.winfo_screenwidth()
    root.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))
    db.initialize()
    add_account_window = AddAccountWindow(200, 160)
    root.mainloop()