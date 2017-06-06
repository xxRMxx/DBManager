# logic for table options

def addTable():
    tablename = tab2TableName.get()
    try:
        cur.execute("begin")
        cur.execute(
            "create table "+tablename+"("+
            tablename+"_id serial primary key, "+
            tablename+"_modtime timestamp with time zone, "+
            tablename+"_author varchar(80))"
        )
        cur.execute("commit")
        string = "Add table: "+tablename
        writeTarget(string)
    except:
        rollback()

def dropTable():
    tablename = tab2TableName.get()
    try:
        cur.execute("begin")
        cur.execute(
            "drop table "+tablename
        )
        cur.execute("commit")
        string = "Drop table: "+tablename
        writeTarget(string)
    except:
        rollback()
