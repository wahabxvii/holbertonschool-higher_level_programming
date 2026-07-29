#!/usr/bin/python3
'''A scirpt that lists id, name in states table.'''

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
    )

    cursor = db.cursor()

    state = sys.argv[4]
    query = f"SELECT * FROM states WHERE BINARY name = '{state}' ORDER BY id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
