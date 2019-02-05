#!/usr/bin/env python
# -*- coding: utf-8 -*-


def reset():

    # list for all input fields in application
    entryFields = []

    # append all input fields of every view to list
    entryFields.append(databaseInputFields)
    entryFields.append(tableInputFields)
    entryFields.append(mxntableInputFields)
    entryFields.append(columnInputFields)
    entryFields.append(foreignkeyInputFields)
    entryFields.append(sequenceInputFields)
    entryFields.append(contentInputFields)
    entryFields.append(analyzerInputFields)
    entryFields.append(diagramInputFields)

    # loop over every input field and clear it
    for entry in entryFields:
        for item in entry:
            try:
                item.delete(0, END)
                item.insert(0, '')
            except AttributeError:
                # pass when input field is of type option menu
                pass

    writeTarget("Reset user entries successful")


def help():
    # a pop up should be shown
    print "Hold on. Rescue will be implemented soon."


# show databases
def showDatabases(event = None):

    # functions needs an event argument to handle keyboard shortcut (e.g. <F1>)

    try:
        begin("Show available databases")
        getDatabases = cur.execute("select datname from pg_database where datistemplate is False")
        databases = cur.fetchall()
        commit("SUCCESS: get available databases")

        text_info.delete(1.0, END)
        text_info.insert(END, 'DATABASES: \n')

        for database in databases:
            database = "%s\n" % (database)
            text_info.insert(END, database)

    except:
        rollback("FAILED: get databases")


# show database users
def showUsers(event = None):

    # functions needs an event argument to handle keyboard shortcut (e.g. <F2>)

    try:
        begin("Show available users")
        getUsernames = cur.execute("select usename from pg_user")
        users = cur.fetchall()
        commit("success: get available users")

        text_info.delete(1.0, END)
        text_info.insert(END, 'USERS: \n')

        for user in users:
            user = "%s\n" % (user)
            text_info.insert(END, user)

    except:
        rollback("FAILED: get users")


# show tables in current database
def showTables(event = None):

    # functions needs an event argument to handle keyboard shortcut (e.g. <F3>)

    databasename = databaseInputFields[0].get()
    user = databaseInputFields[1].get()


    try:
        begin("Show available tables")
        getTablenames = cur.execute("select tablename from pg_tables where pg_tables.tableowner like '%s'" % (user))
        tables = cur.fetchall()
        commit("success: get available tables")

        text_info.delete(1.0, END)
        text_info.insert(END, 'TABLES: \n')

        for table in tables:
                table = "%s\n" % (table)
                text_info.insert(END, table)

    except:
        rollback("FAILED: No tables in current database found")


# show columns for given tablename
def showColumns(event = None):

    # functions needs an event argument to handle keyboard shortcut (e.g. <F4>)

    info = text_info.get(1.0, 'end-1c')
    table = tableInputFields[0].get()

    if table == "":
        text_info.delete(1.0, END)
        text_info.insert(END, "NOTE: Insert table name in tab <table> first")
    else:
        try:

            begin("Show columns of table %s" % (table))
            getTablenames = cur.execute("select (column_name || ' (' || data_type || ')') as information from information_schema.columns where table_name = '%s'" % (table))
            columns = cur.fetchall()
            commit("SUCCESS: get columns of table %s" % (table))

            text_info.delete(1.0, END)
            text_info.insert(END, 'COLUMNS: \n')

            for column in columns:
                column = "%s\n" % (column)
                text_info.insert(END, column)
        except:
            rollback("FAILED: %s contains no columns" % (table))
