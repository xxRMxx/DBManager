#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab2 = Frame(note)

note.add(
    tab2,
    text = "Table"
)


# this list contains all input fields in this tab
tableInputFields = []


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
tableInputFields.append(input_tablename)


# button to add a table with given user information
button_addTable = Button(
    tab2,
    text = 'Add table',
    command = lambda: addTable(
        table = tableInputFields[0].get() # input_tablename
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
        table = tableInputFields[0].get() # input_tablename
    )
)
button_deleteTable.place(
    x = 280,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to analyze specific table
button_analyze = Button(
    tab2,
    text = 'Analyze table',
    command = lambda: analyzeTable(
        table = tableInputFields[0].get()
    )
)
button_analyze.place(
    x = 80,
    y = 200,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to vacuum specific table
button_vacuum = Button(
    tab2,
    text = 'Vacuum table',
    command = lambda: vacuumTable(
        table = tableInputFields[0].get()
    )
)
button_vacuum.place(
    x = 280,
    y = 200,
    width = styles.button['width'],
    height = styles.button['height']
)
