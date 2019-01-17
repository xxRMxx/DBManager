#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab4 = Frame(note)

note.add(
    tab4,
    text = "Column"
)


# label and input field for table information
label_tablename = Label(
    tab4,
    text = 'Table'
)
label_tablename.place(
    x = styles.label['x-axis'],
    y = 0,
    width = styles.label['width'],
    height = styles.label['height']
)
input_tablename = Entry(tab4)
input_tablename.insert(0, "")
input_tablename.place(
    x = styles.input['x-axis'],
    y = 0,
    width = styles.input['width'],
    height = styles.input['height']
)


# label and input field for column name
label_columnname = Label(
    tab4,
    text = 'Name'
)
label_columnname.place(
    x = styles.label['x-axis'],
    y = 20,
    width = styles.label['width'],
    height = styles.label['height']
)
input_columnname = Entry(tab4)
input_columnname.insert(0, "")
input_columnname.place(
    x = styles.input['x-axis'],
    y = 20,
    width = styles.input['width'],
    height = styles.input['height']
)


# label and input field for column type
label_columntype = Label(
    tab4,
    text = 'Type'
)
label_columntype.place(
    x = styles.label['x-axis'],
    y = 40,
    width = styles.label['width'],
    height = styles.label['height']
)
input_columntype = Entry(tab4)
input_columntype.insert(0, "")
input_columntype.place(
    x = styles.input['x-axis'],
    y = 40,
    width = styles.input['width'],
    height = styles.input['height']
)


# button to add a column with user given type
button_addColumn = Button(
    tab4,
    text = 'Add column',
    command = lambda: addColumn(
        table = input_tablename.get(),
        column = input_columnname.get(),
        columntype = input_columntype.get()
    )
)
button_addColumn.place(
    x = 80,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to drop column with user given information
button_deleteColumn = Button(
    tab4,
    text = 'Delete column',
    command = lambda: dropColumn(
        table = input_tablename.get(),
        column = input_columnname.get()
    ),
)
button_deleteColumn.place(
    x = 280,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


note.grid()
