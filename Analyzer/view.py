#!/usr/bin/env python
# -*- coding: utf-8 -*-


# check that all id-columns have an index
# check that column name is min three characters long


tab9 = Frame(note)

note.add(
    tab9,
    text = "Analyzer"
)


# this list contains all input fields in this tab
analyzerInputFields = []


# label and input field for query
label_query = Label(
    tab9,
    text = 'Query'
)
label_query.place(
    x = styles.label['x-axis'],
    y = 0,
    width = styles.label['width'],
    height = styles.label['height']
)
input_query = Entry(tab9)
input_query.insert(0, "")
input_query.place(
    x = styles.input['x-axis'],
    y = 0,
    width = styles.input['width'],
    height = styles.input['height']
)
analyzerInputFields.append(input_query)


# button to start analysis for given table and column information
button_explain = Button(
    tab9,
    text = 'Analyze query',
    command = lambda: explainAnalyze(
        query = analyzerInputFields[0].get()
    )
)
button_explain.place(
    x = 80,
    y = 150,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to validate all id-columns have an index
button_explain = Button(
    tab9,
    text = 'Validate indexing',
    command = lambda: checkIndex()
)
button_explain.place(
    x = 280,
    y = 150,
    width = styles.button['width'],
    height = styles.button['height']
)


# validate that column names are at least two characters long
button_explain = Button(
    tab9,
    text = 'Validate column length',
    command = lambda: checkColumnLength()
)
button_explain.place(
    x = 80,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


note.grid(
    row = 1,
    column = 8
)
