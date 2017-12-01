#!/usr/bin/env python
# -*- coding: utf-8 -*-

# logic for getting databases, users, tables, columns and other additional information

# function for logging
def writeTarget(string):
    target = open(filename, 'a')
    target.write(timestamp+": "+string+"\n")
    target.close()

def begin(string):
    cur.execute("begin")
    writeTarget(string)

def commit(string):
    cur.execute("commit")
    textFieldInfo.delete(1.0, END)
    textFieldInfo.insert(1.0, string)
    writeTarget(string)

def rollback(string):
    cur.execute("rollback")
    textFieldInfo.delete(1.0, END)
    textFieldInfo.insert(1.0, string)
    writeTarget(string)

def reset():
    # list for all entry fields in application
    entryFields = []
    # append all entry fields of every view to list
    entryFields.append(databaseEntryFields)
    entryFields.append(tableEntryFields)
    entryFields.append(mxntableEntryFields)
    entryFields.append(columnEntryFields)
    entryFields.append(foreignkeyEntryFields)
    entryFields.append(sequenceEntryFields)
    entryFields.append(contentEntryFields)
    entryFields.append(diagramEntryFields)
    # for every entry field in every view
    # delete user entry and insert an empty string
    for entries in entryFields:
        for en in entries:
            en.delete(0, END)
            en.insert(0, "")
    writeTarget("Reset user entries successful")

def help():
    # a pop up should be shown
    print "Rettung naht"


# function to show databases on system
def showDatabases():
    try:
        begin("Show available databases")
        getDatabases = cur.execute(
            "select datname from pg_database where datistemplate is False")
        databases = cur.fetchall()
        commit("success: get available databases")
        infoField = textFieldInfo.get(1.0, 'end-1c')
        if infoField == "":
            for x in databases:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
        else:
            textFieldInfo.delete(1.0, END)
            for x in databases:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
    except:
        rollback("error: getting databases")


# function to show database users
def showUsers():
    try:
        begin("Show available users")
        getUsernames = cur.execute("select usename from pg_user")
        users = cur.fetchall()
        commit("success: get available users")
        infoField = textFieldInfo.get(1.0, 'end-1c')
        if infoField == "":
            for x in users:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
        else:
            textFieldInfo.delete(1.0, END)
            for x in users:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
    except:
        rollback("error: getting users")


# function to show tables in current database
def showTables():
    databasename = databaseEntryFields[0].get()
    user = databaseEntryFields[1].get()
    infoField = textFieldInfo.get(1.0, 'end-1c')
    try:
        begin("Show available tables")
        getTablenames = cur.execute(
            "select tablename from pg_tables where pg_tables.tableowner like '%"
            +user+"'")
        tables = cur.fetchall()
        commit("success: get available tables")
        if infoField == "":
            for x in tables:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
        else:
            textFieldInfo.delete(1.0, END)
            for x in tables:
                x = x[0] + str("\n")
                textFieldInfo.insert(END, x)
    except:
        rollback("error: getting tables")


# function to show columns for given tablename
def showColumns():
    infoField = textFieldInfo.get(1.0, 'end-1c')
    tableList = [
        {'table': tableEntryFields[0]},
        {'table': columnEntryFields[0]},
        {'table': foreignkeyEntryFields[0]},
        {'table': sequenceEntryFields[0]},
        {'table': contentEntryFields[0]},
        {'table': diagramEntryFields[2]}
    ]
    for item in tableList:
        if item['table'] == "":
            textFieldInfo.delete(1.0, END)
            textFieldInfo.insert(END, "Enter table name first")
        elif item['table'] != "":
            textFieldInfo.delete(1.0, END)
            try:
                begin("Show columns of table %s" % item['table'])
                getTablenames = cur.execute(
                                            "select (column_name || ' | ' || data_type) as information from information_schema.columns where table_name like '"
                                            +item['table']+"'")
                columns = cur.fetchall()
                commit("success: getting columns of table %s" % item['table'])
                for x in columns:
                    x = x[0]+str("\n")
                    textFieldInfo.insert(END, x)
            except:
                rollback("error: getting columns of table %s" % item['table'])
        else:
            rollback("error: infoField empty or missing table")
