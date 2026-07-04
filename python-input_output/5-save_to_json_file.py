#!/usr/bin/python3
"""Module that include the save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """Module that include the save_to_json_file function"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
