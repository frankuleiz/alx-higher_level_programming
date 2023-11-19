#!/usr/bin/python3
""""
This script takes an argument and displays all values in the
states table where name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Gives access to states in the database
    """
    db = MySQLdb.connect(host="localhost", username=argv[1],
                         passwd=argv[2], port="3306", db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
