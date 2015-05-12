from distutils.core import setup

import py2exe

setup (console= [{"script":'DNHconsoleMain.py', "icon_resources":[(1,"favicon.ico")]}])