# logic for building diagrams


# ToDo:
# do not allow to enter a database here

# function for creating a diagram
def createDia(user, table):

    database = "'%s'" % (databaseInputFields[0].get())

    raise ValueError("Not supported yet.")
    dumpname = database + ".sql"
    '''
    pg_dump test -U raphael > test.sql
    cat test.sql | pf_dump2graph -n test1 -d svg
    '''
    try:
        databasedump = subprocess.Popen(
            "pg_dump -s -d %s -U %s > %s" % (database, user, dumpname),
            shell = True
        )
        writeTarget("creating dump successful")
    except: # describe to concrete exception
        writeTarget("Error in creating dump")
    time.sleep(2) # take a short nap so that the dump can be created

    try:
        subprocess.call(
            "cat %s | pf_dump2graph -n ./%s -d svg" % (dumpname, database),
            shell = True
        )
        writeTarget("creating svg file successfull")
    except: # describe the concrete exception
        writeTarget("creating svg file not successfull")
