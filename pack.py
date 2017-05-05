#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'c:/Python36-32/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'c:/Python36-32/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = ["tkinter"],
    excludes = [],
    include_files=['c:/Python36-32/DLLs/tcl86t.dll', 'c:/Python36-32/DLLs/tk86t.dll']
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base = base)
]

setup(
    name = "App",
    version = "0.1",
    description = "test",
    options = {"build_exe": buildOptions},
    executables = executables)