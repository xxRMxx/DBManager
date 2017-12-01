# logic for database options

global conn
global cur
conn = ""
cur = ""


# function to open a database connection
def openDB(database, user, password, host):
    global conn # do I need this? Definition is above
    global cur # do I need this? Definition is above
    conn = 0
    try:
        if conn != 0:
                conn.close()
        if host == "":
            if len(password) == 0:
                conn = psycopg2.connect(
                    "dbname='"+database+
                    "' user='"+user+"'"
                )
                cur = conn.cursor()
                writeTarget("Connection established: database "+database+", current user "+user)
            else:
                conn = psycopg2.connect(
                    "dbname='"+database+
                    "' user='"+user+
                    "' password='"+password+"'"
                )
                cur = conn.cursor()
                writeTarget("Connection established: database "+database+", current user "+user)
        else:
            if len(password) == 0:
                conn = psycopg2.connect(
                    "dbname='"+database+
                    "' user='"+user+
                    "' host='"+host+"'"
                )
                cur = conn.cursor()
                writeTarget("Connection established: database "+database+", current user "+user)
            else:
                conn = psycopg2.connect(
                    "dbname='"+database+
                    "' user='"+user+
                    "' password='"+password+
                    "' host='"+host+"'"
                )
                cur = conn.cursor()
                writeTarget("Connection established: database "+database+", current user "+user)
    except:
        rollback("Connecting to database failed")


# function for closing a database connection
def closeDB():
    if cur == "":
        root.quit()
    else:
        try:
            conn.rollback()
            conn.close()
            writeTarget("Connection closed")
            root.quit()
        except:
            rollback("Connection closed")
            sys.exit(1)
