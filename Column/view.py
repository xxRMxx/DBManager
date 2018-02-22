#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Spaltenoption

tab4 = Frame(note)

note.add(
    tab4,
    text = "Spalte"
)

# list for labels
columnDict = [
    {'name': 'Tabellenname',
     'y': 0},
    {'name': 'Spaltenname',
     'y': 20},
    {'name': 'Spaltentyp',
     'y': 40}
]

# list for column entries
columnEntryFields = []

buttons = [
    {'name': 'Spalte anlegen',
     'command': lambda: addColumn(
                                    table = columnEntryFields[0].get(),
                                    column = columnEntryFields[1].get(),
                                    columntype = columnEntryFields[2].get()
                                    ),
     'x': 80,
     'y': 175,
     'width': 200,
     'height': 25
     },
    {'name': 'Spalte löschen',
     'command': lambda: dropColumn(
                                    table = columnEntryFields[0].get(),
                                    column = columnEntryFields[1].get()
                                    ),
     'x': 280,
     'y': 175,
     'width': 200,
     'height': 25
     }
     ]

# loop over every label in tableLabels
for item in columnDict:
    Label(
        tab4,
        text = item['name']
    ).place(
        x = 0,
        y = item['y'],
        width = 200,
        height = 25
    )
    en = Entry(tab4)
    en.insert(0, "")
    en.place(
            x = 205,
            y = item['y'],
            width = 200,
            height = 25
            )
    columnEntryFields.append(en)

# loop over every button in buttons
for button in buttons:
    Button(
        tab4,
        text = button['name'],
        command = button['command']
    ).place(
        x = button['x'],
        y = button['y'],
        width = button['width'],
        height = button['height']
    )

note.grid()
