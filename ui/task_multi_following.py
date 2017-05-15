#!/usr/bin/python
# -*- coding: utf-8 -*-

from ttkthemes import themed_tk as thk
import tkinter as tk
import tkinter.ttk as ttk
from ui import spinbox


class FrameLikes(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, relief="groove", borderwidth=2)

        '''
        self.tk.eval("""ttk::style layout TSpinbox {
    Spinbox.field -sticky {} -children {
        Spinbox.background -sticky w -children {
            Spinbox.padding -sticky w -children {
                Spinbox.innerbg -sticky w -children {
                    Spinbox.textarea -expand 1 -sticky {}
                }
            }
            Spinbox.uparrow -side top -sticky ens
            Spinbox.downarrow -side bottom -sticky ens
        }
    }
        }""")
        '''
        #self.var_check_likes = tk.IntVar()
        self.check_likes = ttk.Checkbutton(self, text="Лайки")
        self.check_likes.grid(row=0, column=0, sticky="w", columnspan=2)

        self.label1 = ttk.Label(self, text="Количество лайков, которые будут\nпоставлены одному пользователю:")
        self.label1.grid(row=1, column=0, sticky="w")

        self.spinbox_likes = spinbox.Spinbox(self, from_=0, to=10, increment=1)
        self.spinbox_likes.grid(row=1, column=1, sticky="w")

        self.var_random_likes = tk.IntVar()
        self.random_likes = ttk.Checkbutton(self, text="Добавлять лайки под случайными записями",
                                            variable=self.var_random_likes)
        self.random_likes.grid(row=2, column=0, sticky="w", columnspan=2)

        self.columnconfigure(0, minsize=350, weight=1)
        self.columnconfigure(1, minsize=40, weight=1)


class FramePause(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, relief="groove", borderwidth=2)

        #self.var_check_likes = tk.IntVar()
        self.check_pause = ttk.Checkbutton(self, text="Случайная пауза")
        self.check_pause.grid(row=0, column=0, sticky="w", columnspan=4)

        self.label1 = ttk.Label(self, text="Случайная пауза каждые")
        self.label1.grid(row=1, column=0, sticky="w", columnspan=2)
        self.spinbox_followers = spinbox.Spinbox(self, from_=1, to=10, increment=1)
        self.spinbox_followers.grid(row=1, column=2)
        self.label2 = ttk.Label(self, text="подписчиков")
        self.label2.grid(row=1, column=3, sticky="w", columnspan=2)

        self.label3 = ttk.Label(self, text="Пауза в минутах")
        self.label3.grid(row=2, column=0, sticky="w")
        self.label4 = ttk.Label(self, text="от")
        self.label4.grid(row=2, column=1, sticky="w")
        self.spinbox_pause_from = spinbox.Spinbox(self, from_=1, to=10, increment=1)
        self.spinbox_pause_from.grid(row=2, column=2)
        self.label5 = ttk.Label(self, text="до")
        self.label5.grid(row=2, column=3, sticky="w")
        self.spinbox_pause_to = spinbox.Spinbox(self, from_=1, to=10, increment=1)
        self.spinbox_pause_to.grid(row=2, column=4)

        self.columnconfigure(0, minsize=140, weight=1)
        self.columnconfigure(1, minsize=40, weight=1)
        self.columnconfigure(2, minsize=40, weight=1)
        self.columnconfigure(3, minsize=30, weight=1)
        self.columnconfigure(4, minsize=50, weight=1)


