#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1],
         passwd=sys.argv[2],
         db=sys.argv[3],
         port=3306,
         host="localhost")

cur = db.cursor()

cur.execute("SELECT cities.id, cities.name, states.name\
        FROM cities\
        INNER JOIN states ON states.id = cities.state_id")
for row in cur.fetchall():
    print(row)

