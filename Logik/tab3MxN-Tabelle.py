# logic for mxn-tables

def addMxNTable():
    mxntablename = tab3MxNTableName.get()
    tablename1 = mxntablename.split('x')[0]
    tablename2 = mxntablename.split('x')[1]
    try:
        cur.execute("begin")
        cur.execute(
            "create table "+tablename1+"("+
            tablename1+"_id serial primary key, "+
            tablename1+"_modtime timestamp with time zone, "+
            tablename1+"_author varchar(80))"
        )
        cur.execute(
            "create table "+tablename2+"("+
            tablename2+"_id serial primary key, "+
            tablename2+"_modtime timestamp with time zone, "+
            tablename2+"_author varchar(80))"
        )
        cur.execute(
            "create table "+mxntablename+"("+
            mxntablename+"_id serial primary key, "+
            mxntablename+"_modtime timestamp with time zone, "+
            mxntablename+"_author varchar(80), "+
            mxntablename+"_"+tablename1+"_id bigint references "+
            tablename1+"("+tablename1+"_id), "+
            mxntablename+"_"+tablename2+"_id bigint references "+
            tablename2+"("+tablename2+"_id))"
        )
        cur.execute("commit")
        string = "Add mxn-table: "+mxntablename
        writeTarget(string)
        string = "Add table: "+tablename1
        writeTarget(string)
        string = "Add table: "+tablename2
        writeTarget(string)
    except:
        rollback()

def dropMxNTable():
    mxntablename = tab3MxNTableName.get()
    tablename1 = mxntablename.split('x')[0]
    tablename2 = mxntablename.split('x')[1]
    try:
        cur.execute("begin")
        cur.execute(
            "drop table "+mxntablename
        )
        cur.execute(
            "drop table "+tablename1
        )
        cur.execute(
            "drop table "+tablename2
        )
        cur.execute("commit")
        string = "Drop mxn-table: "+mxntablename
        writeTarget(string)
        string = "Drop table: "+tablename1
        writeTarget(string)
        string = "Drop table: "+tablename2
        writeTarget(string)
    except:
        rollback()