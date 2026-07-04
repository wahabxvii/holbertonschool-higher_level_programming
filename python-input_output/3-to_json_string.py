#!/usr/bin/python3
"""Module that has the to_json_string function"""


import json



def to_json_string(my_obj):
    """Function that returns the JSON representation of an obj."""
    return json.dumps(my_obj)
