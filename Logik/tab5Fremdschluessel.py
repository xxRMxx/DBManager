# logic for foreign keys

def addForeignKey():
    tablename = tab5TableName.get()
    columnname = tab5ColumnName.get()
    reftablename = tab5RefTableName.get()
    try:
        cur.execute("begin")
        cur.execute(
            "alter table "+tablename+
            " add foreign key ("+
            tablename+"_"+reftablename+"_id) references "+reftablename
        )
        cur.execute("commit")
        string = "Table: "+tablename+": add constraint on: "+columnname
        writeTarget(string)
    except:
        rollback()

def dropForeignKey():
    tablename = tab5TableName.get()
    columnname = tab5ColumnName.get()
    reftablename = tab5RefTableName.get()
    try:
        cur.execute("begin")
        cur.execute(
            "alter table "+tablename+" drop constraint "+
            tablename+"_"+tablename+"_"+reftablename+"_id_fkey"
        )
        cur.execute("commit")
        string = "Table: "+tablename+": drop constraint on: "+columnname
        writeTarget(string)
    except:
        rollback()
