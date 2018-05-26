#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab3 = Frame(note)

note.add(
    tab3,
    text = "MxN-table"
)

# list for labels
mxntableDict = [
    {
        'name': 'Name',
        'y': 0
    }
]


# list for entry fields
mxntableEntryFields = []


# list for buttons
buttons = [
    {
        'name': 'Add MxN-table',
        'command': lambda: addMxNTable(
            mxntable = mxntableEntryFields[0].get()
        ),
        'x': 80,
        'y': 175,
        'width': 200,
        'height': 25
    },
    {
        'name': 'Delete MxN-table',
        'command': lambda: dropMxNTable(
            mxntable = mxntableEntryFields[0].get()
        ),
        'x': 280,
        'y': 175,
        'width': 200,
        'height': 25
    }
]


# generate label specified mxntabledict
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


# generate button specified buttons
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
