# logic for content mangement

def insert():
    tablename = tab7TableName.get()
    columnname = tab7ColumnName.get()
    content = tab7Content.get()
    columnlist = columnname.split(", ")
    contentlist = content.split(", ")
    columnlist2 = []
    for item in columnlist:
        item = ", "+item
        columnlist2.append(item)
    column = ''.join(columnlist2)
    contentlist2 = []
    for item in contentlist:
        item = ", "+"'"+str(item)+"'"
        contentlist2.append(item)
    content = ''.join(contentlist2)
    if len(content) == 0:
        string = "No content given"
        writeTarget(string)
    else:
        try:
            cur.execute("begin")
            cur.execute(
                "insert into "+
                tablename+" ("+
                tablename+"_id, "+
                tablename+"_modtime, "+
                tablename+"_author"+
                column+") values (default, now(), '"+
                user+"'"+
                content+")"
            )
            cur.execute("commit")
            string = "Table: "+tablename+": insert new content in: "+tablename
            writeTarget(string)
        except:
            rollback()

def update():
    tablename = tab7TableName.get()
    columnname = tab7ColumnName.get()
    content = tab7Content.get()
    columnname2 = tab7ColumnName2.get()
    content2 = tab7Content2.get()
    try:
        content = int(content)
    except:
        content = str(content)
    try:
        content2 = int(content2)
    except:
        content2 = str(content2)
    if type(content2) == int:
        try:
            cur.execute("begin")
            cur.execute(
                "update "+tablename+
                " set "+columnname+" = '"+
                content+"' where "+
                columnname2+" = "+str(content2)
            )
            cur.execute("commit")
            string = "Update "+tablename+" set "+columnname+" = '"
            +content+"' where "+columnname2+" = "+str(content2)
            writeTarget(string)
        except:
            rollback()
    else:
        try:
            cur.execute("begin")
            cur.execute(
                "update "+tablename+
                " set "+columnname+" = '"+
                content+"' where "+
                columnname2+" like '"+content2+"'"
            )
            cur.execute("commit")
            string = "update "+tablename+" set "+columnname+" = '"
            +content+"' where "+columnname2+" like '"+content2+"'"
            writeTarget(string)
        except:
            rollback()

def delete():
    tablename = tab7TableName.get()
    columnname = tab7ColumnName2.get()
    content = tab7Content2.get()
    columnlist = columnname.split(", ")
    contentlist = content.split(", ")
    columnlist2 = []
    if len(columnlist) == 1:
        for item in columnlist:
            item ="'"+tablename+"_"+str(item)+"'"
            columnlist2.append(item)
    column = ''.join(columnlist2)
    contentlist2 = []
    for item in contentlist:
        item = "'"+str(item)+"'"
        contentlist2.append(item)
    content = ''.join(contentlist2)
    if len(columnname) == 0:
        try:
            cur.execute("begin")
            cur.execute("delete from "+tablename)
            cur.execute("commit")
            string = "Clear table: "+tablename
            writeTarget(string)
        except:
            rollback()
    else:
        if '_id' in column:
            try:
                cur.execute("begin")
                cur.execute(
                    "delete from "+
                    tablename+" where "+
                    columnname+" = "+content
                )
                cur.execute("commit")
                string = "delete from "+tablename+" where "+columnname+" = "+content
                writeTarget(string)
            except:
                rollback()
        else:
            try:
                cur.execute("begin")
                cur.execute(
                    "delete from "+tablename+
                    " where "+
                    columnname+" like "+content)
                cur.execute("commit")
                string = "delete from "+tablename+" where "+columnname+" like "+content
                writeTarget(string)
            except:
                rollback()
