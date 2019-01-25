#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab3 = Frame(note)

note.add(
    tab3,
    text = "MxN-table"
)

# this list contains all input fields in this tab
mxntableInputFields = []


# label and input field for mxntable information
label_mxntable = Label(tab3, text = 'Name')
label_mxntable.place(
    x = styles.label['x-axis'],
    y = 0,
    width = styles.label['width'],
    height = styles.label['height']
)
input_mxntable = Entry(tab3)
input_mxntable.insert(0, "")
input_mxntable.place(
    x = 205,
    y = 0,
    width = styles.input['width'],
    height = styles.input['height']
)
mxntableInputFields.append(input_mxntable)


# display a hint
label_hint = Label(tab3, text = 'If you enter the scheme "tbl1xtbl2"\nreferrenced tables will be created automatically.')
label_hint.place(
    x = 175,
    y = 20,
    width = 360,
    height = 50
)


# button to add mxn table with given user information
button_addMxNTable = Button(
    tab3,
    text = 'Add MxN-Table',
    command = lambda: addMxNTable(
        mxntable = mxntableInputFields[0].get() # input_mxntable
    )
)
button_addMxNTable.place(
    x = 80,
    y = 175,
    width = 200,
    height = 25
)


# button to delete mxn table with given user information
button_deleteMxNTable = Button(
    tab3,
    text = 'Delete MxN-Table',
    command = lambda: dropMxNTable(
        mxntable = mxntableInputFields[0].get() # input_mxntable
    )
)
button_deleteMxNTable.place(
    x = 280,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)
