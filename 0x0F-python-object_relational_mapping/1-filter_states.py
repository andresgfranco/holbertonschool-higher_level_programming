#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def main():
    db = MySQLdb.connect(user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            host="localhost")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    for row in cur.fetchall():
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
