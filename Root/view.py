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
    label = 'Reset',
    command = reset
)


filemenu.add_separator()
filemenu.add_command(
    label = 'Help',
    command = help
)


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
