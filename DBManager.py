#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The DBManager is an API for database communication and development
# current database: Postgres

# import things for database and system
from Tkinter import *
from ttk import *
from ScrolledText import *
from subprocess import Popen, PIPE
from shlex import split
import tkMessageBox
import psycopg2
import subprocess
import time

from datetime import datetime
timestamp = str(datetime.now())

# check whether logfile exists
# else create it
#retcode = subprocess.Popen("ls /var/log/ | grep dbmanager.log")
if subprocess.Popen("ls /var/log/ | grep dbmanager.log", shell=True) == 0:
    filename = 'var/log/dbmanager.log'
else:
    subprocess.Popen("cd /var/log/ && touch dbmanager.log", shell=True)
    filename = "/var/log/dbmanager.log"

# global width and height
globalWidth = 746
globalHeight = 269

# build the gui
root = Tk()
root.title("DBManager")
root.minsize(
    width = globalWidth,
    height = globalHeight
)

note = Notebook(root)

backgroundcolour = '#A9E2F3'
#Style().configure(root, background = backgroundcolour)
#Style().configure(note, background = backgroundcolour)

# width of note for responsiveness
widgetWidth = 650

# list of logic scripts
logics = [
    './Logik/root.py',
    './Logik/tab1database.py',
    './Logik/tab2table.py',
    './Logik/tab3mxntable.py',
    './Logik/tab4column.py',
    './Logik/tab5foreignkey.py',
    './Logik/tab6sequence.py',
    './Logik/tab7content.py',
    './Logik/tab8diagram.py'
]

# list of view scripts
views = [
    './Views/root.py',
    './Views/tab1database.py',
    './Views/tab2table.py',
    './Views/tab3mxntable.py',
    './Views/tab4column.py',
    './Views/tab5foreignkey.py',
    './Views/tab6sequence.py',
    './Views/tab7content.py',
    './Views/tab8diagram.py'
]

# import every logic script
for script in logics:
    execfile(script)

# import every view
for view in views:
    execfile(view)

# build the gui
root.mainloop()
