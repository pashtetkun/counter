#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter.ttk as ttk

if __name__ == "__main__":
    s = ttk.Style()
    print(s.layout('TNotebook'))
    print(s.layout('TNotebook.Tab'))
    print('Notebook.client: ', s.element_options('Notebook.client'))
    print('Notebook.tab: ', s.element_options('Notebook.tab'))
    print('Notebook.padding: ', s.element_options('Notebook.padding'))
    print('Notebook.focus: ', s.element_options('Notebook.focus'))
    print('Notebook.label: ', s.element_options('Notebook.label'))

    print('padding:', s.lookup('Notebook.padding', 'padding'))

    print('label:', s.lookup('Notebook.label', 'background'))