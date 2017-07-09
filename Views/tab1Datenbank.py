# tab for database information

tab1 = Frame(note)
note.add(
    tab1,
    text="Datenbank"
)

dblabel = Label(
    tab1,
    text="Datenbankname"
).grid(row=0)
tab1DBName = Entry(
    tab1,
    textvariable = StringVar()
)
tab1DBName.insert(0, "")
tab1DBName.grid(row=0, column=1)

dblabel = Label(
    tab1,
    text="Benutzer"
).grid(row=1)
tab1UserName = Entry(
    tab1,
    textvariable = StringVar()
)
tab1UserName.insert(0, "")
tab1UserName.grid(row=1, column=1)

dblabel = Label(
    tab1,
    text="Passwort"
).grid(row=2)
tab1Password = Entry(
    tab1,
    textvariable = StringVar(),
    show='*'
)
tab1Password.insert(0, "")
tab1Password.grid(row=2, column=1)

dblabel = Label(
    tab1,
    text="Host"
).grid(row=3)
tab1Host = Entry(
    tab1,
    textvariable = StringVar()
)
tab1Host.insert(0, "")
tab1Host.grid(row=3, column=1)

Button(
    tab1,
    text="Anmelden",
    width=25,
    command=openDB
).grid(row=4, column=1)

note.grid()