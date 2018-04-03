#!/usr/bin/env python
# -*- coding: utf-8 -*-


# function for inserting content in table
def insert(table, column, content, column2, content2):
    columnlist = column.split(", ")
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
            begin("Inserting content into table %s" % table)
            cur.execute(
                "insert into "+
                table+" ("+
                table+"_id, "+
                table+"_modtime, "+
                table+"_author"+
                column+") values (default, now(), '"+
                user+"'"+
                content+")"
            )
            commit("Inserting data into table %s successful" % table)
        except:
            rollback('Inserting content not successful')


# function for updating existend data in table
def update(table, column, content, column2, content2):
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
            begin("Updating content in table %s" % table)
            cur.execute(
                "update "+table+
                " set "+column+" = '"+
                content+"' where "+
                column2+" = "+str(content2)
            )
            commit("Updating content in table %s successful" % table)
        except:
            rollback('Updating content in table %s not successful' % table)
    else:
        try:
            begin("Updating content in table %s" % table)
            cur.execute(
                "update "+table+
                " set "+column+" = '"+
                content+"' where "+
                column2+" like '"+content2+"'"
            )
            commit("Updating content in table %s successful" % table)
        except:
            rollback('Updating content for table %s not successful' % table)


# function for deleting an entry in table
def delete(table, column, content, column2, content2):
    columnlist = column.split(", ")
    contentlist = content.split(", ")
    columnlist2 = []
    val = tkMessageBox.askyesno(
        "Inhalt",
        "Inhalt wirklich loeschen?")
    if val == True:
        tkMessageBox.showinfo(
            "HINWEIS",
            "Nicht vergessen die Sequenz zurueckzusetzen")
        if len(columnlist) == 1:
            for item in columnlist:
                item ="'"+table+"_"+str(item)+"'"
                columnlist2.append(item)
        column = ''.join(columnlist2)
        contentlist2 = []
        for item in contentlist:
            item = "'"+str(item)+"'"
            contentlist2.append(item)
        content = ''.join(contentlist2)
        if len(column) == 0:
            try:
                begin("Delete content from table %s" % table)
                cur.execute("delete from "+table)
                commit("Delete content in table %s successful" % table)
            except:
                rollback('Delete content in table %s not successful' % table)
        else:
            if '_id' in column:
                try:
                    begin("Delete content in table %s" % table)
                    cur.execute(
                                "delete from "+
                                table+" where "+
                                column+" = "+content
                                )
                    commit("Delete content in table %s successful" % table)
                except:
                    rollback('Delete content in table %s not successful' % table)
            else:
                try:
                    begin("Delete content in table %s" % table)
                    cur.execute(
                                "delete from "+table+
                                " where "+
                                column+" like "+content
                                )
                    commit("Delete content in table %s successful" % table)
                except:
                    rollback('Delete content in table %s not successful' % table)

    '''
    if len(columnlist) == 1:
        for item in columnlist:
            item ="'"+table+"_"+str(item)+"'"
            columnlist2.append(item)
    column = ''.join(columnlist2)
    contentlist2 = []
    for item in contentlist:
        item = "'"+str(item)+"'"
        contentlist2.append(item)
    content = ''.join(contentlist2)
    if len(column) == 0:
        try:
            cur.execute("begin")
            cur.execute("delete from "+table)
            cur.execute("commit")
            string = "Clear table: "+table
            writeTarget(string)
        except:
            rollback()
    else:
        if '_id' in column:
            try:
                cur.execute("begin")
                cur.execute(
                    "delete from "+
                    table+" where "+
                    column+" = "+content
                )
                cur.execute("commit")
                string = "delete from "+table+" where "+column+" = "+content
                writeTarget(string)
            except:
                rollback()
        else:
            try:
                cur.execute("begin")
                cur.execute(
                    "delete from "+table+
                    " where "+
                    column+" like "+content)
                cur.execute("commit")
                string = "delete from "+table+" where "+column+" like "+content
                writeTarget(string)
            except:
                rollback()
'''
