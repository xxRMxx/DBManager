#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Diagramoptionen

tab8 = Frame(note)

note.add(
    tab8,
    text = "Diagram"
)


# this list contains all input fields in this tab
diagramInputFields = []


# label and input field for database information
label_database = Label(tab8, text = 'Database')
label_database.place(
    x = styles.label['x-axis'],
    y = 0,
    width = styles.label['width'],
    height = styles.label['height']
)
input_database = Entry(tab8)
input_database.insert(0, "")
input_database.place(
    x = styles.input['x-axis'],
    y = 0,
    width = styles.input['width'],
    height = styles.input['height']
)
diagramInputFields.append(input_database)


# label and input field for user information
label_user = Label(tab8, text = 'User')
label_user.place(
    x = styles.label['x-axis'],
    y = 20,
    width = styles.label['width'],
    height = styles.label['height']
)
input_user = Entry(tab8)
input_user.insert(0, "")
input_user.place(
    x = styles.input['x-axis'],
    y = 20,
    width = styles.input['width'],
    height = styles.input['height']
)
diagramInputFields.append(input_user)


# label and input field for table information
label_table = Label(tab8, text = 'Table')
label_table.place(
    x = styles.label['x-axis'],
    y = 40,
    width = styles.label['width'],
    height = styles.label['height']
)
input_table = Entry(tab8)
input_table.insert(0, "")
input_table.place(
    x = styles.input['x-axis'],
    y = 40,
    width = styles.input['width'],
    height = styles.input['height']
)
diagramInputFields.append(input_table)


# button to create the diagram
button_createDiagram = Button(
    tab8,
    text = 'Create diagram',
    command = lambda: createDia(
        user = diagramInputFields[1].get(), # input_user
        table = diagramInputFields[2].get() # input_table
    )
)
button_createDiagram.place(
    x = 80,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)
