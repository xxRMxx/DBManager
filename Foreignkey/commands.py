#!/usr/bin/env python
# -*- coding: utf-8 -*-


# add foreign key
def addForeignKey(table, column, reftable, fkoption):
    if fkoption == 1:
        try:
            begin("Add foreign key with delete restriction")
            cur.execute("alter table %s add foreign key (%s_%s_id) references %s on delete restrict" % (table, table, reftable, reftable))
            commit("Add foreign key on table %s on column %s with delete restriction successful" % (table, column))
        except:
            rollback("Add foreign key on table %s on column %s with delete restriction failed" % (table, column))
    elif fkoption == 2:
        try:
            begin("Add foreign key with delete cascading")
            cur.execute("alter table %s add foreign key (%s_%s_id) references %s on delete cascade" % (table, table, reftable, reftable))
            commit("Add foreign key on table %s on column %s with delete cascading successful" % (table, column))
        except:
            rollback("Add foreign key on table %s on column %s with delete cascading failed" % (table, column))
    else:
        try:
            begin("Add foreign key with delete set null constraint")
            cur.execute("alter table %s add foreign key (%s_%s_id) references %s on delete set null" % (table, table, reftable, reftable))
            commit("Add foreign key on table %s on column %s with on delete set null successful" % (table, column))
        except:
            rollback("Add foreign key on table %s on column %s with on delete set null failed" % (table, column))


# drop foreign key
def dropForeignKey(table, column, reftable):
    val = tkMessageBox.askyesno(
        "Confirmation",
        "Do you really want to drop foreign key %s_%s_id?" % (table, reftable)
    )

    if val:
        try:
            begin("Drop foreign key for table %s on column %s" % (table, column))
            cur.execute("alter table %s drop constraint %s_%s_%s_id_fkey" % (table, table, table, reftable))
            commit("Drop foreign key for table %s on column %s successful" % (table, column))
        except:
            rollback("Drop foreign key for table %s on column %s failed" % (table, column))
