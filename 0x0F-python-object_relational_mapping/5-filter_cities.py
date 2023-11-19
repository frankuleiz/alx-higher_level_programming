#!/usr/bin/python3
"""
The script takes in the name of a state as an argument amd lists
all cities of that state in the database that is SQL injection free
"""
import sys
import MySQLdb

state_name = argv[4]

db = MySQLdb.connect(host="localhost", username=argv[1],
                     passwd=argv[2], port="3306", db=argv[3])

cur = db.cursor()
sql_query = "SELECT cities.id, cities.name \
             FROM cities \
             JOIN states \
             ON cities.state_id = states.id \
             WHERE states.name LIKE BINARY %s \
             ORDER BY cities.id ASC"
cur.execute(sql_query, (state_name,))
rows = cur.fetchall()

if rows is not None:
    print(", ".join([row[1] for row in rows]))
