#!/usr/bin/env python
# -*- coding: utf-8 -*-


# add column to table
def addColumn(table, column, columntype):
    try:
        begin("Add column %s (%s) to table %s" % (column, columntype, table))
        cur.execute("alter table %s add column %s %s" % (table, column, columntype))
        commit("SUCCESS: ALTER TABLE %s ADD COLUMN %s %s;" % (table, column, columntype))
    except:
        rollback("FAILED: ALTER TABLE %s ADD COLUMN %s %s;" % (table, column, columntype))


# drop column from table
def dropColumn(table, column):
    val = tkMessageBox.askyesno(
        "Confirmation",
        "Do you really want to drop column '%s'?" % (column))
    if val:
        try:
            begin("Drop column %s from table %s" % (column, table))
            cur.execute("alter table %s drop column %s" % (table, column))
            commit("SUCCESS: ALTER TABLE %s DROP COLUMN %s;" % (table, column))
        except:
            rollback("FAILED: ALTER TABLE %s DROP COLUMN %s;" % (table, column))


# add index to specific column
def addIndex(table, column, index):

    is_unique = tkMessageBox.askyesno(
        "Confirmation",
        "Is the index unique?"
    )

    if is_unique:
        try:
            begin('Create unique index on column %s' % (colunm))
            cur.execute('create unique index %s on %s (%s)' % (index, table, column))
            commit('SUCCESS: CREATE UNIQUE INDEX %s ON %s (%s);' % (index, table, column))
        except:
            rollback('FAILED: CREATE UNIQUE INDEX %s ON %s (%s);' % (index, table, column))

    try:
        begin('Create index on column %s' % (column))
        cur.execute('create index %s on %s (%s)' % (index, table, column))
        commit('SUCCESS: CREATE INDEX %s ON %s (%s);' % (index, table, column))
    except:
        rollback('FAILED: CREATE INDEX %s ON %s (%s);' % (index, table, column))


# drop index
def dropIndex(index):
    try:
        begin('Drop index %s' % (index))
        cur.execute('drop index %s' % (index))
        commit('SUCCESS: DROP INDEX %s;' % (index))
    except:
        rollback('FAILED: DROP INDEX %s;' % (index))


# analyse specific column
def analyzeColumn(table, column):

    # get current user and database information
    database = databaseInputFields[0].get()
    user = databaseInputFields[1].get()

    try:
        begin('Analyze column %s' % (column))
        call = functions.popen("echo 'analyze verbose %s (%s);' | psql -d %s -U %s" % (table, column, database, user))
        result = call.stdout.read()

        if not result:
            raise AssertionError('FAILED: %s does not exist' % (column))

        commit('SUCCESS: ANALYZE %s;\n%s' % (column, result))
    except:
        rollback('FAILED: ANALYZE column %s;' % (column))


# vacuum specific column
def vacuumColumn(column):

    # get current user and database information
    database = databaseInputFields[0].get()
    user = databaseInputFields[1].get()

    try:
        begin('Vacuum full table %s' % (column))
        call = functions.popen("echo 'vacuum full verbose analyze %s;' | psql -d %s -U %s" % (column, database, user))
        result = call.stdout.read()

        if not result:
            raise AssertionError('FAILED: %s does not exist' % (column))

        commit('SUCCESS: VACUUM FULL VERBOSE ANALYZE %s;\n%s' % (column, result))
    except:
        rollback('FAILED: VACUUM FULL VERBOSE ANALYZE %s;' % (column))
