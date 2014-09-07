#! ./venv/bin/python

# This example lists all tables in all databases on the listed server
# Note: it expects a file settings.py with the following variable names
#my_host = 'localhost'
#my_user = 'root'
#my_passwd = 'passwd'

import MySQLdb

import settings

db_server = MySQLdb.connect(host=settings.my_host, 
                            user=settings.my_user, 
                            passwd=settings.my_passwd)

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur0 = db_server.cursor() 

# Use all the SQL you like
cur0.execute("SHOW DATABASES")

# print all the first cell of all the rows
for db_name in cur0.fetchall() :
    db = MySQLdb.connect(host=settings.my_host, 
                         user=settings.my_user, 
                         passwd=settings.my_passwd,
                         db=db_name[0])
    print db_name[0]
    cur = db.cursor() 
    cur.execute("SHOW TABLES")
    for table_name in cur.fetchall() :
        print '    ' + table_name[0]

