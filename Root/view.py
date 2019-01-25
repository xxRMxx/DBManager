#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
    label = "Reset",
    command = reset
)


filemenu.add_separator()
filemenu.add_command(
    label = "Help",
    command = help
)


filemenu.add_separator()
filemenu.add_command(
    label = "Exit",
    command = closeDB
)


# info field
textFieldInfo = Text(
    root
)
textFieldInfo.insert(END, "")
textFieldInfo.place(
    x = 561,
    y = 0,
    width = 200,
    height = 274
)
