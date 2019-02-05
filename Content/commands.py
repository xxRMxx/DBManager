#!/usr/bin/env python
# -*- coding: utf-8 -*-


# function for inserting content in table
def insert(table, column, content):

    # get user from current db connection
    user = "'%s'" % (databaseInputFields[1].get())
    content = "'%s'" % (content)


    if len(content) == 0:
        string = "No content given"
        writeTarget(string)
    else:
        try:
            begin("Inserting content into table %s" % (table))
            cur.execute("insert into %s (%s_id, %s_modtime, %s_author, %s) values (default, now(), %s, %s)" % (table, table, table, table, column, user, content))
            commit("Inserting data into table %s successful" % (table))
        except:
            rollback('Inserting content not successful')


# function for updating existend data in table
def update(table, column, content, column2, content2):

    # get user from current db connection
    user = "'%s'" % (databaseInputFields[1].get())
    content = "'%s'" % (content)
    content2 = "'%s'" % (content2)

    try:
        begin("Updating content in table %s" % (table))
        cur.execute("update %s set (%s_modtime, %s_author, %s) = (now(), %s, %s) where %s = %s" % (table, table, table, column, user, content, column2, content2))
        commit("Updating content in table %s successful" % (table))
    except:
        rollback('Updating content in table %s not successful' % (table))


# function for deleting an entry in table
def delete(table, column, content, column2, content2):

    # get user from current db connection
    user = "'%s'" % (databaseInputFields[1].get())
    content = "'%s'" % (content)

    val = tkMessageBox.askyesno(
        "Confirmation",
        "Do you really want to delete the content?"
    )
    if val == True:
        tkMessageBox.showinfo("NOTE", "Remember to restart the sequence.")
        if not column2:
            try:
                begin('Clean table %s' % (table))
                cur.execute('delete from %s' % (table))
                commit('Clean table %s successful' % (table))
            except:
                rollback('Clean table %s not successful' % (table))
        else:
            try:
                begin('Delete %s from table %s' % (content, table))
                cur.execute('delete from %s where %s = %s' % (table, column2, content2))
                commit('Delete %s (%s) from table %s successful' % (content2, column2, table))
            except:
                rollback('Delete %s (%s) from table %s not successful' % (content2, column2, table))


# send custom query to database
def sendQuery(query):

    database = databaseInputFields[0].get()
    user = databaseInputFields[1].get()

    try:
        begin('Send custom query to database')
        call = functions.popen("echo '%s;' | psql %s %s" % (query, database, user))
        result = call.stdout.read()
        commit("SUCCESS: '%s';\n%s" % (query, result))
    except:
        rollback("FAILED: '%s';" % (query))
