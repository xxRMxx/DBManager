#!/usr/bin/env python
# -*- coding: utf-8 -*-


# function for reset a sequence
def setSequence(table):
    try:
        begin("Restart sequence")
        cur.execute("alter sequence %s_%s_id_seq restart" % (table, table))
        commit("Restart sequence successful")
    except:
        rollback("Restart sequence failed")
