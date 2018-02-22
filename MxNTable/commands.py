# logic for mxn-tables


# function for adding a mxntable in current database
def addMxNTable(mxntable):
    table1 = mxntable.split('x')[0]
    table2 = mxntable.split('x')[1]
    try:
        begin("Create mxntable %s" % mxntable)
        cur.execute(
            "create table "+table1+"("+
            table1+"_id serial primary key, "+
            table1+"_modtime timestamp with time zone, "+
            table1+"_author varchar(80))"
        )
        cur.execute(
            "create table "+table2+"("+
            table2+"_id serial primary key, "+
            table2+"_modtime timestamp with time zone, "+
            table2+"_author varchar(80))"
        )
        cur.execute(
            "create table "+mxntable+"("+
            mxntable+"_id serial primary key, "+
            mxntable+"_modtime timestamp with time zone, "+
            mxntable+"_author varchar(80), "+
            mxntable+"_"+table1+"_id bigint references "+
            table1+"("+table1+"_id), "+
            mxntable+"_"+table2+"_id bigint references "+
            table2+"("+table2+"_id))"
        )
        commit("Add table %s, table %s and mxntable %s successful" % (table1, table2, mxntable))
    except:
        rollback("Add table %s, table %s and mxntable %s failed" % table1, table2, mxntable)


# function for dropping mxntable in current database
def dropMxNTable(mxntable):
    table1 = mxntable.split('x')[0]
    table2 = mxntable.split('x')[1]
    val = tkMessageBox.askyesno(
        "MxN-Tabelle",
        "MxN-Tabelle wirklich loeschen?")
    if val == True:
        try:
            cur.execute("begin")
            cur.execute(
                        "drop table "+mxntable
                        )
            cur.execute(
                        "drop table "+table1
                        )
            cur.execute(
                        "drop table "+table2
                        )
            commit("Drop table %s, table %s and mxntable %s successful" % (table1, table2, mxntable))
        except:
            rollback("Drop table %s, table %s and mxntable %s failed" % (table1, tabl2, mxntable))
