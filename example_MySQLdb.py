#!/usr/bin/python
import MySQLdb

from settings import *

my_db = 'pq'

db = MySQLdb.connect(host=my_host, # your host, usually localhost
                     user=my_user, # your username
                      passwd=my_passwd, # your password
                      db=my_db) # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM pq_jobs")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]
