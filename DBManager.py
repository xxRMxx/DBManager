#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import things for database communication and system processes
from Tkinter import *
from ttk import *
from ScrolledText import *
from subprocess import Popen, PIPE
from shlex import split
from datetime import datetime
import tkMessageBox
import time
import os
import psycopg2

# custom modules
import functions
import styles

# TODO
# responsiveness
# more fresh design
# add focus (highlighting for current active field)
# rewrite all functions to send a call and retrieve the result
# describe the concrete exception

# check whether logfile exists; else create it
try:
    functions.popen('ls /var/log/dbmanager.log | grep dbmanager.log')
except:
    functions.popen('cd /var/log/ && touch dbmanager.log')


filename = '/var/log/dbmanager.log'
timestamp = str(datetime.now())


# build the gui
root = Tk()
root.title('DBManager')
root.minsize(
    width = styles.globalWidth,
    height = styles.globalHeight
)
root.resizable(
    width = False,
    height = False
)
root.call('wm', 'iconphoto', root._w, PhotoImage(file = styles.app_logo))


note = Notebook(root)


# list of logic scripts
commands = [
    './Root/commands.py',
    './Database/commands.py',
    './Table/commands.py',
    './MxNTable/commands.py',
    './Column/commands.py',
    './Foreignkey/commands.py',
    './Sequence/commands.py',
    './Content/commands.py',
    './Analyzer/commands.py',
    './Diagram/commands.py',
    './functions.py'
]


# list of view scripts
views = [
    './Root/view.py',
    './Database/view.py',
    './Table/view.py',
    './MxNTable/view.py',
    './Column/view.py',
    './Foreignkey/view.py',
    './Sequence/view.py',
    './Content/view.py',
    './Analyzer/view.py',
    './Diagram/view.py',
    './styles.py'
]


# import logic
for script in commands:
    execfile(script)


# import views
for view in views:
    execfile(view)


# keyboard shortcut to show available databases, users, tables and columns by key press
root.bind('<F1>', showDatabases)
root.bind('<F2>', showUsers)
root.bind('<F3>', showTables)
root.bind('<F4>', showColumns)


# run gui
root.mainloop()
