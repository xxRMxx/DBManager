#!/usr/bin/env python
# -*- coding: utf-8 -*-


# buttons for showing db structure
menuoptions = [
    {
        'label': 'Databases',
        'command': showDatabases
    },
    {
        'label': 'Users',
        'command': showUsers
    },
    {
        'label': 'Tables',
        'command': showTables
    },
    {
        'label': 'Columns',
        'command': showColumns
    }
]


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

# loop over options and create some buttons
for item in menuoptions:
    submenu.add_command(
        label = item['label'],
        command = item['command']
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
