# coding=utf-8

import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import themed_tk as thk
import instagramapi as api


class AddAccountWindow(tk.Toplevel):
    def __init__(self, width, height, parent, callback=None):
        tk.Toplevel.__init__(self, height=height, width=width)

        self.title("")
        self.transient(parent)
        self.grab_set()
        hs = self.winfo_screenheight()
        ws = self.winfo_screenwidth()
        self.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))

        self.frame = ttk.Frame(self)
        self.frame.pack()

        self.frame_account = ttk.Frame(self.frame)
        self.frame_account.pack(fill="x", expand=1)

        self.header = ttk.Label(self.frame_account, text="Добавить аккаунт")
        self.header.grid(row=0, column=0)
        self.label1 = ttk.Label(self.frame_account, text='Логин')
        self.label1.grid(row=1, column=0, sticky="w")
        self.var_login = tk.StringVar()
        self.entry1 = ttk.Entry(self.frame_account, textvariable=self.var_login)
        self.entry1.grid(row=2, column=0, sticky="we")
        self.label2 = ttk.Label(self.frame_account, text='Пароль')
        self.label2.grid(row=3, column=0, sticky="w")
        self.var_password = tk.StringVar()
        self.entry2 = ttk.Entry(self.frame_account, textvariable=self.var_password)
        self.entry2.grid(row=4, column=0, sticky="ew")
        self.var_message = tk.StringVar()
        self.label3 = ttk.Label(self.frame_account, textvariable=self.var_message, width=10)
        self.label3.grid(row=5, column=0)
        self.button_save = ttk.Button(self.frame_account, text="Сохранить", command=self.save)
        self.button_save.grid(row=6, column=0)

        '''
        self.var_proxy = tk.IntVar()
        self.check1 = ttk.Checkbutton(self.frame_account, text="Прокси", command=self.proxy_checked,
                                             variable=self.var_proxy, state='disabled')
        self.check1.grid(row=7, column=0, sticky="w")
        '''

        self.frame_account.rowconfigure(0, minsize=20, weight=1, pad=25)
        self.frame_account.rowconfigure(1, minsize=20, weight=1)
        self.frame_account.rowconfigure(2, minsize=20, weight=1)
        self.frame_account.rowconfigure(3, minsize=20, weight=1)
        self.frame_account.rowconfigure(4, minsize=20, weight=1)
        self.frame_account.rowconfigure(5, minsize=60, weight=1)
        self.frame_account.rowconfigure(6, minsize=10, weight=1)
        #self.frame_account.rowconfigure(7, minsize=20, weight=1)
        self.frame_account.columnconfigure(0, minsize=100, weight=1)

        '''
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
        '''
        self.callback = callback

        #self.proxy_checked()

    def save(self):
        resp = api.do_login(self.var_login.get(), self.var_password.get())
        if not resp.success:
            self.var_message.set(resp.message)
        else:
            if self.callback:
                self.callback(self.var_login.get(), self.var_password.get())
            self.destroy()


    def proxy_checked(self):
        if self.var_proxy.get() == 1 :
            #self.label4.grid_remove()
            #self.cmb1.forget()
            self.frame_proxy.pack()
        else:
            #self.label4.grid()
            #self.cmb1.grid()
            self.frame_proxy.forget()


if __name__ == "__main__":
    root = thk.ThemedTk()
    root.set_theme("vista")
    width = 1000
    height = 500
    hs = root.winfo_screenheight()
    ws = root.winfo_screenwidth()
    root.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))
    add_account_window = AddAccountWindow(180, 220, root )
    root.mainloop()