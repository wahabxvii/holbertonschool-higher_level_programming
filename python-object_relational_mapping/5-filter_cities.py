#!/usr/bin/python3
"""A scirpt that lists id, name in states table."""

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
    query = ("""
    SELECT cities.name FROM cities
    LEFT JOIN states ON states.id = cities.state_id
    WHERE state.name = %s
    ORDER BY cities.id ASC
             """, (state,))

    cursor.execute(query)

    rows = cursor.fetchall()

    print(", ".join(row[0] for row in rows))

    cursor.close()
    db.close()
