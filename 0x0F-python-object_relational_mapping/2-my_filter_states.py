#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1],
         passwd=sys.argv[2],
         db=sys.argv[3],
         port=3306,
         host="localhost")

cur = db.cursor()

cur.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))

for row in cur.fetchall():
    print(row)
