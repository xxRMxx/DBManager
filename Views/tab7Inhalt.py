# Inhaltsoption

tab7 = Frame(note)
note.add(
    tab7,
    text="Inhalt"
)

contentlabel = Label(
    tab7,
    text="Tabellenname"
).grid(row=0)
tab7TableName = Entry(
    tab7,
    textvariable = StringVar()
)
tab7TableName.insert(0, "")
tab7TableName.grid(row=0, column=1)

contentlabel = Label(
    tab7,
    text="Spaltenname"
).grid(row=1)
tab7ColumnName = Entry(
    tab7,
    textvariable = StringVar()
)
tab7ColumnName.insert(0, "")
tab7ColumnName.grid(row=1, column=1)

contentlabel = Label(
    tab7,
    text="Inhalt"
).grid(row=2)
tab7Content = Entry(
    tab7,
    textvariable = StringVar()
)
tab7Content.insert(0, "")
tab7Content.grid(row=2, column=1)

contentlabel = Label(
    tab7,
    text="WHERE-Spaltenname"
).grid(row=3)
tab7ColumnName2 = Entry(
    tab7,
    textvariable = StringVar()
)
tab7ColumnName2.insert(0, "")
tab7ColumnName2.grid(row=3, column=1)

contentlabel = Label(
    tab7,
    text="WHERE-Inhalt"
).grid(row=4)
tab7Content2 = Entry(
    tab7,
    textvariable = StringVar()
)
tab7Content2.insert(0, "")
tab7Content2.grid(row=4, column=1)

btnInsert = Button(
    tab7,
    text="Insertieren",
    width=20,
    command=insert
).grid(row=6, column=0)
btnUpdate = Button(
    tab7,
    text="Ersetzen",
    width=20,
    command=update
).grid(row=6, column=1)

btnDelete = Button(
    tab7,
    text="Loeschen",
    width=20,
    command=lambda: askQuestion(param="content")
).grid(row=6, column=2)

note.grid(ipady=25)
