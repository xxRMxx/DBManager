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

    if mxn_seperator:
        try:
            begin("Create mxntable %s" % (mxntable))
            cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (table1, table1, table1, table1))
            cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (table2, table2, table2, table2))
            cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80), %s_id bigint references %s (%s_id), %s_id bigint references %s (%s_id))" % (mxntable, mxntable, mxntable, mxntable, table1, table1, table1, table2, table2, table2))
            commit("SUCCESS: CREATE TABLE %s; CREATE TABLE %s; CREATE TABLE %s;" % (mxntable, table1, table2))
            msg = 'def addMxNTable(with seperator): passed'
            return msg
        except:
            rollback("FAILED: CREATE TABLE %s;" % (mxntable))
            msg = 'def addMxNTable(with seperator): failed'
            return msg
    else:
        try:
            begin('Create mxntable %s' % (mxntable))
            cur.execute("create table %s (%s_id serial primary key, %s_modtime timestamp with time zone, %s_author varchar(80))" % (mxntable, mxntable, mxntable, mxntable))
            commit('SUCCESS: CREATE TABLE %s;' % (mxntable))
            msg = 'def addMxNTable(without seperator): passed'
            return msg
        except:
            rollback('FAILED: CREATE TABLE %s;' % (mxntable))
            msg = 'def addMxNTable(without seperator): failed'
            return msg


# drop mxntable
def dropMxNTable(mxntable):

    val = tkMessageBox.askyesno(
        "Confirmation",
        "Do you really want to drop mxn table %s?" % (mxntable))

    if not val:
        return None

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
            commit("SUCCESS: DROP TABLE %s; DROP TABLE %s; DROP TABLE %s;" % (mxntable, table1, table2))
            msg = 'def dropMxNTable(with seperator): passed'
            return msg
        except:
            rollback("FAILED: DROP TABLE %s;" % (mxntable))
            msg = 'def dropMxNTable(with seperator): failed'
            return msg
    else:
        try:
            begin('Drop mxntable %s' % (mxntable))
            cur.execute("drop table %s" % (mxntable))
            commit('SUCCESS: DROP TABLE %s' % (mxntable))
            msg = 'def dropMxNTable(without seperator): passed'
            return msg
        except:
            rollback('FAILED: DROP TABLE %s' % (mxntable))
            msg = 'def dropMxNTable(without seperator): failed'
            return msg
