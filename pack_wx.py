#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = ["wx", "idna"],
    excludes = [],
    includes = [],
    include_files=[]
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main_wx.py', base = base)
]

setup(
    name = "App",
    version = "0.1",
    description = "test",
    options = {"build_exe": buildOptions},
    executables = executables)