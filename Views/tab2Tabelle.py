# Tabellenoption

tab2 = Frame(note)
note.add(
    tab2,
    text="Tabelle"
)

tablelabel = Label(
    tab2,
    text="Tabellenname"
).grid(row=0)
tab2TableName = Entry(
    tab2,
    textvariable = StringVar()
)
tab2TableName.insert(0, "")
tab2TableName.grid(row=0, column=1)

Button(
    tab2,
    text="Tabelle anlegen",
    width=25,
    command=addTable
).grid(row=1, column=1)

Button(
    tab2,
    text="Tabelle loeschen",
    width=25,
    command=lambda: askQuestion(param="table")
).grid(row=2, column=1)

note.grid()