class TaskMultiFollowingWindow(tk.Toplevel):
    def __init__(self, width, height, parent, callback=None):
        tk.Toplevel.__init__(self, height=height, width=width)

        self.title("Фолловинг по списку")
        self.transient(parent)
        self.grab_set()
        hs = self.winfo_screenheight()
        ws = self.winfo_screenwidth()
        self.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))

        self.frame = ttk.Frame(self)
        self.frame.pack()

        self.header = ttk.Label(self.frame, text='Фолловинг по списку')
        self.header.grid(row=0, column=0, columnspan=6)
        self.label_logins = ttk.Label(self.frame, text="Файл со списком пользователей для фолловинга:")
        self.label_logins.grid(row=1, column=0, sticky="w", columnspan=2)
        self.var_logins = tk.StringVar()
        self.entry_logins = ttk.Entry(self.frame, textvariable=self.var_logins)
        self.entry_logins.grid(row=1, column=2, columnspan=3, sticky="ew")
        self.button_choose = ttk.Button(self.frame, text="Выбрать")
        self.button_choose.grid(row=1, column=5)

        self.label_delay_actions = ttk.Label(self.frame, text='Задержка в секундах между действиями:')
        self.label_delay_actions.grid(row=2, column=0, sticky="w")
        self.label_delay_actions_from = ttk.Label(self.frame, text="от")
        self.label_delay_actions_from.grid(row=2, column=1, sticky="e")
        self.var_delay_actions_from = tk.IntVar()
        self.spinbox_delay_actions_from = spinbox.Spinbox(self.frame, from_=1, to=10, increment=1)
        self.spinbox_delay_actions_from.grid(row=2, column=2)
        self.label_delay_actions_to = ttk.Label(self.frame, text="до")
        self.label_delay_actions_to.grid(row=2, column=3)
        self.var_delay_actions_to = tk.StringVar()
        self.spinbox_delay_actions_to = spinbox.Spinbox(self.frame, from_=1, to=10, increment=1)
        self.spinbox_delay_actions_to.grid(row=2, column=4)

        self.label_followed_count = ttk.Label(self.frame, text="Количество пользователей, которых следует зафолловить:")
        self.label_followed_count.grid(row=3, column=0, sticky="w", columnspan=2)
        self.var_followed_count = tk.StringVar()
        self.spinbox_followed_count = spinbox.Spinbox(self.frame, from_=1, to=10, increment=1)
        self.spinbox_followed_count.grid(row=3, column=2)

        self.var_check_private = tk.IntVar()
        self.check_private = ttk.Checkbutton(self.frame, text="не подписываться на приватные страницы",
                                             variable=self.var_check_private)
        self.check_private.grid(row=4, column=0, sticky="w", columnspan=2)

        self.var_check_followed = tk.IntVar()
        self.check_followed = ttk.Checkbutton(self.frame, text="не подписываться на тех, кто находится в подписчиках",
                                              variable=self.var_check_followed)
        self.check_followed.grid(row=5, column=0, sticky="w", columnspan=2)

        self.frame_likes = FrameLikes(self.frame)
        self.frame_likes.grid(row=6, column=0, sticky="wens")
        self.frame_pause = FramePause(self.frame)
        self.frame_pause.grid(row=6, column=1, columnspan=5, sticky="wens")

        self.button_add = ttk.Button(self.frame, text="Добавить задание")
        self.button_add.grid(row=7, column=0, columnspan=6)

        self.frame.rowconfigure(0, minsize=10, weight=1)
        self.frame.rowconfigure(1, minsize=10, weight=1)
        self.frame.rowconfigure(2, minsize=10, weight=1)
        self.frame.rowconfigure(3, minsize=10, weight=1)
        self.frame.rowconfigure(4, minsize=10, weight=1)
        self.frame.rowconfigure(5, minsize=10, weight=1)
        self.frame.rowconfigure(6, minsize=100, weight=1)
        self.frame.rowconfigure(7, minsize=10, weight=1)
        self.frame.columnconfigure(0, minsize=390, weight=1)
        self.frame.columnconfigure(1, minsize=20, weight=1)
        self.frame.columnconfigure(2, minsize=50, weight=1)
        self.frame.columnconfigure(3, minsize=50, weight=1)
        self.frame.columnconfigure(4, minsize=50, weight=1)
        self.frame.columnconfigure(5, minsize=210, weight=1)

        self.callback = callback


if __name__ == "__main__":
    root = thk.ThemedTk()
    root.set_theme("vista")
    width = 1000
    height = 500
    hs = root.winfo_screenheight()
    ws = root.winfo_screenwidth()
    root.geometry('%dx%d+%d+%d' % (width, height, (ws - width) // 2, (hs - height) // 2))
    TaskMultiFollowingWindow(800, 300, root)
    root.mainloop()