#!/usr/bin/env python
# -*- coding: utf-8 -*-


# add mxntable
def addMxNTable(mxntable):

    mxn_seperator = False

    if 'x' in mxntable:
        try:
            table1 = mxntable.split('x')[0]
            table2 = mxntable.split('x')[1]

            mxn_seperator = True
        except Exception:
            mxn_seperator = False
            print('No unique seperator to create two tables automatically.')

    print(mxn_seperator)
    if mxn_seperator:
        try:
            begin("Create mxntable %s" % (mxntable))
            cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (table1, table1, table1, table1))
            cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (table2, table2, table2, table2))
            cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80), %s_id bigint references %s (%s_id), %s_id bigint references %s (%s_id))" % (mxntable, mxntable, mxntable, mxntable, table1, table1, table1, table2, table2, table2))
            commit("Add table %s, table %s and mxntable %s successful" % (table1, table2, mxntable))
        except:
            rollback("Add table %s, table %s and mxntable %s failed" % (table1, table2, mxntable))
    else:
        try:
            begin('Create mxntable %s' % (mxntable))
            cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (mxntable, mxntable, mxntable, mxntable))
            commit('Add table %s successful' % (mxntable))
        except Exception:
            rollback('Create of mxntable %s failed.' % (mxntable))


# drop mxntable
def dropMxNTable(mxntable):

    val = tkMessageBox.askyesno(
        "Confirmation",
        "Do you really want to drop mxn table %s?" % (mxntable))

    if not val:
        return False
        #return None

    mxn_seperator = False

    if 'x' in mxntable:
        try:
            table1 = mxntable.split('x')[0]
            table2 = mxntable.split('x')[1]

            mxn_seperator = True
        except Exception:
            mxn_seperator = False
            print("No unique seperator to delete two tables automatically.")


    if mxn_seperator:
        try:
            begin("Drop tables %s, %s and %s" % (table1, table2, mxntable))
            cur.execute("drop table %s" % (mxntable))
            cur.execute("drop table %s" % (table1))
            cur.execute("drop table %s" % (table2))
            commit("Drop table %s, table %s and mxntable %s successful" % (table1, table2, mxntable))
        except:
            rollback("Drop table %s, table %s and mxntable %s failed" % (table1, tabl2, mxntable))
    else:
        try:
            begin('Drop mxntable %s' % (mxntable))
            cur.execute("drop table %s" % (mxntable))
            commit('Drop mxntable %s successful' % (mxntable))
        except Exception:
            rollback('Drop mxntablel %s failed' % (mxntable))
