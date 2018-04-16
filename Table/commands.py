#!/usr/bin/env python
# -*- coding: utf-8 -*-


# add table
def addTable(table):
    try:
        begin("Add table %s" % (table))
        cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (table, table, table, table))
        commit("Add table %s successful" % (table))
    except:
        rollback("Add table %s failed" % (table))


# drop table
def dropTable(table):
    val = tkMessageBox.askyesno(
        "Tabelle",
        "Tabelle wirklich loeschen?"
    )

    if val:
        try:
            begin("Drop table %s" % (table))
            cur.execute("drop table %s" % (table))
            commit("Drop table %s successful" % (table))
        except:
            rollback("Drop table %s failed" % (table))
