# logic for building diagrams


# function for creating a diagram
def createDia(database, user, table):
    dumpname = database+".sql"
    '''
    pg_dump test -U raphael > test.sql
    cat test.sql | pf_dump2graph -n test1 -d svg
    '''
    try:
        databasedump = subprocess.Popen(
                                        "pg_dump -s -d "+database+" -U "+user+" > "+dumpname, shell = True
                                        )
        writeTarget("creating dump successful") # this works
    except:
        writeTarget("Error in creating dump")
    time.sleep(2) # take a short nap so that the dump can be created
    try:
        subprocess.call(
                        "cat %s | pf_dump2graph -n ./%s -d svg" % (dumpname, database), shell = True
                        )
        writeTarget("creating svg file successfull")
    except:
        writeTarget("creating svg file not successfull")
