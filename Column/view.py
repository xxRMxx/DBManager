#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab4 = Frame(note)

note.add(
    tab4,
    text = "Column"
)


# TODO:
# add option for nullable, index and default value

# this list contains all input fields in this tab
columnInputFields = []


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
columnInputFields.append(input_tablename)


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
columnInputFields.append(input_columnname)


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
columnInputFields.append(input_columntype)


# label and input field for index name
label_index = Label(
    tab4,
    text = 'Index'
)
label_index.place(
    x = styles.label['x-axis'],
    y = 60,
    width = styles.label['width'],
    height = styles.label['height']
)
input_index = Entry(tab4)
input_index.insert(0, "")
input_index.place(
    x = styles.input['x-axis'],
    y = 60,
    width = styles.input['width'],
    height = styles.input['height']
)
columnInputFields.append(input_index)


# button to add a column with user given type
button_addColumn = Button(
    tab4,
    text = 'Add column',
    command = lambda: addColumn(
        table = columnInputFields[0].get(), # input_tablename
        column = columnInputFields[1].get(), # input_colname
        columntype = columnInputFields[2].get() # input_columntype
    )
)
button_addColumn.place(
    x = 80,
    y = 150,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to drop column with user given information
button_deleteColumn = Button(
    tab4,
    text = 'Delete column',
    command = lambda: dropColumn(
        table = columnInputFields[0].get(), # input_tablename
        column = columnInputFields[1].get() # input_columnname
    )
)
button_deleteColumn.place(
    x = 280,
    y = 150,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to add index to specific column
button_addIndex = Button(
    tab4,
    text = 'Add index',
    command = lambda: addIndex(
        table = columnInputFields[0].get(),
        column = columnInputFields[1].get(),
        index = columnInputFields[3].get()
    )
)
button_addIndex.place(
    x = 80,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to start analysis for given table and column information
button_dropIndex = Button(
    tab4,
    text = 'Drop index',
    command = lambda: dropIndex(
        index = columnInputFields[3].get()
    )
)
button_dropIndex.place(
    x = 280,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to analyze specific column
button_analyze = Button(
    tab4,
    text = 'Analyze column',
    command = lambda: analyzeColumn(
        table = columnInputFields[0].get(),
        column = columnInputFields[1].get()
    )
)
button_analyze.place(
    x = 80,
    y = 200,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to vacuum specific column
button_vacuum = Button(
    tab4,
    text = 'Vacuuming column',
    command = lambda: vacuumColumn(
        column = columnInputFields[0].get()
    )
)
button_vacuum.place(
    x = 280,
    y = 200,
    width = styles.button['width'],
    height = styles.button['height']
)
