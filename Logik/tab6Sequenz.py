# logic for sequences

def setSequence(tablename):
    if tablename == "":
        sequencename = tab6SequenceName.get()
    try:
        cur.execute("begin")
        cur.execute(
            "alter sequence "+
            sequencename+"_"+sequencename+"_id_seq restart"
        )
        cur.execute("commit")
        string = "alter sequence "+sequencename+"_"+sequencename+"_id_seq restart"
        writeTarget(string)
    except:
        rollback()
