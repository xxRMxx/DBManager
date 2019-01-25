#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab6 = Frame(note)

note.add(
    tab6,
    text = "Sequence"
)


# this list contains all input fields in this tab
sequenceInputFields = []


# label and input field for sequence of table
label_sequence = Label(tab6, text = 'Table')
label_sequence.place(
    x = styles.label['x-axis'],
    y = 0,
    width = styles.label['width'],
    height = styles.label['height']
)
input_sequence = Entry(tab6)
input_sequence.insert(0, "")
input_sequence.place(
    x = 205,
    y = 0,
    width = styles.input['width'],
    height = styles.input['height']
)
sequenceInputFields.append(input_sequence)


# button to reset sequence of specified table
button_resetSequence = Button(
    tab6,
    text = 'Reset sequence',
    command = lambda: setSequence(
        table = sequenceInputFields[0].get() # input_sequence
    )
)
button_resetSequence.place(
    x = 80,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)
