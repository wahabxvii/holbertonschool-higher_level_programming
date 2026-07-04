#!/usr/bin/python3
"""Module that includes the load_from_json_file function"""

import json


def load_from_json_file(filename):
    """Module that includes the load_from_json_file function"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
