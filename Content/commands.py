#!/usr/bin/env python
# -*- coding: utf-8 -*-


# function for inserting content in table
def insert(table, column, content, column2, content2):
    columnlist = column.split(", ")
    contentlist = content.split(", ")
    columnlist2 = []

    for item in columnlist:
        item = ", " + item
        columnlist2.append(item)

    column = ''.join(columnlist2)
    contentlist2 = []

    for item in contentlist:
        item = ", " + "'" + str(item) + "'"
        contentlist2.append(item)

    content = ''.join(contentlist2)

    if len(content) == 0:
        string = "No content given"
        writeTarget(string)
    else:
        try:
            begin("Inserting content into table %s" % (table))
            cur.execute("insert into %s (%s_id, %s_modtime, %s_author, %s) values (default, now(), %s, %s" % (table, table, table, table, column, user, content))
            commit("Inserting data into table %s successful" % (table))
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
            begin("Updating content in table %s" % (table))
            cur.execute("update %s set %s = %s where %s = %s" % (table, column, content, column2, content2))
            commit("Updating content in table %s successful" % (table))
        except:
            rollback('Updating content in table %s not successful' % (table))
    else:
        try:
            begin("Updating content in table %s" % (table))
            cur.execute("update %s set %s = %s where %s like '%s'" % (table, column, content, column2, content2))
            commit("Updating content in table %s successful" % (table))
        except:
            rollback('Updating content for table %s not successful' % (table))


# function for deleting an entry in table
def delete(table, column, content, column2, content2):
    columnlist = column.split(", ")
    contentlist = content.split(", ")
    columnlist2 = []

    val = tkMessageBox.askyesno(
        "Confirmation",
        "Do you really want to delete the content?"
    )
    if val == True:
        tkMessageBox.showinfo(
            "NOTE",
            "Remember to restart the sequence."
        )
        if len(columnlist) == 1:
            for item in columnlist:
                item = "%s_%s" % (table, item)
                columnlist2.append(item)

        column = ''.join(columnlist2)
        contentlist2 = []

        for item in contentlist:
            contentlist2.append(item)

        content = ''.join(contentlist2)

        if len(column) == 0:
            try:
                begin("Delete content from table %s" % (table))
                cur.execute("delete from %s" % (table))
                commit("Delete content in table %s successful" % (table))
            except:
                rollback('Delete content in table %s not successful' % (table))
        else:
            if '_id' in column:
                try:
                    begin("Delete content in table %s" % (table))
                    cur.execute("delete from %s where %s = %s" % (table, column, content))
                    commit("Delete content in table %s successful" % (table))
                except:
                    rollback('Delete content in table %s not successful' % (table))
            else:
                try:
                    begin("Delete content in table %s" % (table))
                    cur.execute("delete from %s where %s like '%s'" % (table, column, content))
                    commit("Delete content in table %s successful" % (table))
                except:
                    rollback('Delete content in table %s not successful' % (table))
