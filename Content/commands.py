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
            commit("SUCCESS: INSERT INTO %s (%s_id, %s_modtime, %s_author, %s) VALUES (default, now(), %s, %s);" % (table, table, table, table, column, user, content))
            msg = 'def insert(): passed'
            return msg
        except:
            rollback("FAILED: INSERT INTO %s (%s_id, %s_modtime, %s_author, %s) VALUES (default, now(), %s, %s);" % (table, table, table, table, column, user, content))
            msg = 'def insert(): failed'
            return msg


# function for updating existend data in table
def update(table, column, content, column2, content2):

    # get user from current db connection
    user = "'%s'" % (databaseInputFields[1].get())
    content = "'%s'" % (content)
    content2 = "'%s'" % (content2)

    try:
        begin("Updating content in table %s" % (table))
        cur.execute("update %s set (%s_modtime, %s_author, %s) = (now(), %s, %s) where %s = %s" % (table, table, table, column, user, content, column2, content2))
        commit("SUCCESS: UPDATE %s SET (%s_modtime, %s_author, %s) = (now(), %s, %s) WHERE %s = %s;" % (table, table, table, column, user, content, column2, content2))
        msg = 'def update(): passed'
        return msg
    except:
        rollback("FAILED: UPDATE %s SET (%s_modtime, %s_author, %s) = (now(), %s, %s) WHERE %s = %s;" % (table, table, table, column, user, content, column2, content2))
        msg = 'def update(): failed'
        return msg


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
                commit('SUCCESS: DELETE FROM %s;' % (table))
                msg = 'def delete(all): passed'
                return msg
            except:
                rollback('FAILED: DELETE FROM %s;' % (table))
                msg = 'def delete(all): failed'
                return msg
        else:
            try:
                begin('Delete %s from table %s' % (content, table))
                cur.execute("delete from %s where %s = '%s'" % (table, column2, content2))
                commit('SUCCESS: DELETE FROM %s WHERE %s = "%s";' % (table, column2, content2))
                msg = 'def delete(where): passed'
                return msg
            except:
                rollback('FAILED: DELETE FROM %s WHERE %s = "%s";' % (table, column2, content2))
                msg = 'def delete(where): failed'
                return msg


# send custom query to database
def sendQuery(query):

    database = databaseInputFields[0].get()
    user = databaseInputFields[1].get()

    try:
        begin('Send custom query to database')
        call = functions.popen("echo '%s;' | psql %s %s" % (query, database, user))
        result = call.stdout.read()
        commit("SUCCESS: '%s';\n%s" % (query, result))
        msg = 'def sendQuery(): passed'
        return msg
    except:
        rollback("FAILED: '%s';" % (query))
        msg = 'def sendQuery(): failed'
        return msg
