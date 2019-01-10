#!/usr/bin/env python
# -*- coding: utf-8 -*-


# add column to table
def addColumn(table, column, columntype):
    try:
        begin("Add column %s (%s) to table %s" % (column, columntype, table))
        cur.execute("alter table %s add column %s %s" % (table, column, columntype))
        commit("Add column %s (%s) to table %s successful" % (column, columntype, table))
    except:
        rollback("Add column %s to table %s failed" % (column, table))


# drop column from table
def dropColumn(table, column):
    val = tkMessageBox.askyesno(
        "Confirmation",
        "Do you really want to drop column '%s'?" % (column))
    if val:
        try:
            begin("Drop column %s from table %s" % (column, table))
            cur.execute("alter table %s drop column %s" % (table, column))
            commit("Drop column %s from table %s successful" % (column, table))
        except:
            rollback("Drop column %s from table %s failed" % (column, table))
