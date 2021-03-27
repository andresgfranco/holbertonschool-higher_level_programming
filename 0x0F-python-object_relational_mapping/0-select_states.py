#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    """main function that lists all states from the database"""
    db = MySQLdb.connect(user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            host="localhost")

    cur = db.cursor()

    cur.execute("SELECT * FROM states")

    for row in cur.fetchall():
        print(row[0], " ", row[1])

    cur.close()
    db.close()
