#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab2 = Frame(note)

note.add(
    tab2,
    text = "Tabelle"
)


# list for labels
tableDict = [
    {
        'name': 'Tabellenname',
        'y': 0
    }
]


# list for entry fields
tableEntryFields = []


# generate label defined in tableDict
for item in tableDict:
    Label(
        tab2,
        text = item['name']
    ).place(
        x = 0,
        y = item['y'],
        width = 200,
        height = 25
    )
    en = Entry(tab2)
    en.insert(0, "")
    en.place(
        x = 205,
        y = item['y'],
        width = 200,
        height = 25
    )
    tableEntryFields.append(en)


buttons = [
    {
        'name': 'Tabelle anlegen',
        'command': lambda: addTable(
            table = tableEntryFields[0].get()
        ),
        'x': 80,
        'y': 175,
        'width': 200,
        'height': 25
    },
    {
        'name': 'Tabelle löschen',
        'command': lambda: dropTable(
            table = tableEntryFields[0].get()
        ),
        'x': 280,
        'y': 175,
        'width': 200,
        'height': 25
    }
]


# generate button specified in buttons
for button in buttons:
    Button(
        tab2,
        text = button['name'],
        command = button['command']
    ).place(
        x = button['x'],
        y = button['y'],
        width = button['width'],
        height = button['height']
    )

note.grid()
