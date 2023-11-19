#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    state_name = argv[4]

    db = MySQLdb.connect(host="hostname", username=argv[1],
                         passwd=argv[2], port="3306", db=argv[3])

    cur = db.cursor()
    sql_query = "SELECT * FROM states \
                 WHERE name LIKE BINARY %s \
                 ORDER BY state.id ASC"
    cur.execute(sql_query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
