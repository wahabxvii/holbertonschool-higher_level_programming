#!/usr/bin/python3
"""Module includes convert_csv_to_json function."""


import csv
import json


def convert_csv_to_json(filename):
    """Convert csv to json."""
    try:
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        return True
    except FileNotFoundError:
        return False
