#!/usr/bin/python3
import json
"""Module that has the to_json_string function"""


def to_json_string(my_obj):
    """Function that returns the JSON representation of an obj."""
    return json.dumps(str(my_obj))
