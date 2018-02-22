# logic for columns


# function for adding a column
def addColumn(table, column, columntype):
    try:
        begin("Add column %s (%s) to table %s" % (column, columntype, table))
        cur.execute(
            "alter table "+table+
            " add column "+column+" "+
            columntype
        )
        commit("Add column %s (%s) to table %s successful" % (column, columntype, table))
    except:
        rollback("Add column %s to table %s failed" % (column, table))


# function for dropping a column
def dropColumn(table, column):
    val = tkMessageBox.askyesno(
        "Spalte",
        "Spalte wirklich loeschen?")
    if val == True:
        try:
            begin("Drop column %s from table %s" % (column, table))
            cur.execute(
                        "alter table "+ table +
                        " drop column "+ column
                        )
            commit("Drop column %s from table %s successful" % (column, table))
        except:
            rollback("Drop column %s from table %s failed" % (column, table))
