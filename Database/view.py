#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab1 = Frame(note)

note.add(
    tab1,
    text = "Database"
)


# this list contains all input fields in this tab
databaseInputFields = []


# label and input field for database information
label_db = Label(tab1, text = "Database")
label_db.place(
    x = styles.label['x-axis'],
    y = 0,
    width = styles.label['width'],
    height = styles.label['height']
)
input_db = Entry(tab1)
input_db.insert(0, "")
input_db.place(
    x = styles.input['x-axis'],
    y = 0,
    width = styles.input['width'],
    height = styles.input['height']
)
databaseInputFields.append(input_db)


# label and input field for user information
user_label = Label(tab1, text = "User")
user_label.place(
    x = styles.label['x-axis'],
    y = 20,
    width = styles.label['width'],
    height = styles.label['height']
)
input_user = Entry(tab1)
input_user.insert(0, "")
input_user.place(
    x = styles.input['x-axis'],
    y = 20,
    width = styles.input['width'],
    height = styles.input['height']
)
databaseInputFields.append(input_user)


# label and input field for password
pw_label = Label(tab1, text = "Password")
pw_label.place(
    x = styles.label['x-axis'],
    y = 40,
    width = styles.label['width'],
    height = styles.label['height']
)
input_pw = Entry(tab1, show = '*')
input_pw.insert(0, "")
input_pw.place(
    x = styles.input['x-axis'],
    y = 40,
    width = styles.input['width'],
    height = styles.input['height']
)
databaseInputFields.append(input_pw)


# label and input field for host information
host_label = Label(tab1, text = "Host")
host_label.place(
    x = styles.label['x-axis'],
    y = 60,
    width = styles.label['width'],
    height = styles.label['height']
)
input_host = Entry(tab1)
input_host.insert(0, "")
input_host.place(
    x = styles.input['x-axis'],
    y = 60,
    width = styles.input['width'],
    height = styles.input['height']
)
databaseInputFields.append(input_host)


# label and input field for the connection status
connection_label = Label(tab1, text = "Connection")
connection_label.place(
    x = styles.label['x-axis'],
    y = 100,
    width = styles.label['width'],
    height = styles.label['height']
)
connection = StringVar()
connection.set('not established')
input_connection = Entry(
    tab1,
    textvariable = connection,
    state = "disabled"
)
input_connection.place(
    x = styles.input['x-axis'],
    y = 100,
    width = 300,
    height = styles.input['height']
)
connection.trace("w", set_connstate)


# generate a button for login into database
connection_button = Button(
    tab1,
    text = "Connect",
    command = lambda: openDB(
        database = databaseInputFields[0].get(), # input_database
        user = databaseInputFields[1].get(), # input_user
        password = databaseInputFields[2].get(), # input_password
        host = databaseInputFields[3].get() # input_host
    )
)
connection_button.place(
    x = 80,
    y = 175,
    width = styles.button['width'],
    height = styles.button['height']
)



# for debugging only
if debug:

    database = ''
    user = ''
    password = ''
    host = ''

    # fill the input fields with debugging values
    input_db.insert(0, database)
    input_user.insert(0, user)
    input_pw.insert(0, password)
    input_host.insert(0, host)

    connection_button = Button(
        tab1,
        text = "DEBUG: Connect",
        command = lambda: openDB(
            database = database,
            user = user,
            password = password,
            host = host
        )
    )
    connection_button.place(
        x = 280,
        y = 175,
        width = styles.button['width'],
        height = styles.button['height']
    )


note.grid(
    ipady = 125
)
