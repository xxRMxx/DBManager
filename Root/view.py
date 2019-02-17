#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import modules for database communication and system processes
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


# check whether logfile exists; else create it
#filename = 'dbmanager.log'
logfile = 'dbmanager.log'
try:
    functions.popen('ls /var/log/ | grep %s' % (logfile))
except:
    functions.popen('touch /var/log/%s' % (logfile))

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
    './functions.py'
]


# list of view scripts
views = [
    './Database/view.py',
    './Table/view.py',
    './MxNTable/view.py',
    './Column/view.py',
    './Foreignkey/view.py',
    './Sequence/view.py',
    './Content/view.py',
    './Analyzer/view.py',
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


# build application menu
menu = Menu(root)
root.config(menu = menu)

# menu option point
filemenu = Menu(menu)

menu.add_cascade(
    label = "Options",
    menu = filemenu
)

submenu = Menu(menu)

filemenu.add_cascade(
    label = "Show",
    menu = submenu
)


# button to display all available databases
submenu.add_command(
    label = 'Databases',
    command = showDatabases
)

# display all available users
submenu.add_command(
    label = 'Users',
    command = showUsers
)

# show all tables in current db
submenu.add_command(
    label = 'Tables',
    command = showTables
)

# show all columns of given table
submenu.add_command(
    label = 'Columns',
    command = showColumns
)


filemenu.add_separator()
filemenu.add_command(
    label = 'Reset',
    command = reset
)


filemenu.add_separator()
filemenu.add_command(
    label = 'Help',
    command = help
)


##### debug option #####
if debug:
    filemenu.add_separator()
    filemenu.add_command(
        label = 'Debug',
        command = debugging
    )
########################


filemenu.add_separator()
filemenu.add_command(
    label = 'Exit',
    command = closeDB
)


# info field
label_info = Label(root, text = 'Output')
label_info.place(
    x = 250,
    y = 285,
    width = styles.label['width'],
    height = styles.label['height']
)
text_info = Text(
    root
)
text_info.insert(END, "NOTE: Connect to a database first.")
text_info.place(
    x = styles.text['x-axis'],
    y = styles.text['y-axis'],
    width = styles.text['width'],
    height = styles.text['height']
)


# run gui
root.mainloop()
