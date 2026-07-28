#!/usr/bin/python3
'''A scirpt that lists id, name in states table.'''
import sys

import MySQLdb


user = sys.argv[1]
password = sys.argv[2]
name = sys.argv[3]


db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, name=name)
cursor = db.cursor()

query = "SELECT id, name FROM states ORDER BY id ASC"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()
