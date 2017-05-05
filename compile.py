#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup
#from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("ui.mainWindow", ["ui/mainWindow.py"]),
    Extension("models.account", ["models/account.py"]),
    Extension("dbmanager.dbmanager", ["dbmanager/dbmanager.py"]),
    ]

setup(
    name = 'App',
    #ext_modules = cythonize("main.pyx")
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)