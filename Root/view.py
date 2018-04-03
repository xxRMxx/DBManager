#!/usr/bin/env python
# -*- coding: utf-8 -*-


# buttons for showing db structure
menuoptions = [
    {
        'label': 'Datenbanken',
        'command': showDatabases
    },
    {
        'label': 'Benutzer',
        'command': showUsers
    },
    {
        'label': 'Tabellen',
        'command': showTables
    },
    {
        'label': 'Spalten',
        'command': showColumns
    }
]


# build application menu
menu = Menu(root)
root.config(menu = menu)

# menu option point
filemenu = Menu(menu)

menu.add_cascade(
    label = "Optionen",
    menu = filemenu
    )

submenu = Menu(menu)

filemenu.add_cascade(
    label = "Anzeigen",
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
    label = "Zurücksetzen",
    command = reset
)


filemenu.add_separator()
filemenu.add_command(
    label = "Hilfe",
    command = help
)


filemenu.add_separator()
filemenu.add_command(
    label = "Schließen",
    command = closeDB
)


# info field
textFieldInfo = Text(
    root
)
textFieldInfo.insert(END, "")
textFieldInfo.place(
    x = 545,
    y = 0,
    width = 200,
    height = 274
)
