#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab2 = Frame(note)

note.add(
    tab2,
    text = "Table"
)


# label and input field for table name
label_tablename = Label(
    tab2,
    text = 'Name'
)
label_tablename.place(
    x = styles.label['x-axis'],
    y = 0,
    width = styles.label['width'],
    height = styles.label['height']
)
input_tablename = Entry(tab2)
input_tablename.insert(0, "")
input_tablename.place(
    x = styles.input['x-axis'],
    y = 0,
    width = styles.input['width'],
    height = styles.input['height']
)


# button to add a table with given user information
button_addTable = Button(
    tab2,
    text = 'Add table',
    command = lambda: addTable(
        table = input_tablename.get()
    )
)
button_addTable.place(
    x = 80,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to drop a table with given information
button_deleteTable = Button(
    tab2,
    text = 'Delete table',
    command = lambda: dropTable(
        table = input_tablename.get()
    )
)
button_deleteTable.place(
    x = 280,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


note.grid()
