#!/usr/bin/env python
# -*- coding: utf-8 -*-


# add table
def addTable(table):

    try:
        begin("Add table %s" % (table))
        cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (table, table, table, table))
        commit("SUCCESS: CREATE TABLE %s;" % (table))
        msg = 'def addTable(): passed'
        return msg
    except:
        rollback("FAILED: CREATE TABLE %s;" % (table))
        msg = 'def addTable(): failed'
        return msg


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
            msg = 'def dropTable(): passed'
            return msg
        except:
            rollback("FAILED: DROP TABLE %s;" % (table))
            msg = 'def dropTable(): failed'
            return msg


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
        msg = 'def analyzeTable(): passed'
        return msg
    except:
        rollback('FAILED: ANALYZE %s;' % (table))
        msg = 'def analyzeTable(): failed'
        return msg


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
        msg = 'def vacuumTable(): passed'
        return msg
    except:
        rollback('FAILED: VACUUM FULL VERBOSE ANALYZE %s;' % (table))
        msg = 'def vacuumTable(): failed'
        return msg


# function for creating a diagram
def createDia(user, table):

    database = "'%s'" % (databaseInputFields[0].get())

    raise ValueError("Not supported yet.")
    dumpname = database + ".sql"
    '''
    pg_dump test -U raphael > test.sql
    cat test.sql | pf_dump2graph -n test1 -d svg
    '''
    try:
        databasedump = subprocess.Popen(
            "pg_dump -s -d %s -U %s > %s" % (database, user, dumpname),
            shell = True
        )
        writeTarget("creating dump successful")
    except: # describe to concrete exception
        writeTarget("Error in creating dump")
    time.sleep(2) # take a short nap so that the dump can be created

    try:
        subprocess.call(
            "cat %s | pf_dump2graph -n ./%s -d svg" % (dumpname, database),
            shell = True
        )
        writeTarget("creating svg file successfull")
    except:
        writeTarget("creating svg file not successfull")
