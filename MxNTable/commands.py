#!/usr/bin/env python
# -*- coding: utf-8 -*-


# add mxntable
def addMxNTable(mxntable):
    table1 = mxntable.split('x')[0]
    table2 = mxntable.split('x')[1]
    try:
        begin("Create mxntable %s" % (mxntable))
        cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (table1, table1, table1, table1))
        cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (table2, table2, table2, table2))
        cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80), %s_%s_id bigint references %s (%s_id), %s_%s_id bigint references %s (%s_id))" % (mxntable, mxntable, mxntable, mxntable, mxntable, table1, table1, table1, mxntable, table2, table2, table2))
        commit("Add table %s, table %s and mxntable %s successful" % (table1, table2, mxntable))
    except:
        rollback("Add table %s, table %s and mxntable %s failed" % (table1, table2, mxntable))


# drop mxntable
def dropMxNTable(mxntable):
    table1 = mxntable.split('x')[0]
    table2 = mxntable.split('x')[1]
    val = tkMessageBox.askyesno(
        "Confirmation",
        "Do you really want to drop mxn table %s?" % (mxntable))
    if val:
        try:
            cur.execute("begin")
            cur.execute("drop table %s" % (mxntable))
            cur.execute("drop table %s" % (table1))
            cur.execute("drop table %s" % (table2))
            commit("Drop table %s, table %s and mxntable %s successful" % (table1, table2, mxntable))
        except:
            rollback("Drop table %s, table %s and mxntable %s failed" % (table1, tabl2, mxntable))
