#!/usr/bin/python3
'''A scirpt that lists id, name in states table.'''
import MySQLdb

import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        name=sys.argv[3])

    cursor = db.cursor()

    state = sys.argv[4]
    query = f"SELECT * FROM {state} ORDER BY states.id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
