#!/usr/bin/env python
# -*- coding: utf-8 -*-


# add table
def addTable(table):

    try:
        begin("Add table %s" % (table))
        cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (table, table, table, table))
        commit("SUCCESS: CREATE TABLE %s;" % (table))
    except:
        rollback("FAILED: CREATE TABLE %s;" % (table))


# drop table
def dropTable(table):
    val = tkMessageBox.askyesno(
        "Confirmation",
        "Do you really want to drop table %s?" % (table)
    )

    if val:
        try:
            begin("Drop table %s" % (table))
            cur.execute("drop table %s" % (table))
            commit("SUCCESS: DROP TABLE %s;" % (table))
        except:
            rollback("FAILED: DROP TABLE %s;" % (table))


# analyse specific table
def analyzeTable(table):

    # get current user and database information
    database = databaseInputFields[0].get()
    user = databaseInputFields[1].get()

    try:
        begin('Analyze table %s' % (table))
        call = functions.popen("echo 'analyze verbose %s;' | psql -d %s -U %s" % (table, database, user))
        result = call.stdout.read()

        if not result:
            raise AssertionError('FAILED: %s does not exist' % (table))

        commit('SUCCESS: ANALYZE %s;\n%s' % (table, result))
    except:
        rollback('FAILED: ANALYZE %s;' % (table))


# vacuum specific table
def vacuumTable(table):

    # get current user and database information
    database = databaseInputFields[0].get()
    user = databaseInputFields[1].get()

    try:
        begin('Vacuum full table %s' % (table))
        call = functions.popen("echo 'vacuum full verbose analyze %s;' | psql -d %s -U %s" % (table, database, user))
        result = call.stdout.read()

        if not result:
            raise AssertionError('FAILED: %s does not exist' % (table))

        commit('SUCCESS: VACUUM FULL VERBOSE ANALYZE %s;\n%s' % (table, result))
    except:
        rollback('FAILED: VACUUM FULL VERBOSE ANALYZE %s;' % (table))
