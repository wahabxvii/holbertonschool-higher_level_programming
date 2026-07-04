#!/usr/bin/python3
import json
"""Module that has the from_json_string function"""


def from_json_string(my_str):
    """Function that return a JSON stirng of
    python data structure"""
    return json.loads(my_str)
