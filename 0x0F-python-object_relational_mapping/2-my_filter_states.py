#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Function that takes in an argument and displays all values
    in the states table of db where name matches the argument"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host="localhost")

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = '{}'\
            ORDER BY id ASC".format(sys.argv[4]))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
