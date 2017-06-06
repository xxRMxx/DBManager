# logic for database options

# import psycopg2

global conn
global cur
conn = ""
cur = ""

# functions for the db
def openDB():
    global conn
    global cur
    global dbname
    global user
    global password
    global host
    dbname = tab1DBName.get()
    user = tab1UserName.get()
    password = tab1Password.get()
    host = tab1Host.get()
    conn = 0
    try:
        if conn != 0:
                conn.close()
        if host == "":
            if len(password) == 0:
                conn = psycopg2.connect(
                    "dbname='"+dbname+
                    "' user='"+user+"'"
                )
                cur = conn.cursor()
                string = "Connection established: database "+dbname+", current user "+user
                writeTarget(string)
            else:
                conn = psycopg2.connect(
                    "dbname='"+dbname+
                    "' user='"+user+
                    "' password='"+password+"'"
                )
                cur = conn.cursor()
                string = "Connection established: database "+dbname+", current user "+user
                writeTarget(string)
        else:
            if len(password) == 0:
                conn = psycopg2.connect(
                    "dbname='"+dbname+
                    "' user='"+user+
                    "' host='"+host+"'"
                )
                cur = conn.cursor()
                string = "Connection established: database "+dbname+", current user "+user
                writeTarget(string)
            else:
                conn = psycopg2.connect(
                    "dbname='"+dbname+
                    "' user='"+user+
                    "' password='"+password+
                    "' host='"+host+"'"
                )
                cur = conn.cursor()
                string = "Connection established: database "+dbname+", current user "+user
                writeTarget(string)
    except:
        rollback()

def closeDB():
    if cur == "":
        root.quit()
    else:
        try:
            conn.rollback()
            conn.close()
            string = "Connection closed"
            writeTarget(string)
            root.quit()
        except:
            rollback()
            sys.exit(1)
