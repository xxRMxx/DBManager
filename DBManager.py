#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The DBManager is an API for database communication
# supported databases: Postgres

# TODO
# responsiveness
# database analyzer
# more fresh design
# show application logo when in window switcher
# in foreign key view there is no hote.grid() at end --> valdiate if needed


# import things for database communication and system processes
from Tkinter import *
from ttk import *
from ScrolledText import *
from subprocess import Popen, PIPE
from shlex import split
from datetime import datetime
import tkMessageBox
import psycopg2
import subprocess
import time

# import the main styling for buttons, inputFields etc.
import styles


timestamp = str(datetime.now())

# check whether logfile exists; else create it
try:
    subprocess.Popen("ls /var/log/dbmanager.log | grep dbmanager.log", shell = True)
except:
    subprocess.Popen("cd /var/log/ && touch dbmanager.log", shell = True)

filename = '/var/log/dbmanager.log'


# build the gui
root = Tk()
root.title("DBManager")
root.minsize(
    width = styles.globalWidth,
    height = styles.globalHeight
)
# TODO: make this resizable?
root.resizable(
    width = False,
    height = False
)

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
    './Diagram/commands.py'
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
    './Diagram/view.py'
]


# import logic
for script in commands:
    execfile(script)


# import views
for view in views:
    execfile(view)


# run gui
root.mainloop()
