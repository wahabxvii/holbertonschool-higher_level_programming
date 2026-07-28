#!/usr/bin/python3
'''A scirpt that lists id, name in states table.'''
import sys

import MySQLdb


db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    name=sys.argv[3])

cursor = db.cursor()

query = "SELECT id, name FROM states ORDER BY id ASC"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()
