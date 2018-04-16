#!/usr/bin/env python
# -*- coding: utf-8 -*-


tab5 = Frame(note)

note.add(
    tab5,
    text = "Fremdschlüssel"
)

# lables for foreign key tab
foreignkeysDict = [
    {
        'name': 'Tabellenname',
        'y': 0
    },
    {
        'name': 'Spaltenname',
        'y': 20
    },
    {
        'name': 'Referenzierte Tabelle',
        'y': 40
    },
    {
        'name': 'Referenzielle Integrität',
        'y': 60
    }
]


# list for foreign key entry fields
foreignkeyEntryFields = []


# buttons for foreign key tab
buttons = [
    {
        'name': 'Fremdschlüssel hinzufügen',
        'command': lambda: addForeignKey(
            table = foreignkeyEntryFields[0].get(),
            column = foreignkeyEntryFields[1].get(),
            reftable = foreignkeyEntryFields[2].get(),
            fkoption = v.get()
        ),
        'x': 80,
        'y': 175,
        'width': 200,
        'height': 25
    },
    {
        'name': 'Fremdschlüssel löschen',
        'command': lambda: dropForeignKey(
            table = foreignkeyEntryFields[0].get(),
            column = foreignkeyEntryFields[1].get(),
            reftable = foreignkeyEntryFields[2].get()
        ),
        'x': 280,
        'y': 175,
        'width': 200,
        'height': 25
    }
]


# generate label specified in foreignkeysDict
for item in foreignkeysDict:
    Label(
        tab5,
        text = item['name']
    ).place(
        x = 0,
        y = item['y'],
        width = 200,
        height = 25
    )
    en = Entry(tab5)
    en.insert(0, "")
    en.place(
        x = 205,
        y = item['y'],
        width = 200,
        height = 25
    )
    foreignkeyEntryFields.append(en)



# added this for reference options
v = IntVar()
v.set("1")  # default for radio button


radiobuttons = [
    {
        'text': "Löschbeschränkung",
        'value': 1,
        'x': 200,
        'y': 100
    },
    {
        'text': "Löschweitergabe",
        'value': 2,
        'x': 200,
        'y': 120
    },
    {
        'text': "NULL bei Löschung",
        'value': 3,
        'x': 200,
        'y': 140
    }
]


for radiobutton in radiobuttons:
    tab5btnRadio = Radiobutton(
        tab5,
        text = radiobutton['text'],
        variable = v,
        value = radiobutton['value']
    ).place(
        x = radiobutton['x'],
        y = radiobutton['y']
    )


# generate buttons specified in buttons
for button in buttons:
    Button(
        tab5,
        text = button['name'],
        command = button['command']
    ).place(
        x = button['x'],
        y = button['y'],
        width = button['width'],
        height = button['height']
    )
