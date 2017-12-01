# logic for table options

# function for adding a table to current database
def addTable(table):
    try:
        begin("Add table %s" % table)
        cur.execute(
            "create table "+table+"("+
            table+"_id serial primary key, "+
            table+"_modtime timestamp with time zone, "+
            table+"_author varchar(80))"
        )
        commit("Add table %s successful" % table)
    except:
        rollback("Add table %s failed" % table)


# function for dropping a table from current database
def dropTable(table):
    val = tkMessageBox.askyesno(
        "Tabelle",
        "Tabelle wirklich loeschen?")
    if val == True:
        try:
            begin("Drop table %s" % table)
            cur.execute(
                        "drop table "+table
                        )
            commit("Drop table %s successful" % table)
        except:
            rollback("Drop table %s failed" % table)
