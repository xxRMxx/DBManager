#!/usr/bin/env python
# -*- coding: utf-8 -*-

# check that all id-columns have an index
# check that column name is min three characters long (_id is ok)


# analyze query on performance
def explainAnalyze(query):

    # get current user and database information
    database = databaseInputFields[0].get()
    user = databaseInputFields[1].get()

    try:
        begin("Analyse query '%s'" % (query))
        call = functions.popen("echo 'explain analyze %s;' | psql %s %s" % (query, database, user))
        result = call.stdout.read()
        commit("SUCCESS: EXPLAIN ANALYZE '%s';\n%s" % (query, result))
    except:
        rollback("FAILED: EXPLAIN ANALYZE '%s';" % (query))
