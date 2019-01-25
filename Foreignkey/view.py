#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab5 = Frame(note)

note.add(
    tab5,
    text = "Foreign key"
)


# this list contains all input fields in this tab
foreignkeyInputFields = []


# label and input field for table information
label_table = Label(tab5, text = 'Table')
label_table.place(
    x = styles.label['x-axis'],
    y = 0,
    width = styles.label['width'],
    height = styles.label['height']

)
input_table = Entry(tab5)
input_table.insert(0, "")
input_table.place(
    x = styles.input['x-axis'],
    y = 0,
    width = styles.input['width'],
    height = styles.input['height']
)
foreignkeyInputFields.append(input_table)


# label and input field for column information
label_column = Label(tab5, text = 'Column')
label_column.place(
    x = styles.label['x-axis'],
    y = 20,
    width = styles.label['width'],
    height = styles.label['height']

)
input_column = Entry(tab5)
input_column.insert(0, "")
input_column.place(
    x = styles.input['x-axis'],
    y = 20,
    width = styles.input['width'],
    height = styles.input['height']
)
foreignkeyInputFields.append(input_column)


# label and input field for referenced table information
label_reftable = Label(tab5, text = 'References table')
label_reftable.place(
    x = styles.label['x-axis'],
    y = 40,
    width = styles.label['width'],
    height = styles.label['height']

)
input_reftable = Entry(tab5)
input_reftable.insert(0, "")
input_reftable.place(
    x = styles.input['x-axis'],
    y = 40,
    width = styles.input['width'],
    height = styles.input['height']
)
foreignkeyInputFields.append(input_reftable)


# label and input field for constraint information
label_constraint = Label(tab5, text = 'Constraint')
label_constraint.place(
    x = styles.label['x-axis'],
    y = 70,
    width = styles.label['width'],
    height = styles.label['height']

)

# added this for reference options
foreignkey = IntVar()
foreignkey.set("1")  # default for radio button

button_op1 = Radiobutton(
    tab5,
    text = "Delete restrict",
    variable = foreignkey,
    value = '1'
    )
button_op1.place(
    x = 200,
    y = 70
)

button_op2 = Radiobutton(
    tab5,
    text = "Delete on cascade",
    variable = foreignkey,
    value = '2'
    )
button_op2.place(
    x = 200,
    y = 90
)

button_op3 = Radiobutton(
    tab5,
    text = "NULL on delete",
    variable = foreignkey,
    value = '3'
    )
button_op3.place(
    x = 200,
    y = 110
)
foreignkeyInputFields.append(foreignkey)


# button for adding a foreign key constraint
button_AddConstraint = Button(
    tab5,
    text = "Add foreign key constraint",
    command = lambda: addForeignKey(
        table = foreignkeyInputFields[0].get(), # input_table
        column = foreignkeyInputFields[1].get(), # input_column
        reftable = foreignkeyInputFields[2].get(), # input_reftable
        fkoption = foreignkey.get() # input_fkoption
    )
)
button_AddConstraint.place(
    x = 80,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to drop an existing foreign key constraint
button_DropConstraint = Button(
    tab5,
    text = "Drop foreign key constraint",
    command = lambda: dropForeignKey(
        table = foreignkeyInputFields[0].get(), # input_table
        column = foreignkeyInputFields[1].get(), # input_column
        reftable = foreignkeyInputFields[2].get() # input_reftable
    )
)
button_DropConstraint.place(
    x = 280,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)
