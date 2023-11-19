#!/usr/bin/python3
"""
A script that displays all states with a name starting with N
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    The access get states from the database
    """

    db = MySQLdb.connect(host="localhost", username=argv[1],
                         passwd=argv[2], port="3306", db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '%N' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
