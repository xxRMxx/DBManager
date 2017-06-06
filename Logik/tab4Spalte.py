# logic for columns

def addColumn():
    tablename = tab4TableName.get()
    columnname = tab4ColumnName.get()
    columntype = tab4ColumnType.get()
    try:
        cur.execute("begin")
        cur.execute(
            "alter table "+tablename+
            " add column "+columnname+" "+
            columntype
        )
        cur.execute("commit")
        string = "Table: "+tablename+": add column: "+columnname+", "+columntype
        writeTarget(string)
    except:
        rollback()

def dropColumn():
    tablename = tab4TableName.get()
    columnname = tab4ColumnName.get()
    columntype = tab4ColumnType.get()
    try:
        cur.execute("begin")
        cur.execute(
            "alter table "+tablename+
            " drop column "+columnname
        )
        cur.execute("commit")
        string = "Table: "+tablename+": drop column: "+columnname+", "+columntype
        writeTarget(string)
    except:
        rollback()
