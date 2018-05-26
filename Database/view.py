#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab1 = Frame(note)

note.add(
    tab1,
    text = "Database"
)

# list of dicts for labels and entries
databaseDict = [
    {
        'name': 'Database',
        'y': 0
    },
    {
        'name': 'User',
        'y': 20
    },
    {
        'name': 'Password',
        'y': 40,
        'pw': True
    },
    {
        'name': 'Host',
        'y': 60
    }
]


databaseEntryFields = []

# loop over databaseDict
# for every label generate a label
# for every entry generate an entry field
# if dict has a key for password, show '*' instead of number/character
for item in databaseDict:
    Label(
        tab1,
        text = item['name']
    ).place(
        x = 0,
        y = item['y'],
        width = 200,
        height = 25
    )
    if 'pw' in item:
        en = Entry(tab1, show = "*")
        en.insert(0, "")
        en.place(
            x = 205,
            y = item['y'],
            width = 200,
            height = 25
        )
        databaseEntryFields.append(en)
    else:
        en = Entry(tab1)
        en.insert(0, "")
        en.place(
            x = 205,
            y = item['y'],
            width = 200,
            height = 25
        )
        databaseEntryFields.append(en)


Label(
    tab1,
    text = "Connection"
).place(
    x = 0,
    y = 100,
    width = 200,
    height = 25
)


connection = StringVar()
connection.set('not established')
entryConnection = Entry(
    tab1,
    textvariable = connection,
    state = "disabled"
)
entryConnection.place(
    x = 205,
    y = 100,
    width = 200,
    height = 25
)
connection.trace("w", set_connstate)


# generate a button for log in into database
Button(
    tab1,
    text = "Connect",
    command = lambda: openDB(
        database = databaseEntryFields[0].get(),
        user = databaseEntryFields[1].get(),
        password = databaseEntryFields[2].get(),
        host = databaseEntryFields[3].get()
    )
).place(
    x = 80,
    y = 175,
    width = 200,
    height = 25
)

note.grid(
    ipady = 125
)
