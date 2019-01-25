#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab7 = Frame(note)

note.add(
    tab7,
    text = "Content"
)


# this list contains all input fields in this tab
contentInputFields = []


# label and input field for table information
label_tablename = Label(tab7, text = 'Table')
label_tablename.place(
    x = styles.label['x-axis'],
    y = 0,
    width = styles.label['width'],
    height = styles.label['height']
)
input_tablename = Entry(tab7)
input_tablename.insert(0, "")
input_tablename.place(
    x = styles.input['x-axis'],
    y = 0,
    width = styles.input['width'],
    height = styles.input['height']
)
contentInputFields.append(input_tablename)


# label and input field for column information
label_columnname = Label(tab7, text = 'Column')
label_columnname.place(
    x = styles.label['x-axis'],
    y = 20,
    width = styles.label['width'],
    height = styles.label['height']
)
input_columnname = Entry(tab7)
input_columnname.insert(0, "")
input_columnname.place(
    x = styles.input['x-axis'],
    y = 20,
    width = styles.input['width'],
    height = styles.input['height']
)
contentInputFields.append(input_columnname)


# label and input field for content
label_content = Label(tab7, text = 'Content')
label_content.place(
    x = styles.label['x-axis'],
    y = 40,
    width = styles.label['width'],
    height = styles.label['height']
)
input_content = Entry(tab7)
input_content.insert(0, "")
input_content.place(
    x = styles.input['x-axis'],
    y = 40,
    width = styles.input['width'],
    height = styles.input['height']
)
contentInputFields.append(input_content)


# label and input field for column information (where clause)
label_wherecolumnname = Label(tab7, text = 'Column (where clause)')
label_wherecolumnname.place(
    x = styles.label['x-axis'],
    y = 60,
    width = styles.label['width'],
    height = styles.label['height']
)
input_wherecolumnname = Entry(tab7)
input_wherecolumnname.insert(0, "")
input_wherecolumnname.place(
    x = styles.input['x-axis'],
    y = 60,
    width = styles.input['width'],
    height = styles.input['height']
)
contentInputFields.append(input_wherecolumnname)


# label and input field for content (where clause)
label_wherecontent = Label(tab7, text = 'Content (where clause)')
label_wherecontent.place(
    x = styles.label['x-axis'],
    y = 80,
    width = styles.label['width'],
    height = styles.label['height']
)
input_wherecontent = Entry(tab7)
input_wherecontent.insert(0, "")
input_wherecontent.place(
    x = styles.input['x-axis'],
    y = 80,
    width = styles.input['width'],
    height = styles.input['height']
)
contentInputFields.append(input_wherecontent)


# button to start insertation in database
button_insertContent = Button(
    tab7,
    text = 'Insert',
    command = lambda: insert(
        table = contentInputFields[0].get(), # input_tablename
        column = contentInputFields[1].get(), # input_columnname
        content = contentInputFields[2].get() # input_content
    )
)
button_insertContent.place(
    x = 0,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to update data set in database
button_updateContent = Button(
    tab7,
    text = 'Update',
    command = lambda: update(
        table = contentInputFields[0].get(), # input_tablename
        column = contentInputFields[1].get(), # input_columnname
        content = contentInputFields[2].get(), # input_content
        column2 = contentInputFields[3].get(), # input_wherecolumnname
        content2 = contentInputFields[4].get() # input_wherecontent
    )
)
button_updateContent.place(
    x = 175,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)


# button to delete data set in database
button_deleteContent = Button(
    tab7,
    text = 'Delete',
    command = lambda: delete(
        table = contentInputFields[0].get(), # input_tablename
        column = contentInputFields[1].get(), # input_columnname
        content = contentInputFields[2].get(), # input_content
        column2 = contentInputFields[3].get(), # input_wherecolumnname
        content2 = contentInputFields[4].get() # input_wherecontent
    )
)
button_deleteContent.place(
    x = 350,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)



# this button is for hiding the content until tab is fully implemented
#Button(
#    tab7,
#    text = "Not implemented yet",
#    state = DISABLED
#).place(
#    x = 0,
#    y = 0,
#    width = 600,
#    height = 300
#)
