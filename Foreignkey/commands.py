# logic for foreign keys


# function for adding a foreign key
def addForeignKey(table, column, reftable, fkoption):
    if fkoption == 1:
        try:
            begin("Add foreign key with delete restriction")
            cur.execute(
                "alter table "+table+
                " add foreign key ("+
                table+"_"+reftable+"_id) references "+reftable+
                " on delete restrict")
            commit("Add foreign key on table %s on column %s with delete restriction successful" % (table, column))
        except:
            rollback("Add foreign key on table %s on column %s with delete restriction failed" % (table, column))
    elif fkoption == 2:
        try:
            begin("Add foreign key with delete cascading")
            cur.execute(
                "alter table "+table+
                " add foreign key ("+
                table+"_"+reftable+"_id) references "+reftable+
                " on delete cascade")
            commit("Add foreign key on table %s on column %s with delete cascading successful" % (table, column))
        except:
            rollback("Add foreign key on table %s on column %s with delete cascading failed" % (table, column))
    else:
        try:
            begin("Add foreign key with delete set null constraint")
            cur.execute(
                "alter table "+table+
                " add foreign key ("+
                table+"_"+reftable+"_id) references "+reftable+
                " on delete set null"
                )
            commit("Add foreign key on table %s on column %s with on delete set null successful" % (table, column))
        except:
            rollback("Add foreign key on table %s on column %s with on delete set null failed" % (table, column))


# function for dropping a foreign key
def dropForeignKey(table, column, reftable):
    val = tkMessageBox.askyesno(
        "Fremdschluessel",
        "Fremdschluessel wirklich loeschen?")
    if val == True:
        try:
            begin("Drop foreign key for table %s on column %s" % (table, column))
            cur.execute(
                            "alter table "+table+" drop constraint "+
                            table+"_"+table+"_"+reftable+"_id_fkey"
                            )
            commit("Drop foreign key for table %s on column %s successful" % (table, column))
        except:
            rollback("Drop foreign key for table %s on column %s failed" % (table, column))
