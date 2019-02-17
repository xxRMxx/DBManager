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
        msg = 'def showUsers(): passed'
        return msg
    except:
        rollback("FAILED: get users")
        msg = 'def showUsers(): failed'
        return msg


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
        msg = 'def showTables(): passed'
        return msg
    except:
        rollback("FAILED: No tables in current database found")
        msg = 'def showTables(): failed'
        return msg


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
            msg = 'def showColumns(): passed'
            return msg
        except:
            rollback("FAILED: %s contains no columns" % (table))
            msg = 'def showColumns(): failed'
            return msg


# debug option: call every statement to test application's functionality
def debugging():

    # test table information
    test_table1 = 'debugTable01'
    test_table2 = 'debugTable02'

    # test column information
    test_columnname1 = 'debugTable01_name'
    test_columntype1 = 'varchar(255)'
    test_columnname2 = 'debugTable02_debugTable01_id'
    test_columntype2 = 'bigint'
    index = 'testindex'

    # test mxntable information
    test_mxntablename1 = 'debugTable03xdebugTable04'
    test_mxntablename2 = 'autostorage'

    # test content
    content1 = 'Testcontent'
    content2 = 'Testcontent2'
    wherecolumnname = test_columnname1
    query = 'select * from debugTable01 order by 1 desc limit 1000'

    # list for the test results
    results = []

    # first call all additive functions
    result1 = addTable(test_table1)
    results.append(result1)
    result2 = addTable(test_table2)
    results.append(result2)

    result3 = analyzeTable(test_table1)
    results.append(result3)
    result4 = vacuumTable(test_table1)
    results.append(result4)

    result5 = addColumn(test_table1, test_columnname1, test_columntype1)
    results.append(result5)
    result29 = addColumn(test_table2, test_columnname2, test_columntype2)
    results.append(result29)
    result6 = addIndex(test_table1, test_columnname1, index)
    results.append(result6)
    result7 = analyzeColumn(test_table1, test_columnname1)
    results.append(result7)

    # call this function with all three foreign key options
    result9 = addForeignKey(test_table2, test_columnname2, test_table1, 1)
    results.append(result9)
    result25 = dropForeignKey(test_table2, test_columnname2, test_table1)
    results.append(result25)

    result10 = addForeignKey(test_table2, test_columnname2, test_table1, 2)
    results.append(result10)
    result26 = dropForeignKey(test_table2, test_columnname2, test_table1)
    results.append(result26)

    result11 = addForeignKey(test_table2, test_columnname2, test_table1, 3)
    results.append(result11)
    result27 = dropForeignKey(test_table2, test_columnname2, test_table1)
    results.append(result27)

    # first create a mxntable with 'x' seperator
    result12 = addMxNTable(test_mxntablename1)
    results.append(result12)

    # afterwards create a mxntable without 'x'seperator
    result13 = addMxNTable(test_mxntablename2)
    results.append(result13)

    result14 = insert(test_table1, test_columnname1, content1)
    results.append(result14)
    result15 = update(test_table1, test_columnname1, content2, wherecolumnname, content1)
    results.append(result15)
    result16 = delete(test_table1, test_columnname1, content2, wherecolumnname, content1)
    results.append(result16)

    result20 = setSequence(test_table1)
    results.append(result20)

    result17 = sendQuery(query)
    results.append(result17)
    result18 = explainAnalyze(query)
    results.append(result18)


    # afterwards call all destructive functions
    result21 = dropIndex(index)
    results.append(result21)
    result22 = dropColumn(test_table1, test_columnname1)
    results.append(result22)

    result23 = dropMxNTable(test_mxntablename1)
    results.append(result23)
    result24 = dropMxNTable(test_mxntablename2)
    results.append(result24)

    result30 = dropTable(test_table2)
    results.append(result30)
    result19 = dropTable(test_table1)
    results.append(result19)

    # print all test results to command line
    passed = []
    failed = []
    for result in results:
        if 'passed' in result:
            passed.append(result)
        else:
            failed.append(result)

    print('\n##### TEST RESULTS: #####')
    print('PASSED')
    for test in passed:
        print(test)
    print('FAILED')
    for test in failed:
        print(test)
