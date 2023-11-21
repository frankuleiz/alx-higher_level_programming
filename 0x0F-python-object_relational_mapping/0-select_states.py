#!/usr/bin/python3
"""
A script that lists all states from the databases
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    The access to get states from the database
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port="3306",
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
