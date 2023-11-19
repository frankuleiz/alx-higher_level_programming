#!/usr/bin/python3
"""
The script lists all the cities from the databaswe
"""

import sys
import MySQLdb
from mysql.connector import Error

db = MySQLdb.connect(host="localhost", username=argv[1],
                     passwd=argv[2], port="3306", db=argv[3])

cur = db.cursor()
cur.execute("SELECT * FROM cities ORDER BY cities.id")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
db.close()
