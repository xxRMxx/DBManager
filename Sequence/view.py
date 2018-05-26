#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab6 = Frame(note)

note.add(
    tab6,
    text = "Sequence"
)


# list for labels
sequenceDict = [
    {
        'name': 'Table',
        'y': 0
    }
]


# list for sequence entry fields
sequenceEntryFields = []


# list for buttons
buttons = [
    {
        'name': 'Reset sequence',
        'command': lambda: setSequence(
            table = sequenceEntryFields[0].get()
        ),
        'x': 80,
        'y': 175,
        'width': 200,
        'height': 25
    }
]


# generate label specified in sequenceDict
for item in sequenceDict:
    Label(
        tab6,
        text = item['name']
    ).place(
        x = 0,
        y = item['y'],
        width = 200,
        height = 25
    )
    en = Entry(tab6)
    en.insert(0, "")
    en.place(
        x = 205,
        y = item['y'],
        width = 200,
        height = 25
    )
    sequenceEntryFields.append(en)


# generate button defined in buttons
for button in buttons:
    Button(
        tab6,
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
