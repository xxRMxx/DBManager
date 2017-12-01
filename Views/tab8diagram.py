#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Diagramoptionen

tab8 = Frame(note)

note.add(
    tab8,
    text="Diagram"
)

# list for labels
diagramDict = [
    {'name': 'Datenbankname',
     'y': 0},
    {'name': 'Benutzer',
     'y': 20},
    {'name': 'Tabellenname',
     'y': 40}
]

# list for diagram entry fields
diagramEntryFields = []

buttons = [
    {'name': 'Diagram erzeugen',
     'command': lambda: createDia(
                                    database = diagramEntryFields[0].get(),
                                    user = diagramEntryFields[1].get(),
                                    table = diagramEntryFields[2].get()
                                    ),
     'x': 80,
     'y': 175,
     'width': 200,
     'height': 25
    }
]


# loop over every label in tableLabels
for item in diagramDict:
    Label(
        tab8,
        text = item['name']
    ).place(
            x = 0,
            y = item['y'],
            width = 200,
            height = 25
    )
    en = Entry(tab8)
    en.insert(0, "")
    en.place(
            x = 205,
            y = item['y'],
            width = 200,
            height = 25
            )
    diagramEntryFields.append(en)

# loop over every button in buttons
for button in buttons:
    Button(
        tab8,
        text = button['name'],
        width = 25,
        command = button['command']
    ).place(
        x = button['x'],
        y = button['y'],
        width = button['width'],
        height = button['height']
    )

note.grid()
