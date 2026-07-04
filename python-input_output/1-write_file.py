#!/usr/bin/python3
"""Mudole that has a write_file function"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file."""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
