#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab7 = Frame(note)

note.add(
    tab7,
    text = "Content"
)


# list for labels
contentDict = [
    {
        'name': 'Table',
        'y': 0
    },
    {
        'name': 'Column',
        'y': 20},
    {
        'name': 'Content',
        'y': 40
    },
    {
        'name': 'Column (where clause)',
        'y': 60
    },
    {
        'name': 'Content (where clause)',
        'y': 80
    }
]

# list for content entry fields
contentEntryFields = []

buttons = [
    {
        'name': 'Insert',
        'command': lambda: insert(
            table = contentEntryFields[0].get(),
            column = contentEntryFields[1].get(),
            content = contentEntryFields[2].get(),
            column2 = contentEntryFields[3].get(),
            content2 = contentEntryFields[4].get()
        ),
        'x': 50,
        'y': 175,
        'width': 150,
        'height': 25
    },
    {
        'name': 'Update',
        'command': lambda: update(
            table = contentEntryFields[0].get(),
            column = contentEntryFields[1].get(),
            content = contentEntryFields[2].get(),
            column2 = contentEntryFields[3].get(),
            content2 = contentEntryFields[4].get()
        ),
        'x': 200,
        'y': 175,
        'width': 150,
        'height': 25
    },
    {
        'name': 'Delete',
        'command': lambda: delete(
            table = contentEntryFields[0].get(),
            column = contentEntryFields[1].get(),
            content = contentEntryFields[2].get(),
            column2 = contentEntryFields[3].get(),
            content2 = contentEntryFields[4].get()
        ),
        'x': 350,
        'y': 175,
        'width': 150,
        'height': 25
    }
]


# loop over every label in tableLabels
for item in contentDict:
    Label(
        tab7,
        text = item['name']
    ).place(
        x = 0,
        y = item['y'],
        width = 200,
        height = 25
    )
    en = Entry(tab7)
    en.insert(0, "")
    en.place(
        x = 205,
        y = item['y'],
        width = 200,
        height = 25
    )
    contentEntryFields.append(en)

# loop over every button in buttons
for button in buttons:
    Button(
        tab7,
        text = button['name'],
        width = 25,
        command = button['command']
    ).place(
        x = button['x'],
        y = button['y'],
        width = button['width'],
        height = button['height']
    )


# this button is for hiding the content until tab is fully implemented
Button(
    tab7,
    text = "Not implemented yet",
    state = DISABLED
).place(
    x = 0,
    y = 0,
    width = 600,
    height = 300
)

note.grid()
