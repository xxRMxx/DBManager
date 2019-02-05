#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this file contains the main functions of the application

import subprocess
import imp


# write a line into logfile (/var/log/dbmanager.log)
def writeTarget(string):
    target = open(filename, 'a')
    target.write(timestamp + ": %s\n" % (string))
    target.close()


# wrapper for database transaction 'begin'
def begin(string):
    cur.execute("begin")
    writeTarget(string)


# wrappter for database transaction 'commit'
def commit(string):
    cur.execute("commit")
    text_info.delete(1.0, END)
    text_info.insert(1.0, string)
    writeTarget(string)


# wrapper for database transaction 'rollback'
def rollback(string):
    try:
        cur.execute("rollback")
        text_info.delete(1.0, END)
        text_info.insert(1.0, string)
        writeTarget(string)
    except AttributeError:
        writeTarget("No connection string defined. Rollback.")


# wrapper for executed shell commands
def popen(string):
    call = subprocess.Popen("%s" % (string), shell = True, stdout = subprocess.PIPE)
    return call
