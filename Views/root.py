#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

submenu.add_command(
    label = "Datenbanken",
    command = showDatabases
)

submenu.add_command(
    label = "Benutzer",
    command = showUsers
)

submenu.add_command(
    label = "Tabellen",
    command = showTables
)

submenu.add_command(
    label = "Spalten",
    command = showColumns
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
