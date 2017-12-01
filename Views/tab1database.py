# tab for database information

tab1 = Frame(note)

note.add(
    tab1,
    text = "Datenbank"
)

# list of dicts for labels and entries
databaseDict = [
    {'name': 'Datenbankname',
     'y': 0},
    {'name': 'Benutzer',
     'y': 20},
    {'name': 'Passwort',
     'y': 40,
     'pw': True},
    {'name': 'Host',
     'y': 60}
]

databaseEntryFields = []

# loop over databaseDict
# for every label generate a label
# for every entry generate an entry field
# if dict has a key for password, show '*' instead of number/character
for item in databaseDict:
    Label(
        tab1,
        text = item['name']
    ).place(
        x = 0,
        y = item['y'],
        width = 200,
        height = 25
    )
    if 'pw' in item:
        en = Entry(tab1, show = "*")
        en.insert(0, "")
        en.place(
                x = 205,
                y = item['y'],
                width = 200,
                height = 25
                )
        databaseEntryFields.append(en)
    else:
        en = Entry(tab1)
        en.insert(0, "")
        en.place(
                x = 205,
                y = item['y'],
                width = 200,
                height = 25
                )
        databaseEntryFields.append(en)

# login information
'''
# entry fields for currenct database connection
for item in databaseEntryFields:
    infodb = Entry(
                    tab1
                    #state = "readonly"
                    )
    infodb.insert(0, databaseEntryFields[0])
    infodb.grid(
            row = 0,
            column = 2
    )
    infouser = Entry(
                    tab1
                    #state = "readonly"
                    )
    infouser.insert(0, databaseEntryFields[1])
    infouser.grid(
            row = 1,
            column = 2
    )
    infologin = Entry(
                    tab1
                    #state = "readonly"
                    )
    infologin.insert(0, timestamp)
    infologin.grid(
            row = 2,
            column = 2
    )
'''

# generate a button for log in into database
Button(
    tab1,
    text = "Anmelden",
    command = lambda: openDB(
                            database = databaseEntryFields[0].get(),
                            user = databaseEntryFields[1].get(),
                            password = databaseEntryFields[2].get(),
                            host = databaseEntryFields[3].get()
                            )
    # use invoke() instead of lambda call
    ).place(
        x = 80,
        y = 175,
        width = 200,
        height = 25
)

note.grid(ipady = 125)
