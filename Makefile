# This is the MAKEFILE to install all neccessary dependencies.
# This Makefile also creates the log file.
#

install:
	sudo apt install python2.7 python-tk python-psycopg2
	sudo touch /var/log/dbmanager.log
	sudo chmod 666 /var/log/dbmanager.log
