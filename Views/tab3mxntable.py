#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MxN-Tabellenoption

tab3 = Frame(note)

note.add(
    tab3,
    text="MxN-Tabelle"
)

# list for labels
mxntableDict = [
    {'name': 'MxN-Tabellenname',
     'y': 0}
]

# list for entry fields
mxntableEntryFields = []

# list for buttons
buttons = [
    {'name': 'MxN-Tabelle anlegen',
     'command': lambda: addMxNTable(
                                    mxntable = mxntableEntryFields[0].get()
                                    ),
     'x': 80,
     'y': 175,
     'width': 200,
     'height': 25
    },
    {'name': 'MxN-Tabelle löschen',
     'command': lambda: dropMxNTable(
                                    mxntable = mxntableEntryFields[0].get()
                                    ),
     'x': 280,
     'y': 175,
     'width': 200,
     'height': 25
     }
     ]

# loop over every label in databaseLabels
for item in mxntableDict:
    Label(
        tab3,
        text = item['name']
    ).place(
        x = 0,
        y = item['y'],
        width = 200,
        height = 25
    )
    en = Entry(tab3)
    en.insert(0, "")
    en.place(
            x = 205,
            y = item['y'],
            width = 200,
            height = 25
            )
    mxntableEntryFields.append(en)

# loop over every button in buttons
for button in buttons:
    Button(
        tab3,
        text = button['name'],
        command = button['command']
    ).place(
        x = button['x'],
        y = button['y'],
        width = button['width'],
        height = button['height']
    )

note.grid()
