# logic for sequences


# function for reset a sequence
def setSequence(table):
    try:
        begin("Restart sequence")
        cur.execute(
            "alter sequence "+
            sequence+"_"+sequence+"_id_seq restart"
        )
        commit("Restart sequence successful")
    except:
        rollback("Restart sequence failed")
