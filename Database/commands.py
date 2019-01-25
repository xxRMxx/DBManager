#!/usr/bin/env python
# -*- coding: utf-8 -*-

# global values for database connection
global conn
global cur
conn = ""
cur = ""

# function to open a database connection
def openDB(database, user, password, host):
    global conn
    global cur
    conn = ""
    try:
        if conn:
            conn.close()
            connection.set("not established")
        if host == "":
            if len(password) == 0:
                conn = psycopg2.connect("dbname=%s user=%s" % (database, user))
                cur = conn.cursor()
                connection.set("established (%s@%s)" % (user, database))
                writeTarget("Connection established to database %s with user %s" % (database, user))
            else:
                conn = psycopg2.connect("dbname=%s user=%s password=%s" % (database, user, password))
                cur = conn.cursor()
                connection.set("established (%s@%s)" % (user, database))
                writeTarget("Connection established to database %s with user %s" % (database, user))
        else:
            if len(password) == 0:
                conn = psycopg2.connect("dbname=%s user=%s host=%s" % (database, user, host))
                cur = conn.cursor()
                connection.set("established (%s@%s)" % (user, database))
                writeTarget("Connection established to database %s with user %s" % (database, user))
            else:
                conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s" % (database, user, password, host))
                cur = conn.cursor()
                connection.set("established (%s@%s)" % (user, database))
                writeTarget("Connection established to database %s with user %s" % (database, user))
    except:
        # call the set_connstate function here
        connection.set("not established")
        rollback("Connecting to database failed")


# function for setting the connection state
def set_connstate(*args):
    global update_in_progress
    update_in_progress = False

    if update_in_progress:
        return None

    state = 'established'
    update_in_progress = True
    #entryConnection.set(state)
    update_in_progress = False



# function for closing a database connection
def closeDB():
    if cur == "":
        root.quit()
    else:
        try:
            conn.rollback()
            conn.close()
            writeTarget("Connection closed")
            root.quit()
        except:
            rollback("Connection closed")
            sys.exit(1)
