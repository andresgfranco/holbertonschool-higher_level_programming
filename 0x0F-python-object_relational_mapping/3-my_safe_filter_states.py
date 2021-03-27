#!/usr/bin/python3
""" script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!"""
import MySQLdb
import sys

def main():
    db = MySQLdb.connect(user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            host="localhost")

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4], ))

    for row in cur.fetchall():
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
