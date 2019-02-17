#!/usr/bin/env python
# -*- coding: utf-8 -*-


# add foreign key
def addForeignKey(table, column, reftable, fkoption):
    if fkoption == 1:
        try:
            begin("Add foreign key with delete restriction")
            cur.execute("alter table %s add foreign key (%s) references %s on delete restrict" % (table, column, reftable))
            commit("SUCCESS: ALTER TABLE %s ADD FOREIGN KEY (%s) REFERENCES %s ON DELETE RESTRICT;" % (table, column, reftable))
            msg = 'def addForeignKey(1): passed'
            return msg
        except:
            rollback("FAILED: ALTER TABLE %s ADD FOREIGN KEY (%s) REFERENCES %s ON DELETE RESTRICT;" % (table, column, reftable))
            msg = 'def addForeignKey(1): failed'
            return msg
    elif fkoption == 2:
        try:
            begin("Add foreign key with delete cascading")
            cur.execute("alter table %s add foreign key (%s) references %s on delete cascade" % (table, column, reftable))
            commit("SUCCESS: ALTER TABLE %s ADD FOREIGN KEY (%s) REFERENCES %s ON DELETE CASCADE;" % (table, column, reftable))
            msg = 'def addForeignKey(2): passed'
            return msg
        except:
            rollback("FAILED: ALTER TABLE %s ADD FOREIGN KEY (%s) REFERENCES %s ON DELETE CASCADE;" % (table, column, reftable))
            msg = 'def addForeignKey(2): failed'
            return msg
    else:
        try:
            begin("Add foreign key with delete set null constraint")
            cur.execute("alter table %s add foreign key (%s) references %s on delete set null" % (table, column, reftable))
            commit("SUCCESS: ALTER TABLE %s ADD FOREIGN KEY (%s) REFERENCES %s ON DELETE SET NULL;" % (table, column, reftable))
            msg = 'def addForeignKey(3): passed'
            return msg
        except:
            rollback("FAILED: ALTER TABLE %s ADD FOREIGN KEY (%s) REFERENCES %s ON DELETE SET NULL;" % (table, column, reftable))
            msg = 'def addForeignKey(3): failed'
            return msg


# drop foreign key
def dropForeignKey(table, column, reftable):
    val = tkMessageBox.askyesno(
        "Confirmation",
        "Do you really want to drop foreign key %s_id?" % (reftable)
    )

    if val:
        try:
            begin("Drop foreign key for table %s on column %s" % (table, column))
            cur.execute("alter table %s drop constraint %s_%s_fkey" % (table, table, column))
            commit("SUCCESS: ALTER TABLE %s DROP CONSTRAINT %s_%s_fkey;" % (table, table, column))
            msg = 'def dropForeignKey(): passed'
            return msg
        except:
            rollback("FAILED: ALTER TABLE %s DROP CONSTRAINT %s_%s_fkey;" % (table, table, column))
            msg = 'def dropForeignKey(): failed'
            return msg
